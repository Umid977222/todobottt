import types

from bot.control import dp
from aiogram import types
from bot.getting_data import fetch


@dp.message_handler()
async def task(message: types.Message):
    result = await fetch()
#   task_name =
#   description
#   completed
#   starting_time
#   deadline
