from .control import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from .getting_data import fetch, completed, uncompleted, delete1
from .inline import cb


@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}"
    )


@dp.message_handler(commands="listoftask")
async def ListOffTask(message: types.Message):
    await fetch(message)


@dp.message_handler(commands="completed")
async def CompletedTask(message: types.Message):
    await completed(message)


@dp.message_handler(commands="uncompleted")
async def UncompletedTask(message: types.Message):
    await uncompleted(message)


@dp.callback_query_handler(cb.filter(action=['delete', 'edit']))
async def cb_data(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'delete':
        result = await delete1()
        await query.answer(
            text='Accept Deleted',
            url=result
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


