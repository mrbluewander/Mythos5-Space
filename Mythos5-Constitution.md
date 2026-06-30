# Mythos 5：指揮官數位自動化架構憲法

## 1. 核心原則
- 數據高於界面：永遠優先調用 API，棄用 UI 滑鼠操作。
- 邏輯解耦：模型（大腦）與執行器（n8n/Docker）分離，確保隨時可更換。
- 數據歸檔：任何即時獲取之資訊，需同步存入私有向量資料庫。

## 2. 執行流程 (戰術循環)
- 觸發 (Trigger)：GitHub/Webhook 監控。
- 推理 (Reasoning)：Gemini API 調度 (根據任務選擇 Fast/Deep)。
- 執行 (Execution)：n8n 節點鏈結 (HTTP Request/Browser Automation)。
- 反饋 (Feedback Loop)：除錯後將結果回寫至 Git。

## 3. 仿真化防護
- 對外請求需具備 Header 偽裝與代理 IP (Proxy) 路由。
- 避免頻繁高頻存取，執行時間差 (Time-shift) 策略。
