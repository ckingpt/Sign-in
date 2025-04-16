from flask import Flask, request
from datetime import datetime
import threading
import schedule
import time

app = Flask(__name__)
sign_data = {}

def reset_sign_data():
    global sign_data
    sign_data = {}
    print("✅ 簽到資料已重置")

def run_schedule():
    schedule.every().day.at("00:00").do(reset_sign_data)
    while True:
        schedule.run_pending()
        time.sleep(1)

# 背景執行自動重置
threading.Thread(target=run_schedule, daemon=True).start()

@app.route("/簽到")
def sign():
    username = request.args.get("user")
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in sign_data:
        sign_data[today] = []

    if username not in sign_data[today]:
        sign_data[today].append(username)
        position = len(sign_data[today])
        return f"{username} 今日第 {position} 位簽到！"
    else:
        position = sign_data[today].index(username) + 1
        return f"{username} 你已簽到，是第 {position} 位！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
ㄋ