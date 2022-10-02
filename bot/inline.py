from aiogram import types
from aiogram.utils.callback_data import CallbackData


cb = CallbackData('post', 'action')


def get_completed():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    # buttons = ['delete', 'edit']
    keyboard.add(types.InlineKeyboardButton(text='🗑', callback_data=cb.new('delete1')),
                 types.InlineKeyboardButton(text='📝', callback_data=cb.new('edit1')),
                 types.InlineKeyboardButton(text='✅', callback_data=cb.new('completed')))
    return keyboard


def get_inline():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    # buttons = ['delete', 'edit']
    keyboard.add(types.InlineKeyboardButton(text='🗑', callback_data=cb.new('delete')),
                 types.InlineKeyboardButton(text='📝', callback_data=cb.new('edit')))
    return keyboard


def get_detail():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='⚙️⚡️⚙️', callback_data=cb.new('detail')))
    return keyboard


def get_detail1():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='⚙️⚡️⚙️', callback_data=cb.new('detail1')))
    return keyboard


def get_detail2():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='⚙️⚡️⚙️', callback_data=cb.new('detail2')))
    return keyboard


def get_edit_buttons():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='Task name', callback_data=cb.new('task_name')),
                 types.InlineKeyboardButton(text='Description', callback_data=cb.new('description')),
                 types.InlineKeyboardButton(text='starting_time', callback_data=cb.new('starting_time')),
                 types.InlineKeyboardButton(text='Deadline', callback_data=cb.new('deadline')),
                 types.InlineKeyboardButton(text='Go back', callback_data=cb.new('back'))
                 )
    return keyboard

def calendar():
    start_kb = types.InlineKeyboardMarkup(row_width=2)
    start_kb.add(
                 types.InlineKeyboardButton(text='Navigation Calendar', callback_data=cb.new('Navigation Calendar')),
                 types.InlineKeyboardButton(text='Dialog Calendar', callback_data=cb.new('Dialog Calendar'))
                 )
    return start_kb
