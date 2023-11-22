from datetime import datetime

import openai
from aiogram import Bot, Dispatcher, types

from config import TG_TOKEN, OPENAI_TOKEN
from tables_db import Session, User, ConversationHistory

openai.api_key = OPENAI_TOKEN

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """Приветсветнное сообщение"""

    await message.reply('Привет, готов к работе! Напиши мне и я отвечу с помощью Chat GPT\n'
                        'Если долго не отвечаю, то, возможно текст слишком большой.\n'
                        'Подожди и получишь ответ!))')


@dp.message_handler()
async def echo_message(message: types.Message):
    """Ответ пользователю с помощью ИИ и запись данных в БД"""
    start_time = datetime.utcnow()

    await message.answer("Ожидайте, обрабатываю ваш запрос...")

    with Session() as session:

        user = session.query(User).filter(User.tg_id == message.from_user.id).first()

        if not user:
            user = User(
                tg_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                registration_date=datetime.utcnow()
            )

            session.add(user)
            session.commit()

        conversation_history = ConversationHistory(
            user_id=user.id,
            user_message=message.text,
            created_at=datetime.utcnow()
        )

        session.add(conversation_history)
        session.commit()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ],
            temperature=0.2
        )

        end_time = datetime.utcnow()
        time_difference = end_time - start_time

        bot_reply = response['choices'][0]['message']['content']

        conversation_history.response_duration = time_difference
        conversation_history.bot_reply = bot_reply
        session.commit()

        await message.reply(response['choices'][0]['message']['content'])
