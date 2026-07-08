import os
import re
from groq import Groq

raw_key = os.getenv("GROQ_API_KEY", "")
clean_key = re.sub(r'[^\x00-\x7F]+', '', raw_key).strip()

if clean_key:
    print(f"✅ 金鑰已淨化，長度: {len(clean_key)}")
    try:
        client = Groq(api_key=clean_key)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "Hello"}],
            model="llama3-8b-8192",
        )
        print("🚀 連線成功！")
    except Exception as e:
        print(f"❌ 初始化失敗: {e}")
else:
    print("❌ 錯誤：找不到金鑰，請確保環境變數已設定。")
