from os import remove
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update,
)

from telegram.ext import (
    CallbackContext,
    ConversationHandler,
)
import keyboards, static_text


def start_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user

    text = (
        f"Welcome, <code>{user.first_name}!</code> \
        <b>\n\nThis is a simple bot to convert numbers to different number systems.</b>",
    )
    update.message.reply_text(
        text=text,
        reply_markup=keyboards.make_keyboard_for_start_command(),
        parse_mode="HTML",
    )


def settings_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /settings is issued."""
    update.message.reply_text(
        "Settings!",
        reply_markup=keyboards.make_keyboard_for_settings_command(),
    )


def back_to_main_page(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=static_text.you_on_main_menu,
        reply_markup=keyboards.make_keyboard_for_start_command(),
        parse_mode="HTML",
    )
    return ConversationHandler.END


def convertion_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /convertion is issued."""
    update.message.reply_text(
        text=static_text.convertion_command_text,
        reply_markup=keyboards.make_keyboard_for_convertion_command(),
        parse_mode="HTML",
    )


def binary_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /binary is issued."""
    update.message.reply_text(
        text=static_text.conversion_to_binary,
        reply_markup=keyboards.make_keyboard_for_convertion_to_binary_command(),
        parse_mode="HTML",
    )

    keyboard = [
        [
            InlineKeyboardButton(
                static_text.binary_to_octal, callback_data="binary_to_octal"
            )
        ],
        [
            InlineKeyboardButton(
                static_text.binary_to_decimal, callback_data="binary_to_decimal"
            )
        ],
        [
            InlineKeyboardButton(
                static_text.binary_to_hexadecimal, callback_data="binary_to_hexadecimal"
            ),
        ],
    ]

    reply_markup = reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        text=static_text.conversion_type,
        reply_markup=reply_markup,
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")
