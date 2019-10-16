from telegram.ext import CommandHandler, Updater

from src.settings import TELEGRAM_CHANNEL_TOKEN


def hello(update, context):
    del context
    update.message.reply_text("Hello {}".format(update.message.from_user.first_name))


if __name__ == "__main__":
    updater = Updater(TELEGRAM_CHANNEL_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("hello", hello))

    updater.start_polling()
    updater.idle()
