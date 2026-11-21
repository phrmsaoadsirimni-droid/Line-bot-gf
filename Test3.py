import os
import random
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# --- ตั้งค่า Channel Access Token ล่าสุด ---
CHANNEL_ACCESS_TOKEN = (
    "q1+XOEprLJXg1Mvg0Oa7vYWvO6EjfdXnDw8pKiJt81KKeZiCCEli5FwM7Nz4vdPV0OJEJ4L4TtP9UI8PkdHVq8xZnz0DZRt5pUdYPHfZTcr1mgPI9604LPfbsII2TuBkIPQHs2CGfZHHE0DDnRmk6QdB04t89/1O/w1cDnyilFU="
)

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
}

# รายการข้อความสำหรับสุ่มตอบกลับเมื่อมีคนทักเข้ามา
REPLY_MESSAGES = [
    "คิดถึงนะ ทำอะไรอยู่เอ่ย?",
    "อย่าลืมกินข้าวให้ตรงเวลานะ เป็นห่วง",
    "สู้ๆ นะคนเก่ง เค้าเป็นกำลังใจให้เสมอ",
    "ดื่มน้ำเยอะๆ ด้วยนะ ตัวเอง",
    "รักนะ ❤️",
]


@app.route("/", methods=["GET"])
def home():
  return "LINE Bot (Reply Only) is running!"


@app.route("/callback", methods=["POST"])
def callback():
  body = request.get_json(silent=True) or {}
  events = body.get("events", [])

  for event in events:
    # ทำงานเฉพาะเมื่อมีคนส่งข้อความ (message) เข้ามาเท่านั้น
    if event.get("type") == "message":
      reply_token = event.get("replyToken")
      user_id = event.get("source", {}).get("userId")
      incoming_text = event.get("message", {}).get("text", "")

      print(f"รับข้อความจาก {user_id}: {incoming_text}")

      if reply_token:
        reply_text = random.choice(REPLY_MESSAGES)
        payload = {
            "replyToken": reply_token,
            "messages": [{"type": "text", "text": reply_text}],
        }
        res = requests.post(
            "https://api.line.me/v2/bot/message/reply",
            headers=HEADERS,
            json=payload,
        )
        print(f"สถานะตอบกลับ: {res.status_code} {res.text}")

  return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
