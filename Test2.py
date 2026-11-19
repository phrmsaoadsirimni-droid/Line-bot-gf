from datetime import datetime
import random
import time
import requests
import schedule

# --- ตั้งค่า Token และ User ID ของแฟน ---
CHANNEL_ACCESS_TOKEN = (
    "yXkQXeNfyQZDof2jsB53JG4z9obcpj6VljUh37gDgZ2FF7zFmPU3aX9tjpmI92ON0OJEJ4L4TtP9UI8PkdHVq8xZnz0DZRt5pUdYPHfZTcok0KLaZab8Pa1F1bG5FuVUQooygOAF81eTOObbdW5HJQdB04t89/1O/w1cDnyilFU="
)
GIRLFRIEND_USER_ID = "Uaaefed0b9106cc564deb5a881d317bcf"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
}

# --- รายการข้อความสำหรับสุ่มส่งหาแฟน ---
MESSAGES = [
    "คิดถึงนะ ทำอะไรอยู่เอ่ย?",
    "อย่าลืมกินข้าวให้ตรงเวลานะ เป็นห่วง",
    "สู้ๆ นะคนเก่ง เค้าเป็นกำลังใจให้เสมอ",
    "ดื่มน้ำเยอะๆ ด้วยนะ ตัวเอง",
    "รักนะ ❤️",
]


def send_message_to_gf():
  # สุ่มเลือกข้อความจากรายการ
  text_to_send = random.choice(MESSAGES)

  payload = {
      "to": GIRLFRIEND_USER_ID,
      "messages": [{"type": "text", "text": text_to_send}],
  }

  response = requests.post(
      "https://api.line.me/v2/bot/message/push", headers=HEADERS, json=payload
  )

  now = datetime.now().strftime("%H:%M:%S")
  if response.status_code == 200:
    print(f"[{now}] ส่งข้อความหาแฟนสำเร็จ: '{text_to_send}'")
  else:
    print(
        f"[{now}] ส่งไม่สำเร็จ (Status: {response.status_code}):"
        f" {response.text}"
    )


# --- ตั้งเวลาส่งข้อความ (เช่น ส่งทุกๆ 10 วินาที หรือปรับตามต้องการ) ---
schedule.every(10).seconds.do(send_message_to_gf)

print("บอทเริ่มส่งข้อความหาแฟนแบบอัตโนมัติแล้ว...")

# ลูปเพื่อให้โปรแกรมรันทำงานเบื้องหลังตลอดเวลา
while True:
  schedule.run_pending()
  time.sleep(1)
