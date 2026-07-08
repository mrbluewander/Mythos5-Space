import requests
from bs4 import BeautifulSoup

class AgentHands:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

    # 手腳：抓取網頁原始內容
    def fetch_web_content(self, url):
        response = self.session.get(url)
        return response.text

    # 手腳：抓取 API 數據
    def fetch_json_data(self, api_url):
        response = self.session.get(api_url)
        return response.json()

    # 手腳：發送數據到指定站點
    def send_to_hub(self, webhook_url, data):
        return self.session.post(webhook_url, json=data)

if __name__ == "__main__":
    print("小龍蝦手腳模組已就緒。")
