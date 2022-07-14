import logging

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    Filters,
)

import handlers, settings

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.

TOKEN = "5509269318:AAFB_rA_sMQk0DCAtNHLQZrtpuGgEuanoTU"


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(settings.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", handlers.start_command))
    dispatcher.add_handler(CommandHandler("help", handlers.help_command))

    dispatcher.add_handler(
        MessageHandler(Filters.text("Back to main menu 🔙"), handlers.back_to_main_page)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text("Convert Numbers 🔘"), handlers.convertion_command)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text("Settings ⚙️"), handlers.settings_command)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.text("Conversion to binary 🔢"), handlers.binary_command)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.text("Back to main menu 🔙"), handlers.back_to_main_page),
    )

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(
        MessageHandler(Filters.text & Filters.command, handlers.start_command),
    )
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
