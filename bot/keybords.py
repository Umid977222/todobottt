from aiogram import types


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Task name'),
                 types.KeyboardButton(text='Description'),
                 types.KeyboardButton(text='Start time'),
                 types.KeyboardButton(text='Deadline')
                 )
    return keyboard
