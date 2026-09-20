import os
import re

dir_path = r'c:\work\kenji.blog\content\post\cryptocurrency-and-bitcoin'

# We want to replace inline block math $$...$$ with inline math $...$
# Inline block math is typically on the same line.
# Regex to find $$ followed by non-newline characters and then $$
pattern = re.compile(r'\$\$(.+?)\$\$')

count = 0
for file in os.listdir(dir_path):
    if file.endswith('.md'):
        file_path = os.path.join(dir_path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Sub function to decide whether to change
            def replacer(match):
                inner = match.group(1)
                # if there is a newline inside, it's likely a real block math, keep it $$
                if '\n' in inner or '\\begin' in inner:
                    return f"$${inner}$$"
                else:
                    return f"${inner}$"
            
            new_content = pattern.sub(replacer, content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
        except Exception:
            pass

print(f"Fixed inline math in {count} files.")
