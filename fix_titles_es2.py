import os, re, glob, yaml, sys
base = r'c:/work/kenji.blog/content/post'
bad_files = []
for path in glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True):
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
        # Extract title line
        title_match = re.search(r'^(title:\s*)(.*)', content, flags=re.MULTILINE)
        if title_match:
            prefix = title_match.group(1)
            raw = title_match.group(2).strip()
            # Remove surrounding quotes if any
            if raw.startswith("'") and raw.endswith("'"):
                raw = raw[1:-1]
            elif raw.startswith('"') and raw.endswith('"'):
                raw = raw[1:-1]
            # Escape double quotes for YAML double-quoted string
            escaped = raw.replace('"', '\\"')
            # Replace title line
            new_title_line = f"{prefix}\"{escaped}\""
            new_content = re.sub(r'^title:\s*.*', new_title_line, content, flags=re.MULTILINE)
        else:
            new_content = content
        # Write back if changed
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        # Validate frontmatter
        parts = new_content.split('---')
        if len(parts) >= 3:
            front = parts[1]
            yaml.safe_load(front)
        else:
            raise Exception('Missing frontmatter delimiters')
    except Exception as e:
        bad_files.append((path, str(e)))
# Write bad list to file
bad_path = os.path.join(base, 'bad_es.txt')
with open(bad_path, 'w', encoding='utf-8') as bf:
    for p, err in bad_files:
        bf.write(f"{p}\t{err}\n")
print('Processed files:', len(glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True)))
print('YAML errors after fix:', len(bad_files))
print('Bad files written to', bad_path)
