import os
import csv
import requests
import sys
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

sys.stdout.reconfigure(encoding='utf-8')

# Google Cloudのサービスアカウントキー(JSON)のパス
SERVICE_ACCOUNT_FILE = 'service_account.json'
CSV_FILE = '表.csv'

URLS_TO_INDEX = []
remaining_rows = []
header = None

try:
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None) # skip header
        
        for row in reader:
            if not row or not row[0].startswith('http'):
                continue
            if len(URLS_TO_INDEX) < 200:
                URLS_TO_INDEX.append(row[0])
            else:
                remaining_rows.append(row)
except Exception as e:
    print(f"CSVファイルの読み込みに失敗しました: {e}")
    sys.exit(1)

if not URLS_TO_INDEX:
    print("インデックス登録するURLがありません（完了しました）。")
    sys.exit(0)

def request_indexing(url, session):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    body = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = session.post(endpoint, json=body)
    if response.status_code == 200:
        print(f"[OK] {url}")
        return True
    else:
        print(f"[ERROR] ({response.status_code}): {response.text}")
        return False

def main():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"エラー: {SERVICE_ACCOUNT_FILE} が見つかりません。")
        print("Google Cloud ConsoleからサービスアカウントのJSONキーをダウンロードし、配置してください。")
        return

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/indexing"]
    )
    session = AuthorizedSession(credentials)

    print(f"{len(URLS_TO_INDEX)}件のURLのインデックス登録をリクエストします...")
    for url in URLS_TO_INDEX:
        success = request_indexing(url, session)
        if not success:
            remaining_rows.insert(0, [url]) # Failed URLs go back to the top
            break # Stop processing if we hit quota

    # 処理後に残りのURLをCSVに書き戻す
    if remaining_rows:
        try:
            with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                if header:
                    writer.writerow(header)
                writer.writerows(remaining_rows)
            print(f"残りの {len(remaining_rows)} 件を {CSV_FILE} に書き戻しました。")
        except Exception as e:
            print(f"CSVへの書き戻しに失敗しました: {e}")
    else:
        print("すべてのURLの処理が完了しました！")

if __name__ == "__main__":
    main()
