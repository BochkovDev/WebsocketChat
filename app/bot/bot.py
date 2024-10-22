import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from users.dao import UsersDAO
from users.models import User
from users.utils import verify_password
from .dao import TelegramUsersDAO


API_TOKEN = os.environ.get('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class BindForm(StatesGroup):
    email = State()
    password = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply('Привет! Я ваш бот уведомлений.')

@dp.message_handler(commands=['bind'])
async def bind_email(message: Message, state: FSMContext):
    """Начинаем процесс привязки аккаунта"""
    await message.reply('Введите ваш email:')
    await state.set_state(BindForm.email)

@dp.message_handler(state=BindForm.email)
async def process_email(message: Message, state: FSMContext):
    """Обрабатываем введенный email"""
    email = message.text

    await state.update_data(email=email)

    await message.reply('Введите пароль от аккаунта:')
    await state.set_state(BindForm.password)

@dp.message_handler(state=BindForm.password)
async def process_password(message: Message, state: FSMContext):
    """Обрабатываем введенный пароль и проверяем пользователя в базе данных"""
    password = message.text

    user_data = await state.get_data()
    email = user_data['email']

    user: User = await UsersDAO.find_one_or_none(email=email)
    if not user:
        await message.reply('Пользователь с таким email не найден.')
        await state.clear()
        return

    password = user_data['password']
    if not verify_password(password, user.password):
        await message.reply('Неверный пароль.')
        await state.clear()
        return

    telegram_id = message.from_user.id
    await TelegramUsersDAO.add(telegram_id=telegram_id, user_id=user.id)

    await message.reply(f'Аккаунт {email} успешно привязан к вашему Telegram.')

    await state.clear()

async def notify_user(user_id: int, username: str, message_text: str):
    """Отправка уведомления пользователю"""
    notification_text = f'Пользователь `{username}`: Отправил вам сообщение!'
    await bot.send_message(user_id, notification_text)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
