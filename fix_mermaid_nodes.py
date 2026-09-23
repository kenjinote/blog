
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # We need to find all mermaid blocks and process them line by line
        def process_mermaid(match):
            block = match.group(0)
            # Find ID[Text] where Text is not quoted and contains spaces or parentheses or other special chars
            # But let`s be safe: if it starts with [ and ends with ], and is not already quoted, we quote it.
            # E.g. A[Something] -> A["Something"]
            # Be careful not to replace link syntaxes or attribute syntaxes inside mermaid if any.
            # A common mermaid node is: NodeID[Node Text]
            # Regex to match NodeID[Node Text]
            # \b([A-Za-z0-9_]+)\[([^\"\]]+)\]
            
            # This regex matches NodeID[Text] where Text does not contain quotes or brackets
            def repl_node(m):
                node_id = m.group(1)
                text = m.group(2)
                # If text is already just alphanumeric, maybe we don`t need to quote, but quoting is safe.
                # Let`s only quote if there is a parenthesis, space, or non-alphanumeric (excluding CJK).
                # To keep it simple and safe for Mermaid: always quote the text inside [ ]
                return f"{node_id}[\"{text}\"]"
                
            new_block = re.sub(r"([A-Za-z0-9_]+)\[([^\"\]]+)\]", repl_node, block)
            
            # Also need to handle nodes like ID((Text)) -> ID(("Text"))
            def repl_circle(m):
                node_id = m.group(1)
                text = m.group(2)
                return f"{node_id}((\"{text}\"))"
            new_block = re.sub(r"([A-Za-z0-9_]+)\(\(([^\"\)]+)\)\)", repl_circle, new_block)
            
            # Also handle ID(Text) -> ID("Text")
            def repl_round(m):
                node_id = m.group(1)
                text = m.group(2)
                # Only if text contains spaces, parenthesis or other stuff, but for safe we can quote.
                # However, this might conflict with ID((Text)) if not careful.
                # Since we already did ID((Text)), the remaining ID(Text) can be replaced.
                return f"{node_id}(\"{text}\")"
            new_block = re.sub(r"([A-Za-z0-9_]+)\(([^\"\)]+)\)", repl_round, new_block)
            
            return new_block

        # Find mermaid blocks
        new_content = re.sub(r"```mermaid\n.*?\n```", process_mermaid, new_content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

