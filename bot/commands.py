import aiohttp
from aiogram.dispatcher import FSMContext

from .config import user, password
from .control import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from .getting_data import fetch, completed, uncompleted, set_data
from .inline import cb, get_inline, get_edit_buttons, get_completed, calendar
from .models import EditTask
from todobottt.bot.aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar

global id1


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


@dp.message_handler(commands="calendar")
async def UncompletedTask(message: types.Message):
    await message.answer(f'calendar', reply_markup=calendar())


@dp.callback_query_handler(cb.filter(action=['Navigation Calendar']))
async def cb_data(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'Navigation Calendar':
        await query.message.edit_text("Please select a date: ", reply_markup=await SimpleCalendar().start_calendar())


@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(query: types.CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(query, callback_data)
    if selected:
        await query.message.edit_text(f'{date.strftime("%d/%m/%Y")}')


@dp.callback_query_handler(cb.filter(action=['Dialog Calendar']))
async def cb_data2(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'Dialog Calendar':
        await query.message.edit_text("Please select a date: ", reply_markup=await DialogCalendar().start_calendar())


@dp.callback_query_handler(dialog_cal_callback.filter())
async def process_dialog_calendar(query: types.CallbackQuery, callback_data: dict):
    selected, date = await DialogCalendar().process_selection(query, callback_data)
    if selected:
        await query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}'
        )



@dp.callback_query_handler(cb.filter(action=['detail']))
async def cb_data(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'detail':
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                id1 = x['id']
                await query.message.edit_text(text=f'Task name: {task_name}'
                                                   f'\nTask ID: {id1}'
                                                   f'\nDescription: {description}'
                                                   f'\nStarted_at: {start}'
                                                   f'\nDeadline: {deadline}',
                                                   reply_markup=get_completed()
                                              )


@dp.callback_query_handler(cb.filter(action=['detail1']))
async def cb_data1(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'detail1':
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                id1 = x['id']
                await query.message.edit_text(text=f'Task name: {task_name}'
                                                   f'\nTask ID: {id1}'
                                                   f'\nDescription: {description}'
                                                   f'\nStarted_at: {start}'
                                                   f'\nDeadline: {deadline}',
                                                   reply_markup=get_inline())


@dp.callback_query_handler(cb.filter(action=['detail2']))
async def cb_data2(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'detail2':
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                task_name = x['task_name']
                description = x['description']
                start = x['starting_time']
                deadline = x['deadline']
                id1 = x['id']
                await query.message.edit_text(text=f'Task name: {task_name}'
                                                   f'\nTask ID: {id1}'
                                                   f'\nDescription: {description}'
                                                   f'\nStarted_at: {start}'
                                                   f'\nDeadline: {deadline}',
                                                   reply_markup=get_inline())


@dp.callback_query_handler(cb.filter(action=['delete', 'edit']))
async def cb_edit(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'delete':
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                pk = x['id']
                url_detail = 'http://127.0.0.1:8000/tasks/' + str(pk) + '/'
                async with aiohttp.ClientSession() as session:
                    async with await session.delete(url_detail, auth=aiohttp.BasicAuth(user, password)):
                        await query.message.edit_text(f'Accepted deleted')
    elif action == 'edit':
        await query.message.edit_reply_markup(get_edit_buttons())


@dp.callback_query_handler(cb.filter(action=['delete1', 'edit1', 'completed']))
async def cb_comp(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'delete1':
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                pk = x['id']
                url_detail = 'http://127.0.0.1:8000/tasks/' + str(pk) + '/'
                async with aiohttp.ClientSession() as session:
                    async with await session.delete(url_detail, auth=aiohttp.BasicAuth(user, password)):
                        await query.message.edit_text(f'Accepted deleted')
    elif action == 'edit1':
        await query.message.edit_reply_markup(get_edit_buttons())
    elif action == "completed":
        result = await set_data()
        for x in result:
            if query.message.text.splitlines()[1][9:] == str(x['id']):
                pk = x['id']
                x["completed"] = True
                url_detail = 'http://127.0.0.1:8000/tasks/' + str(pk) + '/'
                async with aiohttp.ClientSession() as session:
                    async with await session.patch(url_detail, auth=aiohttp.BasicAuth(user, password), data=x):
                        await query.message.edit_text(f'Accepted completed ✅✅✅')


@dp.callback_query_handler(cb.filter(action=['task_name', 'description', 'starting_time', 'deadline', 'back']))
async def call_updates(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'task_name':
        await query.message.answer(text='Enter new task name: ')
        await EditTask.task_name.set()
    elif action == 'description':
        await query.message.answer(text='Enter new description: ')
        await EditTask.description.set()
    elif action == 'starting_time':
        await query.message.answer(text='Enter new start time of task')
        await EditTask.starting_time.set()
    elif action == 'deadline':
        await query.message.answer(text='Enter new deadline time of task')
        await EditTask.deadline.set()
    elif action == 'back':
        await query.message.edit_reply_markup(reply_markup=get_inline())
    await query.answer()


@dp.message_handler(state=EditTask.task_name)
async def get_task_name(message: types.Message, state: FSMContext):
    task_name = message.text
    await state.update_data(task_name=task_name)
    result = await set_data()
    for x in result:
        if id1 == ['id']:
            x["task_name"] = task_name
            url_detail = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
            async with aiohttp.ClientSession() as session:
                async with await session.patch(url_detail, auth=aiohttp.BasicAuth(user, password), data=x):
                    await message.answer(f'Accepted new task name {x["task_name"]}')
    await state.finish()


@dp.message_handler(state=EditTask.description)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    result = await set_data()
    for x in result:
        if id1 == ['id']:
            x["description"] = description
            url_detail = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
            async with aiohttp.ClientSession() as session:
                async with await session.patch(url_detail, auth=aiohttp.BasicAuth(user, password), data=x):
                    await message.answer(f'Accepted new description {x["description"]}')
    await state.finish()


@dp.message_handler(state=EditTask.starting_time)
async def get_starting_time(message: types.Message, state: FSMContext):
    datetime = message.text.split(' ')
    date = datetime[0].split('.')
    time = datetime[1].split(':')
    starting_time = f'{date[2]}-{date[1]}-{date[0]}' + f' {time[0]}:{time[1]}'
    await state.update_data(starting_time=starting_time)
    result = await set_data()
    for x in result:
        if id1 == ['id']:
            x["starting_time"] = starting_time
            url_detail = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
            async with aiohttp.ClientSession() as session:
                async with await session.patch(url_detail, auth=aiohttp.BasicAuth(user, password), data=x):
                    await message.answer(f'Task name: {x["task_name"]}'
                                         f'\nAccepted new start time {x["starting_time"]}')
    await state.finish()


@dp.message_handler(state=EditTask.deadline)
async def get_deadline(message: types.Message, state: FSMContext):
    datetime = message.text.split(' ')
    date = datetime[0].split('.')
    time = datetime[1].split(':')
    deadline = f'{date[2]}-{date[1]}-{date[0]}' + f' {time[0]}:{time[1]}'
    await state.update_data(deadline=deadline)
    result = await set_data()
    for x in result:
        if id1 == ['id']:
            x["deadline"] = deadline
            url_detail = 'http://127.0.0.1:8000/tasks/' + str(id1) + '/'
            async with aiohttp.ClientSession() as session:
                async with await session.patch(url_detail, auth=aiohttp.BasicAuth(user, password), data=x):
                    await message.answer(f'Task name: {x["task_name"]}'
                                         f'\nAccepted new deadline time {x["deadline"]}')
    await state.finish()
