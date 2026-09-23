
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We are looking for lines with exactly `mermaid or ``mermaid followed by a diagram, ending with ` or ``
        # It is safer to specifically target the exact pattern observed:
        # ^`mermaid$
        # ...
        # ^`$
        
        # We can do this with a regular expression
        # (?m) is multiline. Match a line starting with 1 or 2 backticks and "mermaid", ending there.
        # Then lazily match lines until a line starting with 1 or 2 backticks.
        
        pattern = re.compile(r"^(?P<start>`{1,2})mermaid\s*$(?P<body>.*?)^\s*(?P<end>`{1,2})\s*$", re.MULTILINE | re.DOTALL)
        
        def repl(match):
            return "```mermaid\n" + match.group("body").strip("\r\n") + "\n```"
            
        new_content, subs = pattern.subn(repl, content)
        
        if subs > 0:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

