import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8748587593:AAFrtAazXuqj6BN8RTx8GYWDHR9jpViJdiE'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Подключение базы данных
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, stars INTEGER)')
conn.commit()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    # Добавляем пользователя, если его нет
    cursor.execute('INSERT OR IGNORE INTO users (id, stars) VALUES (?, ?)', (user_id, 0))
    conn.commit()
    
    # Проверяем реферала
    args = message.get_args()
    if args and int(args) != user_id:
        cursor.execute('UPDATE users SET stars = stars + 1 WHERE id = ?', (int(args),))
        conn.commit()
        await message.answer("Ты пришел по реферальной ссылке!")

    await message.answer(f"Твой баланс: 0 звезд.\nТвоя ссылка: https://t.me/ТВОЙ_БОТ_USERNAME?start={user_id}")

@dp.message_handler(commands=['withdraw'])
async def withdraw(message: types.Message):
    await message.answer("Заявка на вывод создана! Ожидай проверки администратором.")
    # Тут можно добавить уведомление админу
