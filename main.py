from aiogram import executor

import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from bot.config import token
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)

