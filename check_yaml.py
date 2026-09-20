import yaml

with open(r"c:\work\kenji.blog\i18n\pt.yaml", "r", encoding="utf-8") as f:
    try:
        data = yaml.safe_load(f)
        print("Success, keys:", list(data.keys()))
    except Exception as e:
        print("Error:", e)
