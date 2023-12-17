from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from app.utils.telegram_utils import send_telegram_message
from config import Config

app = Flask(__name__)

bot = Updater(Config.telegram_bot)
dispatcher = bot.dispatcher


def start_command(update, context):
    chat_id = update.effective_chat.id
    welcome_message = "Welcome to Vedaalay!\n\nType /otp to get a one-time OTP for communication.\nType /help for available commands."
    send_telegram_message(chat_id, welcome_message)

def otp_command(update, context):
    chat_id = update.effective_chat.id
    # Generate and send OTP using your logic
    otp = chat_id
    message = f"Your OTP to set Telegram as a communication mode is: {otp}"
    send_telegram_message(chat_id, message)

def last_payment_command(update, context):
    chat_id = update.effective_chat.id
    # Prompt user for input
    send_telegram_message(chat_id, "Please provide your Registration Number or your Registered Contact Number:")

def handle_payment_input(update, context):
    chat_id = update.effective_chat.id
    user_input = update.message.text
    # Implement logic to fetch and send last payment details based on user input
    # ...

def stop_command(update, context):
    chat_id = update.effective_chat.id
    send_telegram_message(chat_id, "Goodbye!")

def handle_text(update, context):
    # Process text messages
    chat_id = update.effective_chat.id
    text = update.message.text
    # Stop the bot
    Updater.stop_polling()

if __name__ == '__main__':
    bot.start_polling()
    app.run(debug=True)
