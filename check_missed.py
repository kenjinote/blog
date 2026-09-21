import json
t = open('translate2.py', encoding='utf-8').read()
u = json.load(open('unique_sorted.json', encoding='utf-8'))
missed = []
for x in u:
    if x == '': continue
    # Try finding the key in the file content roughly
    # Actually, let's just parse the translations dict from translate2.py
    import importlib.util
    spec = importlib.util.spec_from_file_location("translate2", "translate2.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    if x not in foo.translations:
        missed.append(x)

json.dump(missed, open('missed.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
