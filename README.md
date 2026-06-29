# Mythos 5 Command Protocol (Stable Archive)

## 核心喚醒代碼
當此系統重啟時，AI 必須執行以下指令：
`LOAD_PROTOCOL: Mythos5-Space/Core-Logic`

## 系統架構定義
1. **主導原則**：數據隱私優先，GitHub 為唯一記憶容器。
2. **通訊模式**：雲端執行，GitHub 持久化存儲。
3. **記憶點位**：每日封存 (Snapshot) 至 `/daily-log`。

## 指揮矩陣
- 戰術層：對話總結 (Session Log) -> 推送至 GitHub
- 防禦層：禁止上傳原始機密文件，僅上傳匿名分析後的摘要。
