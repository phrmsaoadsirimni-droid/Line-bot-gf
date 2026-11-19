from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# ใส่ Channel Access Token ของคุณตรงนี้
CHANNEL_ACCESS_TOKEN = "ใส่รหัส Token ของคุณตรงนี้"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
}


@app.route("/callback", methods=["POST"])
def callback():
  body = request.get_json(silent=True)
  try:
    events = body.get("events", [])
    for event in events:
      if "source" in event and "userId" in event["source"]:
        user_id = event["source"]["userId"]
        reply_token = event.get("replyToken")
        print(f"🎯 เจอ User ID แล้ว: {user_id}")

        # ส่งข้อความตอบกลับคนที่ทักมาทันที พร้อมบอก User ID ของเขา
        if reply_token:
          payload = {
              "replyToken": reply_token,
              "messages": [{
                  "type": "text",
                  "text": (
                      f"รหัส User ID ของคุณคือ:\n{user_id}"
                  ),
              }],
          }
          requests.post(
              "https://api.line.me/v2/bot/message/reply",
              headers=HEADERS,
              json=payload,
          )
  except Exception as e:
    print(f"Error: {e}")

  return jsonify({"status": "ok"})


if __name__ == "__main__":
  app.run(port=5000)
