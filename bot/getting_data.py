import aiohttp
from aiogram import types

from .config import proxy, password, user, proxy3, proxy2
from .inline import get_inline


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            count = 0
            for x in data:
                task_name = x['task_name']
                description = x['description']
                completed1 = x['completed']
                start = x['starting_time']
                deadline = x['deadline']
                count += 1
                await message.reply(text=f'Task {count}: {task_name}'
                                         f'\nDescription: {description}'
                                         f'\nCompleted: {completed1}'
                                         f'\nStarted_at: {start}'
                                         f'\nDeadline: {deadline}',
                                         reply_markup=get_inline()
                                    )


async def completed(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy2, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            count = 0
            for x in data:
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                count += 1
                await message.reply(text=f'Task {count}: {task_name}'
                                         f'\nDescription: {description}'
                                         f'\nCompleted: ✅✅✅'
                                         f'\nStarted_at: {start}'
                                         f'\nDeadline: {deadline}'
                                    )


async def uncompleted(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy3, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            count = 0
            for x in data:
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                count += 1
                await message.reply(text=f'Task {count}: {task_name}'
                                         f'\nDescription: {description}'
                                         f'\nCompleted: ❌'
                                         f'\nStarted_at: {start}'
                                         f'\nDeadline: {deadline}'
                                    )


async def delete1():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                if x['task_name']:
                    id1 = x['id']
                    url_delete = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/''deletetask''/'
            await session.get(url_delete)
