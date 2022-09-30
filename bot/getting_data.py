import aiohttp
from aiogram import types

from .config import proxy, password, user, proxy3, proxy2
from .inline import get_detail, get_detail1, get_detail2


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            count = 0
            for x in data:
                task_name = x['task_name']
                count += 1
                await message.reply(text=f'Task {count}: {task_name}',
                                         reply_markup=get_detail1()
                                    )


async def completed(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy2, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                if x['completed']:
                    await message.reply(text=f'Task: {task_name}'
                                             f'\nDescription: {description}'
                                             f'\nCompleted: ✅✅✅'
                                             f'\nStarted_at: {start}'
                                             f'\nDeadline: {deadline}',
                                             reply_markup=get_detail2())
                else:
                    await message.answer(text='you do not have completed tasks')


async def uncompleted(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy3, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                if x['completed']:
                    await message.answer(text='you do not have uncompleted tasks')
                else:
                    await message.reply(text=f'Task: {task_name}'
                                             f'\nDescription: {description}'
                                             f'\nCompleted: ❌'
                                             f'\nStarted_at: {start}'
                                             f'\nDeadline: {deadline}',
                                             reply_markup=get_detail()
                                        )


async def set_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            return await response.json()
