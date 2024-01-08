from telegram import Bot
from telegram.error import TelegramError
from flask import current_app
from app.config import Config

def send_telegram_message(chat_id, text):
    try:
        bot_token = Config.telegram_bot
        bot = Bot(token=bot_token)
        bot.send_message(chat_id=chat_id, text=text)
        return True
    except TelegramError as e:
        current_app.logger.error(f"Telegram error: {str(e)}")
        return False
