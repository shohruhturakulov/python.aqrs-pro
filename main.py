from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "1646068953:AAHs7vj-ifDN4Rgu6o5qUMbrp4-t3sekCAo"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom alaykum, Shohruh ning Kiril-Lotin botiga xush kelibsiz!"
    javob += "\nMatn kiritng: "
    bot.reply_to(message, javob)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "How can i help you?")

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()
