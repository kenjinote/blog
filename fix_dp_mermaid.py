
import re

file_path = "c:/work/kenji.blog/content/post/動的計画法dpマスター/index.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Graph 2
bad_graph_2 = """```mermaid
  graph TD
      A["dp[i-1"][w] (Skip item i)"] --> C["Max: dp[i"][w]"]
      B["dp[i-1"][w - weight["i"]] + value["i"] (Take item i)"] --> C
  ```"""
  
good_graph_2 = """```mermaid
  graph TD
      A["dp[i-1][w] (Skip item i)"] --> C["Max: dp[i][w]"]
      B["dp[i-1][w - weight[i]] + value[i] (Take item i)"] --> C
  ```"""
  
# Graph 3
bad_graph_3 = """```mermaid
  graph TD
      subgraph "S["i-1"] == T["j-1"]"
          A1["dp[i-1"][j-1]"] --> B1["+1 --> dp[i"][j]"]
      end
      subgraph "S["i-1"] != T["j-1"]"
          A2["dp[i-1"][j]"] --> C2["Max --> dp[i"][j]"]
          B2["dp[i"][j-1]"] --> C2
      end
  ```"""
  
good_graph_3 = """```mermaid
  graph TD
      subgraph "S[i-1] == T[j-1]"
          A1["dp[i-1][j-1]"] --> B1["+1 --> dp[i][j]"]
      end
      subgraph "S[i-1] != T[j-1]"
          A2["dp[i-1][j]"] --> C2["Max --> dp[i][j]"]
          B2["dp[i][j-1]"] --> C2
      end
  ```"""

new_content = content.replace(bad_graph_2, good_graph_2).replace(bad_graph_3, good_graph_3)

if new_content != content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed dp-algorithm-master-guide")
else:
    print("Not found or already fixed")

