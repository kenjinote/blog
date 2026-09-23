
import re

file_path = "c:/work/kenji.blog/content/post/動的計画法dpマスター/index.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = content
new_content = new_content.replace("""A["dp[i-1"][w] (Skip item i)"] --> C["Max: dp[i"][w]"]""", """A["dp[i-1][w] (Skip item i)"] --> C["Max: dp[i][w]"]""")
new_content = new_content.replace("""B["dp[i-1"][w - weight["i"]] + value["i"] (Take item i)"] --> C""", """B["dp[i-1][w - weight[i]] + value[i] (Take item i)"] --> C""")

new_content = new_content.replace("""subgraph "S["i-1"] == T["j-1"]\"""", """subgraph "S[i-1] == T[j-1]\"""")
new_content = new_content.replace("""subgraph "S["i-1"] != T["j-1"]\"""", """subgraph "S[i-1] != T[j-1]\"""")

new_content = new_content.replace("""A1["dp[i-1"][j-1]"] --> B1["+1 --> dp[i"][j]"]""", """A1["dp[i-1][j-1]"] --> B1["+1 --> dp[i][j]"]""")
new_content = new_content.replace("""A2["dp[i-1"][j]"] --> C2["Max --> dp[i"][j]"]""", """A2["dp[i-1][j]"] --> C2["Max --> dp[i][j]"]""")
new_content = new_content.replace("""B2["dp[i"][j-1]"] --> C2""", """B2["dp[i][j-1]"] --> C2""")

if new_content != content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed dp-algorithm-master-guide")
else:
    print("Not found or already fixed")

