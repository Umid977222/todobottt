from todobottt.bot.commands import register

token = '5743779089:AAHfajZJ47VsgadTWJDXBk_idQeBHCLE2Bs'

proxy = 'http://127.0.0.1:8000/tasks/'
proxy2 = 'http://127.0.0.1:8000/tasks/completed'
proxy3 = 'http://127.0.0.1:8000/tasks/uncompleted'
user_data = {}


async def user_data1():
    result = await register()
    user = result['user']['username']
    password = result['user']['password']
    user_data['user'] = user
    user_data['password'] = password
    return user, password

