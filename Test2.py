import random
import time
import requests

# --- ตั้งค่า Token และ User ID ล่าสุด ---
CHANNEL_ACCESS_TOKEN = (
    "q1+XOEprLJXg1Mvg0Oa7vYWvO6EjfdXnDw8pKiJt81KKeZiCCEli5FwM7Nz4vdPV0OJEJ4L4TtP9UI8PkdHVq8xZnz0DZRt5pUdYPHfZTcr1mgPI9604LPfbsII2TuBkIPQHs2CGfZHHE0DDnRmk6QdB04t89/1O/w1cDnyilFU="
)
GIRLFRIEND_USER_ID = "U872787524f2f1b14bdccf3d28d39c9d6"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
}

MESSAGES = [
    "คิดถึงนะ ทำอะไรอยู่เอ่ย?",
    "อย่าลืมกินข้าวให้ตรงเวลานะ เป็นห่วง",
    "สู้ๆ นะคนเก่ง เค้าเป็นกำลังใจให้เสมอ",
    "ดื่มน้ำเยอะๆ ด้วยนะ ตัวเอง",
    "รักนะ ❤️",
]


def send_message_to_gf():
  text_to_send = random.choice(MESSAGES)
  payload = {
      "to": GIRLFRIEND_USER_ID,
      "messages": [{"type": "text", "text": text_to_send}],
  }
  response = requests.post(
      "https://api.line.me/v2/bot/message/push",
      headers=HEADERS,
      json=payload,
  )
  now = time.strftime("%H:%M:%S")
  if response.status_code == 200:
    print(f"[{now}] ส่งสำเร็จ: {text_to_send}")
  else:
    print(f"[{now}] ส่งไม่สำเร็จ (Status: {response.status_code}): {response.text}")


print("บอทเริ่มส่งข้อความหาแฟนแบบอัตโนมัติแล้ว...")
while True:
  send_message_to_gf()
  time.sleep(10)
