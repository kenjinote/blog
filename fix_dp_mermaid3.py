
import glob
import re

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/動的計画法dpマスター/*.md"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # Regex replacements to catch translated text as well
        # Broken: A["dp[i-1"][w] (Skip item i)"]
        # Pattern: A\["dp\[i-1"\]\[w\](.*?)\]"\]
        
        def fix_node_quotes(match):
            # match.group(0) is the broken string, we just want to remove the inner quotes
            # A["dp[i-1"][w] (Skip item i)"] -> A["dp[i-1][w] (Skip item i)"]
            inner = match.group(1)
            inner = inner.replace("\"", "")
            return f"[\"{inner}\"]"
            
        # We can find all [\"...\"] in mermaid blocks and if they contain more than 2 quotes, remove the inner ones
        
        def process_mermaid(m):
            block = m.group(0)
            
            def repl(m2):
                inner = m2.group(1)
                # If there are any quotes inside the captured group (which shouldn`t happen in a normal non-greedy match,
                # BUT wait, the broken string is A["dp[i-1"][w] (Text)"]
                # A non-greedy match \["(.*?)"\] on A["dp[i-1"][w] (Text)"] will match:
                # ["dp[i-1"]
                # leaving [w] (Text)"] alone!
                return m2.group(0)
                
            # Better approach: The broken strings specifically have:
            # ["dp[i-1"][w] ... "]
            # Let`s just use regex to fix the specific broken patterns in DP article.
            
            # Fix graph 2
            block = re.sub(r"A\[\"dp\[i-1\"\]\[w\](.*?)\"\]", r"A[\"dp[i-1][w]\1\"]", block)
            block = re.sub(r"C\[\"Max: dp\[i\"\]\[w\]\"\]", r"C[\"Max: dp[i][w]\"]", block)
            block = re.sub(r"B\[\"dp\[i-1\"\]\[w - weight\[\"i\"\]\] \+ value\[\"i\"\](.*?)\"\]", r"B[\"dp[i-1][w - weight[i]] + value[i]\1\"]", block)
            
            # Fix graph 3
            block = re.sub(r"subgraph \"S\[\"i-1\"\] == T\[\"j-1\"\]\"", r"subgraph \"S[i-1] == T[j-1]\"", block)
            block = re.sub(r"subgraph \"S\[\"i-1\"\] != T\[\"j-1\"\]\"", r"subgraph \"S[i-1] != T[j-1]\"", block)
            block = re.sub(r"A1\[\"dp\[i-1\"\]\[j-1\]\"\]", r"A1[\"dp[i-1][j-1]\"]", block)
            block = re.sub(r"B1\[\"\+1 --> dp\[i\"\]\[j\]\"\]", r"B1[\"+1 --> dp[i][j]\"]", block)
            block = re.sub(r"A2\[\"dp\[i-1\"\]\[j\]\"\]", r"A2[\"dp[i-1][j]\"]", block)
            block = re.sub(r"C2\[\"Max --> dp\[i\"\]\[j\]\"\]", r"C2[\"Max --> dp[i][j]\"]", block)
            block = re.sub(r"B2\[\"dp\[i\"\]\[j-1\]\"\]", r"B2[\"dp[i][j-1]\"]", block)
            
            return block
            
        new_content = re.sub(r"```mermaid\n.*?\n```", process_mermaid, new_content, flags=re.DOTALL)

        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

