import json
import os
import re

agents = {
    "ar": "5cb10365-c9ef-409e-a6b9-459b09a7a78d",
    "de": "b93fd4d7-a831-4202-aa84-bce1e2e008fa",
    "es": "73715664-a4f8-4047-92b2-8e65c0038cd4",
    "hi": "6932ec2d-b3ca-4e45-a28e-6605cc97940a",
    "ko": "dc687244-5534-47d9-8911-ed6799ddda6f",
    "ru": "88bd8fe9-9add-4391-a054-d381b9bfbfcf",
    "zh-tw": "b5a52628-7e25-4abb-8e45-ff0d465a4980"
}

base_dir = r"C:\Users\kenjinote\.gemini\antigravity\brain"
dest_dir = r"C:\work\kenji.blog\content\post\random-matrix-theory"

for lang, cid in agents.items():
    log_path = os.path.join(base_dir, cid, ".system_generated", "logs", "transcript_full.jsonl")
    if not os.path.exists(log_path):
        log_path = os.path.join(base_dir, cid, ".system_generated", "logs", "transcript.jsonl")
    
    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    content = ""
    for line in reversed(lines):
        try:
            data = json.loads(line)
            if "tool_calls" in data:
                for tc in data["tool_calls"]:
                    func = tc.get("function", {})
                    if func.get("name") == "default_api:send_message":
                        args = func.get("arguments", "{}")
                        if isinstance(args, str):
                            args = json.loads(args)
                        msg = args.get("Message", "")
                        match = re.search(r"```(?:markdown)?\n(.*?)```", msg, re.DOTALL)
                        if match:
                            content = match.group(1).strip()
                        else:
                            content = msg.strip()
                        break
                if content: break
        except:
            pass
    
    if content:
        # ensure frontmatter --- exists
        if not content.startswith("---"):
            if "---" in content:
                content = "---" + content.split("---", 1)[1]
        dest_file = os.path.join(dest_dir, f"index.{lang}.md")
        with open(dest_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Wrote {dest_file}")
    else:
        print(f"Failed to find content for {lang}")