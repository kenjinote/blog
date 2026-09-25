// Validate extracted diagrams in a real browser using the site's pinned Mermaid.
// node scripts/check_mermaid.mjs INPUT.json OUTPUT.json MERMAID.js PLAYWRIGHT_MODULE [--render]
import fs from 'node:fs';
import { createRequire } from 'node:module';
import { createHash } from 'node:crypto';
const [input, output, library, playwrightPath, ...flags] = process.argv.slice(2);
const { chromium } = createRequire(import.meta.url)(playwrightPath || 'playwright');
const browser = await chromium.launch({ channel: 'msedge', headless: true });
const diagrams = JSON.parse(fs.readFileSync(input, 'utf8'));
const results = new Array(diagrams.length);
const previous = flags.includes('--resume') && fs.existsSync(output)
  ? new Map(JSON.parse(fs.readFileSync(output, 'utf8')).map(r => [r.path + ':' + r.block, r])) : new Map();
let next = 0, finished = 0;
try {
  await Promise.all(Array.from({length: 4}, async () => {
    let page;
    const setup = async () => {
      page = await browser.newPage();
      await page.setContent('<!doctype html><html><body></body></html>');
      await page.addScriptTag({path: library});
      await page.evaluate(() => mermaid.initialize({startOnLoad: false, theme: 'neutral'}));
    };
    await setup();
    while (next < diagrams.length) {
      const i = next++, diagram = diagrams[i];
      const sourceHash = createHash('sha256').update(diagram.source).digest('hex');
      const prior = previous.get(diagram.path + ':' + diagram.block);
      if (prior?.source_sha256 === sourceHash && (!flags.includes('--render') || prior.rendered)) {
        results[i] = previous.get(diagram.path + ':' + diagram.block); finished++; continue;
      }
      let timer;
      try {
      results[i] = await Promise.race([page.evaluate(async ({diagram, i, render}) => {
        try {
          const parsed = await mermaid.parse(diagram.source);
          if (render) {
            const {svg} = await mermaid.render('audit' + i, diagram.source);
            const host = document.createElement('div');
            host.innerHTML = svg; document.body.append(host);
            const el = host.querySelector('svg');
            const box = el?.getBoundingClientRect();
            if (!el || !box.width || !box.height || host.querySelector('.error-icon, .error-text'))
              throw new Error('SVG did not render with nonzero dimensions');
            host.remove();
          }
          return {path: diagram.path, block: diagram.block, ok: true, type: parsed.diagramType};
        } catch (e) {
          document.body.replaceChildren();
          return {path: diagram.path, block: diagram.block, ok: false, error: String(e.message || e)};
        }
      }, {diagram, i, render: flags.includes('--render')}),
      new Promise((_, reject) => { timer = setTimeout(() => reject(new Error('Browser validation timed out after 20 seconds')), 20000); })]);
      } catch (e) {
        results[i] = {path: diagram.path, block: diagram.block, ok: false, error: String(e.message || e)};
        fs.writeFileSync(output, JSON.stringify(results.filter(Boolean), null, 2) + '\n');
        await page.close({runBeforeUnload: true}); await setup();
      } finally { clearTimeout(timer); }
      results[i].source_sha256 = sourceHash;
      results[i].rendered = flags.includes('--render') && results[i].ok;
      finished++;
      if (finished % 250 === 0) {
        console.log(`${finished}/${diagrams.length}`);
        fs.writeFileSync(output, JSON.stringify(results.filter(Boolean), null, 2) + '\n');
      }
    }
    await page.close({runBeforeUnload: true});
  }));
} finally {
  fs.writeFileSync(output, JSON.stringify(results, null, 2) + '\n');
  await Promise.race([browser.close(), new Promise(resolve => setTimeout(resolve, 5000))]);
}
console.log(JSON.stringify({checked: results.length, errors: results.filter(r => !r.ok).length}));
process.exit(results.some(r => !r.ok) ? 1 : 0);
