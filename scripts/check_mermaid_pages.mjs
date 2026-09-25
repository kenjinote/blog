// Integration check against Hugo-built pages served by a local HTTP server.
// node scripts/check_mermaid_pages.mjs SITE_DIR BASE_URL REPORT PLAYWRIGHT_MODULE
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const [site, base, output, modulePath] = process.argv.slice(2);
const {chromium} = createRequire(import.meta.url)(modulePath || 'playwright');
const targets=[];
function walk(dir) {
  for(const file of fs.readdirSync(dir,{withFileTypes:true})) {
    const name=path.join(dir,file.name);
    if(file.isDirectory()) walk(name);
    else if(file.name==='index.html') {
      const html=fs.readFileSync(name,'utf8');
      const count=[...html.matchAll(/<(?:pre|div) class="mermaid"/g)].length;
      if(count) targets.push({url:new URL(path.relative(site,name).split(path.sep).map(encodeURIComponent).join('/'),base).href,count});
    }
  }
}
walk(site);
const browser=await chromium.launch({channel:'msedge',headless:true});
const context=await browser.newContext({viewport:{width:1440,height:1000}});
const results=[];let next=0;
try {
  await Promise.all(Array.from({length:4},async()=>{
    const page=await context.newPage();
    while(next<targets.length) {
      const target=targets[next++];const errors=[];
      const onError=e=>errors.push(e.message);page.on('pageerror',onError);
      try {
        await page.goto(target.url,{waitUntil:'domcontentloaded'});
        await page.waitForFunction(()=>[...document.querySelectorAll('.mermaid')].every(el=>{
          // Mermaid temporarily inserts a nested placeholder SVG while rendering.
          // Only its final direct-child SVG counts as a completed diagram.
          const svg=el.querySelector(':scope > svg');
          const box=svg?.getBoundingClientRect();
          return svg && svg.querySelector('g') && box.width>0 && box.height>0 && !el.querySelector('.error-icon,.error-text');
        }),null,{timeout:30000});
        const rendered=await page.locator('.mermaid > svg').count();
        if(rendered!==target.count)throw new Error(`Expected ${target.count} diagrams, got ${rendered}`);
        const mermaidModules=await page.locator('script').evaluateAll(nodes=>nodes.filter(n=>(n.src+' '+n.textContent).includes('cdn.jsdelivr.net/npm/mermaid@')).length);
        if(mermaidModules!==1)throw new Error(`Expected one Mermaid loader, got ${mermaidModules}`);
        if(target.url===new URL('p/physics-lithium-ion/index.html',base).href)
          await page.locator('.mermaid').first().screenshot({path:path.join(path.dirname(output),'physics-lithium-ion.png')});
        results.push({...target,ok:true,rendered,mermaidModules,errors});
      } catch(e) {results.push({...target,ok:false,error:String(e),errors});}
      page.off('pageerror',onError);
      if(results.length%13===0)console.log(`${results.length}/${targets.length}`);
    }
    await page.close();
  }));
} finally {
  fs.writeFileSync(output,JSON.stringify(results,null,2)+'\n');
  await Promise.race([browser.close(),new Promise(resolve=>setTimeout(resolve,5000))]);
}
console.log(JSON.stringify({pages:results.length,errors:results.filter(r=>!r.ok).length}));
process.exit(results.some(r=>!r.ok)?1:0);
