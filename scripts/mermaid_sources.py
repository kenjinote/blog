"""Extract Mermaid fences without reserializing the surrounding Markdown."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def blocks(text):
    offset, opened, start, mermaid = 0, None, 0, False
    found, fences, fence_start = [], [], 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^[ \t]{0,3}(`{3,}|~{3,})([^\r\n]*)', line)
        if opened:
            if marker and marker[1][0] == opened[0] and len(marker[1]) >= len(opened) and not marker[2].strip():
                if mermaid:
                    found.append((start, offset, text[start:offset]))
                fences.append((fence_start, offset + len(line)))
                opened = None
        elif marker:
            opened = marker[1]
            fence_start = offset
            mermaid = marker[2].strip().split(' ', 1)[0] == 'mermaid'
            start = offset + len(line)
        offset += len(line)
    if opened:
        fences.append((fence_start, len(text)))
    for match in re.finditer(r'\{\{[<%]\s*mermaid\b[^\r\n]*?[>%]\}\}(.*?)\{\{[<%]\s*/mermaid\s*[>%]\}\}', text, re.S):
        if not any(a <= match.start() < b for a, b in fences):
            found.append((*match.span(1), match[1]))
    yield from sorted(found)


def inventory():
    result = []
    for p in sorted((ROOT/'content').rglob('*.md')):
        text = p.read_bytes().decode('utf-8')
        for number, (start, end, source) in enumerate(blocks(text)):
            result.append({'path': p.relative_to(ROOT).as_posix(), 'block': number,
                           'start': start, 'end': end, 'source': source})
    return result


if __name__ == '__main__':
    items = inventory()
    Path(sys.argv[1]).write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
    print(f'{len(items)} diagrams in {len(set(d["path"] for d in items))} articles')
