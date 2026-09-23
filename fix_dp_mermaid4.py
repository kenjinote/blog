
import glob

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/動的計画法dpマスター/*.md"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # In python, replace [\" with ["
        # [\\\" means [\" in regex/literal, but let`s just use plain strings.
        new_content = new_content.replace("A[\\\"dp", "A[\"dp")
        new_content = new_content.replace("\\\"] --> C", "\"] --> C")
        new_content = new_content.replace("C[\\\"Max", "C[\"Max")
        new_content = new_content.replace("w]\\\"]", "w]\"]")
        new_content = new_content.replace("B[\\\"dp", "B[\"dp")
        
        new_content = new_content.replace("subgraph \\\"S", "subgraph \"S")
        new_content = new_content.replace("1]\\\"", "1]\"")
        new_content = new_content.replace("A1[\\\"dp", "A1[\"dp")
        new_content = new_content.replace("1]\\\"]", "1]\"]")
        new_content = new_content.replace("B1[\\\"+1", "B1[\"+1")
        new_content = new_content.replace("j]\\\"]", "j]\"]")
        new_content = new_content.replace("A2[\\\"dp", "A2[\"dp")
        new_content = new_content.replace("C2[\\\"Max", "C2[\"Max")
        new_content = new_content.replace("B2[\\\"dp", "B2[\"dp")
        
        # Or even simpler, globally replace [\" with [" inside mermaid blocks
        import re
        def repl(m):
            block = m.group(0)
            block = block.replace("[\\\"", "[\"")
            block = block.replace("\\\"]", "\"]")
            block = block.replace("subgraph \\\"", "subgraph \"")
            block = block.replace("]\\\"", "]\"")
            return block
            
        new_content = re.sub(r"```mermaid\n.*?\n```", repl, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

