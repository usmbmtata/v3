
from telegram import Bot
from telegram.ext import Updater
from config import Config

bot = Bot(token='telegram_bot')

def send_custom_message(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

def run_bot():
    updater = Updater(token='TELEGRAM_BOT', use_context=True)
    dispatcher = updater.dispatcher
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_bot()