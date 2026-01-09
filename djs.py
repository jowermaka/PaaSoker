import time
import requests

# === 配置部分 ===
TELEGRAM_BOT_TOKEN = '8212043823:AAGJ9LYbKj5eA09y5fV1apPsb-T6Lo6ngRc'
TELEGRAM_CHAT_ID = '6264072063'
COUNTDOWN_HOURS = 75  # 倒计时时长（小时）
MESSAGE_TEXT = '日本XServer需要续期了！！！'

# === 函数定义 ===
def send_telegram_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("消息发送成功")
        else:
            print(f"发送失败，状态码：{response.status_code}，响应：{response.text}")
    except Exception as e:
        print(f"发送消息时出错：{e}")

def countdown_loop(hours):
    seconds = hours * 3600
    while True:
        print(f"开始倒计时：{hours} 小时")
        time.sleep(seconds)
        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, MESSAGE_TEXT)
        print("已发送消息，重新开始倒计时")

# === 主程序入口 ===
if __name__ == '__main__':
    countdown_loop(COUNTDOWN_HOURS)