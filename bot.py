import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8748587593:AAEH7fp4ub4pvXYXy4M-pgniGEQKL9T'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("""Привет! Это бот для заработка звезд. 🌟

Как это работает:
1. Зарабатывай звезды за приглашение людей!
2. Приглашай друзей по своей ссылке.
3. Копи звезды и выводи их.""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
