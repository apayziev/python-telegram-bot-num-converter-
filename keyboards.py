from telegram import ReplyKeyboardMarkup
from static_text import *


def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    buttons = [
        [convertion_button_text],
        [settings, about],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_settings_command() -> ReplyKeyboardMarkup:
    buttons = [
        [change_language_to_english, change_language_to_uzbek],
        [back_to_main_menu],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_convertion_command() -> ReplyKeyboardMarkup:
    buttons = [
        [conversion_to_binary, conversion_to_octal],
        [conversion_to_decimal, conversion_to_hexadecimal],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_convertion_to_binary_command() -> ReplyKeyboardMarkup:
    buttons = [
        [back_to_previous_page],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
