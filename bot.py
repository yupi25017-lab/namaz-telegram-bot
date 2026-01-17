import telebot

TOKEN = "8476939856:AAEWAlFmSCJNKz1OxIogQUVuW-TZBYaloYI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Ассаляму алейкум! Бот работает ✅")

bot.polling()
