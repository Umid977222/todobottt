from aiogram.dispatcher import FSMContext
from aiogram_datepicker import Datepicker, DatepickerSettings, datepicker
from .control import dp
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from .getting_data import fetch, completed, uncompleted, delete1, changecomplete
from .inline import cb, get_edit_buttons
from .keybords import get_keyboard
from .models import EditTask


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


@dp.callback_query_handler(cb.filter(action=['delete', 'edit', 'completed']))
async def cb_data(query: types.CallbackQuery, callback_data: dict):
    action = callback_data.get('action')
    if action == 'delete':
        result = await delete1()
        if result == '':
            await query.message.edit_text(text='Accept deleted')
        else:
            await query.message.edit_text(text=f'{result}')
    elif action == 'edit':
        await query.message.answer(text='Which one do you want to change of task',
                                   reply_markup=get_edit_buttons())
    elif action == 'completed':
        data = await changecomplete()
        if data:
            await query.answer(text="changed")
    await query.answer()


# @dp.callback_query_handler(cb.filter(action=['Task name']))
# async def start_time(message: types.Message):


@dp.callback_query_handler(cb.filter(action=['Description']))
async def get_description(message: types.Message, state: FSMContext):
    await message.answer(text='Enter description: ')
    await EditTask.description.set()


@dp.message_handler(state=EditTask.starting_time)
async def get_start_time(message: types.Message):
    datepicker1 = Datepicker()
    markup = datepicker1.start_calendar()
    await message.answer(text='Enter start time:', reply_markup=markup)

# @dp.callback_query_handler(cb.filter(action=['starting_time']))
# async def set_start_time(query: types.CallbackQuery, state: FSMContext):


    # await EditTask.starting_time.set()


@dp.message_handler(state=EditTask.task_name)
async def set_task_name(message: types.Message, state: FSMContext):
    task_name = message.text
    await state.update_data(task_name=task_name)


@dp.message_handler(state=EditTask.description)
async def set_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)


@dp.message_handler(state=EditTask.starting_time)
async def set_description(message: types.Message, state: FSMContext):
    starting_time = message.text
    await state.update_data(starting_time=starting_time)

# def _get_datepicker_settings():
#     return DatepickerSettings() #some settings
#
#
# @dp.message_handler(state=EditTask.starting_time)
# async def _main(message: types.Message):
#     datepicker = Datepicker(_get_datepicker_settings())
#
#     markup = datepicker.start_calendar()
#     await message.answer('Select a date: ', reply_markup=markup)
#
#
# @dp.callback_query_handler(Datepicker.datepicker_callback.filter())
# async def _process_datepicker(callback_query: types.CallbackQuery, callback_data: dict):
#     datepicker = Datepicker(_get_datepicker_settings())
#
#     date = await datepicker.process(callback_query, callback_data)
#     if date:
#         await callback_query.message.answer(date.strftime('%d/%m/%Y'))
#
#     await callback_query.answer()
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


