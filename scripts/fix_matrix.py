import os
import re

dir_path = r'c:\work\kenji.blog\content\post\method-of-least-squares'

for file in os.listdir(dir_path):
    if file.endswith('.md'):
        file_path = os.path.join(dir_path, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to replace `\\` with `\\\\` inside math blocks ($$ ... $$) and inline math ($ ... $)
        # A simpler way since `\\` is generally only used for math line breaks in this article,
        # is to carefully replace ` \\` or `\\` (not followed by another \) with `\\\\` 
        # But let's specifically target the bmatrix blocks first to be safe, or just do a general regex.
        # Actually, let's find `\\` followed by a newline and replace with `\\\\`
        # and `\\` inside `\begin{bmatrix} ... \end{bmatrix}`.
        
        # Since this article is about math, `\\` -> `\\\\` is almost universally correct for line breaks in KaTeX for Hugo.
        # Let's replace ` \\` with ` \\\\` or `\\` with `\\\\`.
        
        # Replace ` \\` at end of line:
        content = re.sub(r'\\\\\s*\n', r'\\\\\\\\\n', content)
        # Replace ` \\ ` inline (like in `\begin{bmatrix} c \\ d \end{bmatrix}`)
        content = re.sub(r'([^\\])\\\\([^\\])', r'\1\\\\\\\\\2', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Replacement complete.")
