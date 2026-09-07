import os, re, glob, yaml, sys
base = r'c:/work/kenji.blog/content/post'
bad_files = []
for path in glob.glob(os.path.join(base, '**', '*.ko.md'), recursive=True):
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
        parts = content.split('---')
        if len(parts) < 3:
            raise Exception('Missing frontmatter delimiters')
        front = parts[1]
        # Process title line
        lines = front.splitlines()
        new_lines = []
        for line in lines:
            if line.lstrip().startswith('title:'):
                _, val = line.split(':', 1)
                val = val.strip()
                # Strip surrounding quotes if any
                if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
                    val = val[1:-1]
                # Escape double quotes
                escaped = val.replace('"', '\\"')
                new_line = f"title: \"{escaped}\""
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        new_front = "\n".join(new_lines)
        new_content = f"---\n{new_front}\n---\n" + "---".join(parts[2:])
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        yaml.safe_load(new_front)
    except Exception as e:
        bad_files.append((path, str(e)))
print('Processed .ko.md files:', len(glob.glob(os.path.join(base, '**', '*.ko.md'), recursive=True)))
print('Remaining YAML errors:', len(bad_files))
for p, e in bad_files:
    sys.stderr.write(f"{p}\t{e}\n")
