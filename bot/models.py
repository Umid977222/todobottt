from aiogram.dispatcher.filters.state import StatesGroup, State


class EditTask(StatesGroup):
    task_name = State()
    description = State()
    completed = State()
    starting_time = State()
    deadline = State()


class Auth(StatesGroup):
    username = State()
    email = State()
    password = State()

