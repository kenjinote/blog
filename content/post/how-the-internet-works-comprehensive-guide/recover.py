import json, os

transcripts = [
    'C:/Users/kenjinote/.gemini/antigravity/brain/bdef3e0a-19e8-4c7f-be6e-a1e0da71d21c/.system_generated/logs/transcript_full.jsonl',
    'C:/Users/kenjinote/.gemini/antigravity/brain/2426a945-a30e-42de-a810-5ce321a925a5/.system_generated/logs/transcript_full.jsonl',
    'C:/Users/kenjinote/.gemini/antigravity/brain/95c7848c-ed3c-458e-ac27-b39a5fb47bbc/.system_generated/logs/transcript_full.jsonl'
]
out_files = [
    'C:/work/kenji.blog/content/post/how-the-internet-works-comprehensive-guide/chunk_3_recovered.md',
    'C:/work/kenji.blog/content/post/how-the-internet-works-comprehensive-guide/chunk_7_recovered.md',
    'C:/work/kenji.blog/content/post/how-the-internet-works-comprehensive-guide/chunk_8_recovered.md'
]
for t, out in zip(transcripts, out_files):
    if not os.path.exists(t):
        continue
    content = None
    with open(t, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            for tc in data.get('tool_calls', []):
                if tc.get('name') == 'write_to_file':
                    content = tc.get('args', {}).get('CodeContent', '')
    if content:
        if content.startswith('"') and content.endswith('"'):
            content = content[1:-1].replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Recovered ' + out)
