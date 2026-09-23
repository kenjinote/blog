
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        def repl_mermaid(m):
            block = m.group(0)
            
            # Remove nested quotes like P("Spam") -> P(Spam)
            # This handles cases where ID("...") was incorrectly applied inside another node text
            # like Class{"P("Spam") > 0.9?"}
            # We look for something like \(\"(.*?)\"\) -> \(\1\)
            # But only if it`s inside a larger string definition like {"..."} or ["..."]
            
            # Since mermaid node texts should generally just use the outer quotes, 
            # we can safely remove any (\" and \") pairs inside the block EXCEPT for the outermost ones.
            # Actually, doing it generally for \(\"(.*?)\"\) is safe enough, because standard round nodes
            # are ID("Text"), which matches \w+\(\"(.*?)\"\). We want to keep those.
            # But the broken ones are inside quotes themselves!
            # Example: {"P("Spam")"} -> {"P(Spam)"}
            # Let`s just directly target the known breakages:
            # P("Spam") -> P(Spam)
            # f("xn") -> f(xn)
            # And any generic \(\" and \"\) inside { or [
            
            # Wait, ID("Text") is a valid round node in Mermaid.
            # But Class{"P("Spam")"} is invalid because of the inner quotes.
            # We can find {"...(\"...\"...)..."} and remove the inner quotes.
            
            # Let`s do simple string replacements for the known ones:
            block = block.replace("P(\"Spam\")", "P(Spam)")
            block = block.replace("f(\"xn\")", "f(xn)")
            
            # Let`s also check if there are any other {"...\"..."} or ["...\"..."] remaining.
            # We can use regex to find {"..."} and then strip internal quotes
            def fix_inner_braces(m_brace):
                # match is like {" something "}
                inner = m_brace.group(1)
                fixed_inner = inner.replace("\"", "")
                return f"{{\"{fixed_inner}\"}}"
            block = re.sub(r"\{\"(.*?)\"\}", fix_inner_braces, block)
            
            return block
            
        new_content = re.sub(r"```mermaid\n.*?\n```", repl_mermaid, new_content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

