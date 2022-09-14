from aiogram import types
from .control import dp


def lang():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["Uzb", "Rus", "fdsfds"]
    keyboard.add(*buttons)
    return keyboard