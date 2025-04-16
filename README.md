# Twitch Nightbot 自動簽到系統

這是一個用 Flask 打造的 Twitch 簽到系統，支援 Nightbot 指令、記錄簽到順序、每天自動清空簽到資料。

## 🚀 功能
- 使用 `!sign` 指令簽到
- 回傳使用者今日第幾位簽到
- 每天 00:00 自動清空簽到紀錄

## 🛠️ 部署方式（Render）
1. 前往 [https://render.com](https://render.com)
2. 建立新的 Web Service
3. 連接此 Repo
4. 選擇 Python 並設置：
   - Start command: `python main.py`
   - Build command: `pip install -r requirements.txt`

## 🎮 Nightbot 指令設定

在 [Nightbot 指令管理頁](https://nightbot.tv/commands/custom) 新增：

| 指令 | 回應內容 |
|------|---------|
| `!sign` | `$(urlfetch https://你的網址.onrender.com/sign?user=$(user))` |

## 📌 注意
- 這個系統使用記憶體儲存，重啟會清空（可改進為 SQLite 或 Redis）
- 請確保部署平台有 24 小時運作（Render 免費版會睡眠）
