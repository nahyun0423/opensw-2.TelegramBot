import time
import datetime
import requests


def send_telegram_message(token, chat_id, message):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(base_url)
    return response.json()

def is_time_to_send_message():
    current_hour = datetime.datetime.now().hour
    return not (23 <= current_hour or current_hour < 3)

def main():
    token = "6940871687:AAF2prfaM75J4tW0-2Vk0c8PYbJz3ko2UgA"
    chat_id = "6532805693"

    while True:
        if is_time_to_send_message():
            message = "send message"  
            send_telegram_message(token, chat_id, message)
        
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()