import aiohttp
from aiogram import types
from .config import proxy, password, user, proxy3, proxy2, url_reg
from .inline import get_detail, get_detail2, get_detail1


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                task_name = x['task_name']
                pk = x['id']
                await message.reply(text=f'Task name: {task_name}'
                                         f'\nTask ID: {pk}',
                                         reply_markup=get_detail2()
                                    )


async def completed(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy2, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                task_name = x['task_name']
                pk = x['id']
                if x['completed']:
                    await message.reply(text=f'Task name: {task_name}'
                                             f'\nTask ID: {pk}'
                                             f'\nCompleted: ✅✅✅',
                                             reply_markup=get_detail1()
                                        )
                elif not x['completed']:
                    await message.answer(text='you do not have completed tasks')


async def uncompleted(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy3, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                task_name = x['task_name']
                pk = x['id']
                if x['completed']:
                    await message.answer(text='you do not have uncompleted tasks')
                else:
                    await message.reply(text=f'Task: {task_name}'
                                             f'\nTask ID: {pk}'
                                             f'\nCompleted: ❌',
                                             reply_markup=get_detail()
                                        )


async def set_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            return await response.json()
