import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8748587593:AAFrtAazXuqj6BN8RTx8GYWDHR9jPvIjdiE'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Na1pex stars запущен и готов к работе! 🚀")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
