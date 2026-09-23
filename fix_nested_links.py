
import glob
import re

# Match patterns like:
# [prefix [inner_text](inner_url) suffix](outer_url)
# and replace them with:
# [prefix inner_text suffix](outer_url)
# We can use a regex that looks for an outer link containing an inner link.
# Outer link starts with [, contains a [, then ], then (, then ), then ends with ](url)
# This can be tricky to get perfect with regex, but since markdown links don`t naturally nest,
# we can use:
# \[(.*?)\[(.*?)\]\((.*?)\)(.*?)\]\((.*?)\)

pattern = re.compile(r"\[(.*?)\[(.*?)\]\((.*?)\)(.*?)\]\((.*?)\)")

count = 0
for file in glob.glob("c:/work/kenji.blog/content/post/**/*.md", recursive=True):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        # We need to run it multiple times in case there are multiple nested links inside one outer link
        while pattern.search(new_content):
            new_content = pattern.sub(r"[\1\2\4](\5)", new_content)
            
        if new_content != content:
            with open(file, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Fixed {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Fixed {count} files.")

