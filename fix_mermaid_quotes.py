
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        def process_mermaid(match):
            block = match.group(0)
            # Find any [\"...\"] that contains another \" inside the inner ...
            # Actually, because Python regex might be tricky, let`s just look for ID[\"inner\"]
            # where inner has inner quotes, and remove the inner quotes.
            # Example: A[\"fib(\"5\")\"] -> A[\"fib(5)\"]
            # We can just match the pattern [\" (anything) \"]
            
            def repl_node(m):
                full = m.group(0)
                inner = m.group(1)
                if "\"" in inner:
                    # Remove all quotes from the inner text to fix it
                    fixed_inner = inner.replace("\"", "")
                    return f"[\"{fixed_inner}\"]"
                return full
                
            # Use a non-greedy match for the content between [\" and \"]
            return re.sub(r"\[\"(.*?)\"\]", repl_node, block)

        new_content = re.sub(r"```mermaid\n.*?\n```", process_mermaid, new_content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

