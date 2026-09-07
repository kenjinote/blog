import os, re, glob, yaml, sys
base = r'c:/work/kenji.blog/content/post'
bad_files = []
for path in glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True):
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
        # Fix title quoting patterns
        def escape_title(match):
            inner = match.group(1)
            # Escape single quotes by doubling them
            inner_escaped = inner.replace("'", "''")
            return f"title: '{inner_escaped}'"
        # First, handle titles that are incorrectly quoted with double quotes (already handled earlier)
        new_content = re.sub(r'title: "([^"]*)"', lambda m: f"title: '{m.group(1).replace("'", "''")}'", content)
        # Then handle titles that use single quotes but contain inner single quotes
        new_content = re.sub(r"title:\s*'([^']*)'", escape_title, new_content)
        # Also handle the previous pattern where title was using double single quotes ''...''
        new_content = re.sub(r"title: ''([^']+)''", lambda m: f"title: '{m.group(1).replace("'", "''")}'", new_content)
        # Write back if changed
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        # Validate YAML frontmatter
        parts = new_content.split('---')
        if len(parts) >= 3:
            front = parts[1]
            try:
                yaml.safe_load(front)
            except Exception as e:
                bad_files.append((path, str(e)))
        else:
            bad_files.append((path, 'Missing frontmatter delimiters'))
    except Exception as e:
        bad_files.append((path, f'Exception: {e}'))
print('Processed files:', len(glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True)))
print('YAML errors after fix:', len(bad_files))
for p, e in bad_files:
    sys.stderr.write(f"{p}: {e}\n")
