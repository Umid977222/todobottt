import aiohttp
from aiogram import types

from .config import proxy, password, user, proxy3, proxy2
from .inline import get_detail


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                id1 = x['id']
                task_name = x['task_name']
                await message.reply(text=f'Task name: {task_name}'
                                         f'\nTask ID: {id1}',
                                         reply_markup=get_detail()
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
                                             reply_markup=get_detail()
                                        )
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


async def delete1():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                if x['task_name']:
                    id1 = x['id']
                    url_delete = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
                    async with await session.delete(url_delete, auth=aiohttp.BasicAuth(user, password)) as res:
                        return await res.text()


async def ChangeComplete():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                if x['task_name']:
                    id1 = x['id']
                    url_delete = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
                    if not x['completed']:
                        x['completed'] = True
                        async with await session.put(url_delete, auth=aiohttp.BasicAuth(user, password), data=x) as res:
                            return await res.json()
