"""Generate reviewed syntax repairs only for diagrams rejected by Mermaid.

Generate proposals: python -B scripts/repair_mermaid.py INVENTORY ERRORS PROPOSALS
Apply only after browser rendering: add --apply VALIDATION_REPORT
"""
import argparse
import json
import hashlib
import re
from collections import defaultdict
from pathlib import Path
from mermaid_sources import ROOT, blocks


def quoted(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    # Earlier regex repairs accidentally quoted arguments inside math labels.
    value = re.sub(r'\("([^"\r\n]*)"\)', r'(\1)', value)
    return '"' + value.replace('"', '#quot;').replace('|', '#124;') + '"'


def repair(source, path):
    newline = '\r\r\n' if '\r\r\n' in source else '\r\n' if '\r\n' in source else '\n'
    s = source.replace('\r\r\n', '\n').replace('\r\n', '\n')
    if s.lstrip().startswith(('graph ', 'flowchart ')):
        # Quotes mistakenly inserted before array-index closing brackets.
        s = re.sub(r'(\[[^\[\]"\n]+)"\]', r'\1]', s)
        lines, declarations, identifiers = [], [], {}
        for line in s.splitlines():
            if line.lstrip().startswith('%%'):
                lines.append(line); continue
            # A quoted node ID is not a quoted display label.
            def node_id(m):
                before, after = line[:m.start()], line[m.end():]
                context = (not before.strip() or re.search(r'(?:-->|---|\.->|<-->|\bstyle|\bclass)\s*$', before)
                           or (before.rstrip().endswith('|') and before.count('|') % 2 == 0)
                           or (before.rstrip().endswith(',') and re.match(r'\s*class\s', line)))
                if not context or before.rstrip().endswith('subgraph'):
                    return m[0]
                label = m[1]
                if re.fullmatch(r'[A-Za-z_]\w*', label):
                    return label
                if label not in identifiers:
                    identifier = f'repairedNode{len(identifiers)+1}'
                    identifiers[label] = identifier
                    declarations.append(f'    {identifier}[{quoted(label)}]')
                return identifiers[label]
            line = re.sub(r'"([^"\n]*)"', node_id, line)
            sub = re.match(r'(\s*subgraph\s+)(.*)', line)
            if sub:
                title = sub[2].strip()
                broken = re.fullmatch(r'"(.+?)\s*\["(.*)"\]"', title)
                explicit = re.fullmatch(r'([\w-]+)\s*\[(.*)\]', title)
                if broken:
                    # Preserve both original title and translated title.
                    title = quoted(broken[1].strip() + ' / ' + broken[2])
                elif explicit:
                    title = explicit[1] + ' [' + quoted(explicit[2]) + ']'
                else:
                    title = quoted(title)
                lines.append(sub[1]+title)
                if 'physics-lithium-ion/' in path:
                    # Explicit direction keeps the battery diagram wide enough
                    # for its group heading instead of wrapping over the nodes.
                    lines.append(re.match(r'\s*',line)[0]+'    direction LR')
                continue
            # Invalid --|label| and --|label|--> arrow spellings.
            line = re.sub(r'--\|(.+?)\|-->', r'-->|\1|', line)
            line = re.sub(r'(?<!-)--\|', '-->|', line)
            # Two labels on the same arrow: retain both as one label.
            line = re.sub(r' -- ([^|\n]+?) -->\|([^\n]+)\|',
                          lambda m: ' -->|' + quoted(m[1]+' / '+m[2]) + '|', line)
            # Pipe label contents may themselves contain accidental pipes/quotes.
            line = re.sub(r'((?:-->|\.->|---|<-->)\s*)\|(.+)\|(?=\s*[\w"])',
                          lambda m: m[1]+'|'+quoted(m[2])+'|', line)
            line = re.sub(r'( -- | -\. )(.+?)( --> | \.-> )',
                          lambda m: m[1]+quoted(m[2])+m[3], line)
            # Quote plain rectangular/decision labels that contain punctuation.
            line = re.sub(r'(\b\w+)(\[|\{)([^"\[\]{}\n]+)(\]|\})',
                          lambda m: (m[1]+m[2]+quoted(m[3])+m[4]) if line[:m.start()].count('"')%2==0 else m[0], line)
            # Quoted round-node labels with extra quotes in function arguments.
            line = re.sub(r'(\b\w+\(\(?)(".*?")(\)\)?)(?=\s*(?:$|--|\.))',
                          lambda m: m[1]+quoted(m[2])+m[3], line)
            note = re.match(r'\s*Note over ([\w,]+):\s*(.*)', line)
            if note:
                line = '    diagramNote[' + quoted(note[2]) + ']'
                # A note is an annotation, not an extra data-flow edge.
            lines.append(line)
        s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')
        if declarations:
            first = s.index('\n')+1
            s = s[:first]+'\n'.join(declarations)+'\n'+s[first:]
    elif s.lstrip().startswith('stateDiagram'):
        aliases = {}
        # Flowchart node labels must be state descriptions in a state diagram.
        for m in re.finditer(r'(\b\w+)\["([^"\n]*)"\]', s):
            aliases.setdefault(m[1], m[2])
        # Keep action descriptions when a destination is labelled differently
        # on a later transition (e.g. "execute command" -> Normal).
        labelled_lines = []
        inline_definitions = set()
        for line in s.splitlines():
            standalone = re.fullmatch(r'(\s*)(\w+)\["([^"\n]*)"\]', line)
            if standalone:
                inline_definitions.add(standalone[2])
                labelled_lines.append(standalone[1]+'state '+quoted(standalone[3])+' as '+standalone[2])
                continue
            actions = []
            def plain_state(m):
                if aliases[m[1]] != m[2]: actions.append(m[2])
                return m[1]
            line = re.sub(r'(\b\w+)\["([^"\n]*)"\]', plain_state, line)
            if actions and '-->' in line:
                line += (' / ' if ':' in line else ' : ') + ' / '.join(actions)
            labelled_lines.append(line)
        for key in inline_definitions: aliases.pop(key)
        s='\n'.join(labelled_lines)+ ('\n' if s.endswith('\n') else '')
        names = {}
        lines = []
        for line in s.splitlines():
            if '-->' in line or re.match(r'\s*note (?:right|left)', line):
                lhs, sep, rhs = line.partition(':')
                def state_id(m):
                    name = m[1]
                    if re.fullmatch(r'[A-Za-z_]\w*', name): return name
                    key = names.setdefault(name, f'repairedState{len(names)+1}')
                    aliases[key] = name
                    return key
                lhs = re.sub(r'"([^"\n]+)"', state_id, lhs)
                line = lhs+sep+rhs
            lines.append(line)
        s = '\n'.join(lines)+ ('\n' if s.endswith('\n') else '')
        if aliases:
            i = s.index('\n')+1
            s = s[:i]+''.join(f'    state {quoted(v)} as {k}\n' for k,v in aliases.items())+s[i:]
    elif s.lstrip().startswith('classDiagram'):
        s = re.sub(r'(\bclass\s+)"([^"\n]+)"', r'\1\2', s)
        lines=[]
        for line in s.splitlines():
            if re.search(r'<\||\|>|<\.\.|--|\.\.>', line):
                lhs, sep, rhs = line.partition(' : ')
                lhs = re.sub(r'"(\w+)"', r'\1', lhs)
                if rhs.startswith('"') and rhs.endswith('"'):rhs=rhs[1:-1]
                rhs=rhs.replace(':', '#58;')
                line=lhs+sep+rhs
            lines.append(line)
        s='\n'.join(lines)+('\n' if s.endswith('\n') else '')
    elif s.lstrip().startswith('sequenceDiagram'):
        s=s.replace('<-->>', '<<-->>')
        s=re.sub(r'--x(?=\w)', '--x ', s)
        s=re.sub(r'(?m)^([^\n]*?:)([^\n]*)',lambda m:m[1]+m[2].replace(';','#59;'),s)
    elif s.lstrip().startswith('gantt') and 'browser-rendering-mechanism-dom-paint/' in path:
        # dateFormat s takes a numeric start time; trailing s is a duration suffix.
        # Keep the existing durations unchanged.
        s=re.sub(r'(,\s*)(\d+)s(?=,\s*\d+s\s*$)',r'\1\2',s,flags=re.M)
    elif s.lstrip().startswith('xychart'):
        s=re.sub(r'(?m)^(\s*title\s+)([^\n]+)', lambda m:m[1]+quoted(m[2]), s)
        # One quoted comma-separated list is a single category, not many categories.
        s=re.sub(r'(?m)^(\s*x-axis[^\n]*?)\["([^"\n]*,[^"\n]*)"\]',
                 lambda m:m[1]+'['+', '.join(quoted(v) for v in m[2].split(','))+']', s)
        s=re.sub(r'(?m)^(\s*(?:line|bar)\s+)\["([^"\n]+)"\]\s*(\[)', r'\1"\2" \3', s)
    elif s.lstrip().startswith('architecture-beta'):
        # This diagram uses flowchart edges and labels throughout; keep that model.
        s=s.replace('architecture-beta','flowchart TB',1)
        groups=re.findall(r'(?m)^\s*group (\w+)\("([^"\n]+)"\)',s)
        services=re.findall(r'(?m)^\s*service (\w+)\("([^"\n]+)"\) in (\w+)',s)
        edges=re.findall(r'(?m)^\s*(\w+ --> \w+)\s*$',s)
        s='flowchart TB\n'+''.join('    subgraph '+key+' ['+quoted(label)+']\n'+
            ''.join('        '+sid+'['+quoted(sl)+']\n' for sid,sl,g in services if g==key)+'    end\n'
            for key,label in groups)+''.join('    '+e+'\n' for e in edges)
    if 'physics-lithium-ion/' in path and s.lstrip().startswith('graph '):
        s="%%{init: {'flowchart': {'wrappingWidth': 400, 'subGraphTitleMargin': {'top': 8, 'bottom': 24}}}}%%\n"+s
    return s.replace('\n', newline)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('inventory',type=Path);ap.add_argument('errors',type=Path);ap.add_argument('proposals',type=Path)
    ap.add_argument('--apply',type=Path)
    args=ap.parse_args()
    originals=json.loads(args.inventory.read_text(encoding='utf-8'))
    failures={(r['path'],r['block']) for r in json.loads(args.errors.read_text(encoding='utf-8')) if not r['ok']}
    proposed=[dict(d,source=repair(d['source'],d['path'])) for d in originals if (d['path'],d['block']) in failures]
    if not args.apply:
        args.proposals.write_text(json.dumps(proposed,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'{len(proposed)} proposed repairs');return
    # Apply the reviewed proposal file, never generate new changes after validation.
    proposed=json.loads(args.proposals.read_text(encoding='utf-8'))
    verified={(r['path'],r['block'],r.get('source_sha256')) for r in json.loads(args.apply.read_text(encoding='utf-8')) if r['ok'] and r.get('rendered')}
    if any((d['path'],d['block'],hashlib.sha256(d['source'].encode('utf-8')).hexdigest()) not in verified for d in proposed):
        raise RuntimeError('Every proposed diagram must pass browser rendering before writing.')
    original_map={(d['path'],d['block']):d for d in originals}
    by_path=defaultdict(list)
    for d in proposed:
        old=original_map[d['path'],d['block']]
        if d['source']!=old['source']:by_path[d['path']].append((old,d))
    writes=[]
    for name,edits in by_path.items():
        p=ROOT/name;text=p.read_bytes().decode('utf-8');updated=text
        for old,new in sorted(edits,key=lambda e:e[0]['start'],reverse=True):
            if text[old['start']:old['end']]!=old['source']:
                raise RuntimeError(f'Concurrent edit detected: {name}')
            updated=updated[:old['start']]+new['source']+updated[old['end']:]
        # Only Mermaid interiors can differ; all surrounding source is identical.
        def surrounding(value):
            spans=list(blocks(value))
            for a,b,_ in reversed(spans):value=value[:a]+'MERMAID_SOURCE'+value[b:]
            return value
        if surrounding(text)!=surrounding(updated):raise RuntimeError(name)
        writes.append((p,text,updated))
    for p,text,_ in writes:
        if p.read_bytes()!=text.encode('utf-8'):raise RuntimeError(f'Concurrent edit: {p}')
    for p,_,text in writes:p.write_bytes(text.encode('utf-8'))
    print(f'Updated {len(writes)} articles, {sum(len(v) for v in by_path.values())} diagrams')


if __name__=='__main__':main()
