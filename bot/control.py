import logging
from aiogram import Bot, Dispatcher
from .config import token
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)
