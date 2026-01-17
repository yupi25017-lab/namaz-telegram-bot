import os
import requests
import telebot
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

places = [
    ("Mecca", "Saudi Arabia", "🇸🇦 Мекка"),
    ("Istanbul", "Turkey", "🇹🇷 Стамбул"),
    ("Tashkent", "Uzbekistan", "🇺🇿 Ташкент"),
    ("Moscow", "Russia", "🇷🇺 Москва"),
    ("Baku", "Azerbaijan", "🇦🇿 Баку"),
    ("Almaty", "Kazakhstan", "🇰🇿 Алматы"),
    ("Cairo", "Egypt", "🇪🇬 Каир"),
    ("Amman", "Jordan", "🇯🇴 Амман"),
    ("Rabat", "Morocco", "🇲🇦 Рабат"),
    ("Jakarta", "Indonesia", "🇮🇩 Джакарта"),
]

def get_prayer_times(city, country):
    url = (
        "https://api.aladhan.com/v1/timingsByCity"
        f"?city={city}&country={country}&method=2"
    )
    response = requests.get(url)
    return response.json()["data"]["timings"]

def main():
    today = datetime.now().strftime("%d.%m.%Y")
    message = f"🕌 Время намаза\n📅 {today}\n\n"

    for city_api, country_api, title in places:
        times = get_prayer_times(city_api, country_api)

        message += (
            f"{title}\n"
            f"Фаджр: {times['Fajr']}\n"
            f"Зухр: {times['Dhuhr']}\n"
            f"Аср: {times['Asr']}\n"
            f"Магриб: {times['Maghrib']}\n"
            f"Иша: {times['Isha']}\n\n"
        )

    bot.send_message(CHAT_ID, message)

if __name__ == "__main__":
    main()
