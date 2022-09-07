from .control import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from .getting_data import fetch


@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}"
    )


@dp.message_handler(commands="listoftask")
async def ListOffTask(message: types.Message):
    result = await fetch()
    await message.reply(
        text=result
    )

#
# @dp.message_handler(commands="upcomingtask")
# async def Upcommintask(message: types.Message):
#     await message.reply(
#
#     )


# @dp.message_handler(commands='help')
# async def help_cmd(message: types.Message):
#     await message.answer(
#         text="Our bot have some commands. you can use it:\n"
#         f"{ListOffTask}\n"
#         f"{Upcommintask}\n"
#     )


