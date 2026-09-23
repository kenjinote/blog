
import glob

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/functional-programming-concepts-pure-functions-monads/*.md"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        target = "E ::= x \\mid \\lambda x. E \\mid E_1 E_2"
        replacement = "$$\nE ::= x \\mid \\lambda x. E \\mid E_1 E_2\n$$"
        
        if target in new_content and "$$\nE ::=" not in new_content:
            new_content = new_content.replace(target, replacement)
            
        broken_jp = "ここで、$ は変数、$\\lambda x. E$ は抽象化（関数定義）、 E_2$ は関数適用を表します。"
        fixed_jp = "ここで、$x$ は変数、$\\lambda x. E$ は抽象化（関数定義）、$E_1 E_2$ は関数適用を表します。"
        new_content = new_content.replace(broken_jp, fixed_jp)
        
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

