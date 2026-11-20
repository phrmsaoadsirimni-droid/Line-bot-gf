import os
import random
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = (
    "yXkQXeNfyQZDof2jsB53JG4z9obcpj6VljUh37gDgZ2FF7zFmPU3aX9tjpmI92ON0OJEJ4L4TtP9UI8PkdHVq8xZnz0DZRt5pUdYPHfZTcok0KLaZab8Pa1F1bG5FuVUQooygOAF81eTOObbdW5HJQdB04t89/1O/w1cDnyilFU="
)

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
}

REPLY_MESSAGES = [
    "คิดถึงนะ ทำอะไรอยู่เอ่ย?",
    "อย่าลืมกินข้าวให้ตรงเวลานะ เป็นห่วง",
    "สู้ๆ นะคนเก่ง เค้าเป็นกำลังใจให้เสมอ",
    "ดื่มน้ำเยอะๆ ด้วยนะ ตัวเอง",
    "รักนะ ❤️",
]


@app.route("/", methods=["GET"])
def home():
  return "LINE Bot is running!"


@app.route("/callback", methods=["POST"])
def callback():
  body = request.get_json(silent=True) or {}
  events = body.get("events", [])

  for event in events:
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
