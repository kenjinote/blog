import os, re, glob, yaml, sys
base = r'c:/work/kenji.blog/content/post'
bad_files = []
for path in glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True):
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
        # Fix title quoting: replace title: ''...'' with title: "..."
        new_content = re.sub(r"title: ''([^']+)''", r'title: "\1"', content)
        # Fix title lines that use double quotes and contain inner double quotes: convert to single-quoted and escape inner single quotes
        def replace_double(match):
            inner = match.group(1)
            # escape any single quotes by doubling them
            inner_escaped = inner.replace("'", "''")
            return f"title: '{inner_escaped}'"
        new_content = re.sub(r'title: "([^"]*)"', replace_double, new_content)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        # Validate yaml frontmatter
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
        # Catch any file read/write errors
        bad_files.append((path, f'Exception: {e}'))
print('Processed files:', len(glob.glob(os.path.join(base, '**', '*.es.md'), recursive=True)))
print('YAML errors after fix:', len(bad_files))
for p, e in bad_files:
    sys.stderr.write(f"{p}: {e}\n")
