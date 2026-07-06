import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=pax-gold,tether&vs_currencies=usd"

print("--- 測試直連 CoinGecko ---")
try:
    response = requests.get(url)
    print(f"狀態代碼: {response.status_code}")
    print(f"回應內容: {response.text}")
except Exception as e:
    print(f"連線失敗: {e}")