import datetime
import time
from telegram import Bot

# 텔레그램 봇 토큰
TELEGRAM_BOT_TOKEN = '6940871687:AAF2prfaM75J4tW0-2Vk0c8PYbJz3ko2UgA'

# 채널 아이디 (개설 채널의 경우 @channelname 형식)
CHANNEL_ID = '@opensource_test_bot'

def send_message(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    channel_id = CHANNEL_ID

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")

        # 11시부터 6시까지 메시지를 보내지 않음
        if "23:00" <= current_time <= "06:00":
            time.sleep(60 * 30)  # 30분 동안 대기
            continue

        # 30분마다 메시지 전송
        if current_time.endswith(":00") or current_time.endswith(":30"):
            message_text = "안녕하세요! 현재 시각은 {}입니다.".format(current_time)
            send_message(bot, channel_id, message_text)

        time.sleep(60)  # 1분 동안 대기

if __name__ == "__main__":
    main()