import requests
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

# пример: Мекка
CITY = "Mecca"
COUNTRY = "Saudi Arabia"

url = f"https://api.aladhan.com/v1/timingsByCity?city={CITY}&country={COUNTRY}&method=2"
data = requests.get(url).json()

timings = data["data"]["timings"]

text = (
    f"🕌 Время намаза ({CITY})\n\n"
    f"Фаджр: {timings['Fajr']}\n"
    f"Зухр: {timings['Dhuhr']}\n"
    f"Аср: {timings['Asr']}\n"
    f"Магриб: {timings['Maghrib']}\n"
    f"Иша: {timings['Isha']}"
)

bot.send_message(CHAT_ID, text)
