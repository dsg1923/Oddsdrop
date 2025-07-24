
import os
import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Botul funcționează! ✅")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
