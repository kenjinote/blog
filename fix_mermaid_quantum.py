import os
import glob
import re

post_dir = "C:/work/kenji.blog/content/post/quantum-computer-ultimate-guide"
files = glob.glob(f"{post_dir}/*.md")

fixed_count = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to fix the lines in the mermaid graph.
    # Look for the broken lines: Obs -->|"..."| State1["..."]
    # The broken part is often like: -->|"Probability $p("a_1") = \langle \psi"| P_1 | \psi \rangle$ | State1
    
    new_content = content
    
    # Fix the broken quote inside the link text, and the pipe collision
    # Just replace the specific math parts with safe ASCII approximations or remove the broken quotes.
    
    # Example broken line: Obs -->|"確率 $p("a_1") = \langle \psi"| P_1 | \psi \rangle$ | State1["収縮状態 1: $| a_1 \rangle$"]:::state
    
    # The safest way is to regex match the Obs --> lines
    # Pattern: Obs -->\|"(.*?)"\| (State\d+|StateN)\["(.*?)"\]:::state
    # Wait, the current text is:
    # Obs -->|"確率 $p("a_1") = \langle \psi"| P_1 | \psi \rangle$ | State1["収縮状態 1: $| a_1 \rangle$"]:::state
    # Actually, the pipe | is interpreted as the end of the link text `| State1` which breaks everything.
    
    # Let's replace the entire Obs --> ... lines with a clean syntax:
    # Obs -- "text" --> State
    
    lines = new_content.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        if 'Obs -->|' in line and ('State1' in line or 'State2' in line or 'StateN' in line):
            # Try to extract the state name and the text inside the state node
            state_match = re.search(r'(State(?:1|2|N))\["(.*?)"\]', line)
            if state_match:
                state_id = state_match.group(1)
                state_text = state_match.group(2)
                
                # Replace the line with a safe version
                if 'State1' in line:
                    lines[i] = f'      Obs -- "p(a_1) = <ψ|P_1|ψ>" --> {state_id}["{state_text}"]:::state'
                    modified = True
                elif 'State2' in line:
                    lines[i] = f'      Obs -- "p(a_2) = <ψ|P_2|ψ>" --> {state_id}["{state_text}"]:::state'
                    modified = True
                elif 'StateN' in line:
                    lines[i] = f'      Obs -- "..." --> {state_id}["{state_text}"]:::state'
                    modified = True

    if modified:
        new_content = '\n'.join(lines)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed_count += 1

print(f"Fixed {fixed_count} files.")
