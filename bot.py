import requests
import telebot
import os
from datetime import datetime, timedelta

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
CITY = os.getenv("CITY")
COUNTRY = os.getenv("COUNTRY")

bot = telebot.TeleBot(BOT_TOKEN)

url = f"https://api.aladhan.com/v1/timingsByCity?city={CITY}&country={COUNTRY}&method=2"
data = requests.get(url).json()
timings = data["data"]["timings"]

now = datetime.now()

namaz_times = {
    "Фаджр 🕊": timings["Fajr"],
    "Зухр ☀️": timings["Dhuhr"],
    "Аср 🌤": timings["Asr"],
    "Магриб 🌙": timings["Maghrib"],
    "Иша 🌌": timings["Isha"]
}

text = f"🕌 *Время намаза*\n📍 {CITY}, {COUNTRY}\n\n"

for name, time_str in namaz_times.items():
    text += f"{name}: `{time_str}`\n"

text += "\n🤲 Пусть Аллах примет ваши молитвы"

bot.send_message(CHAT_ID, text, parse_mode="Markdown")
