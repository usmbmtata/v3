from flask import Flask, request, jsonify
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from app.utils.telegram_utils import send_telegram_message
from config import Config

app = Flask(__name__)
updater = Updater(Config.telegram_bot)

def start_command(update, context):
    chat_id = update.effective_chat.id
    welcome_message = "Welcome to Vedaalay!\n\nType /otp to get a one-time OTP for communication.\nType /help for available commands."
    context.bot.send_message(chat_id=chat_id, text=welcome_message)

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
    updater.stop()

def handle_text(update, context):
    # Process text messages
    chat_id = update.effective_chat.id
    text = update.message.text
    # Stop the bot
    updater.stop()

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    update = updater.update_queue.put(Update.de_json(json_data, updater.bot))  # type: ignore
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # Register command handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("otp", otp_command))
    dp.add_handler(CommandHandler("lastpayment", last_payment_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_payment_input))
    dp.add_handler(CommandHandler("stop", stop_command))
    dp.add_handler(MessageHandler(Filters.text, handle_text))

    # Start the Flask app
    app.run(debug=True)
