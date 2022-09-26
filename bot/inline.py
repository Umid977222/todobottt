from aiogram import types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('post', 'action')


def get_inline():
    keybord = types.InlineKeyboardMarkup(row_width=2)
    # buttons = ['delete', 'edit']
    keybord.add(types.InlineKeyboardButton(text='delete', callback_data=cb.new('delete')),
                types.InlineKeyboardButton(text='edit', callback_data=cb.new('edit')),
                types.InlineKeyboardButton(text='✅', callback_data=cb.new('completed'))
                )
    return keybord


def get_detail():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='detail', callback_data=cb.new('detail')))
    return keyboard


def get_edit_buttons():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='Task name', callback_data=cb.new('Task name')),
                 types.InlineKeyboardButton(text='Description', callback_data=cb.new('Description')),
                 types.InlineKeyboardButton(text='starting_time', callback_data=cb.new('starting_time')),
                 types.InlineKeyboardButton(text='Deadline', callback_data=cb.new('Deadline'))
                 )
    return keyboard