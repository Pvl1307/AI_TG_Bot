from datetime import datetime

import openai
from aiogram import Bot, Dispatcher, types, executor

from config import TG_TOKEN, OPENAI_TOKEN
from tables_db import Session, User, ConversationHistory

openai.api_key = OPENAI_TOKEN

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):



    await message.reply('Привет, готов к работе! Напиши мне и я отвечу с помощью Chat GPT\n'
                        'Если долго не отвечаю, то, возможно текст слишком большой.\n'
                        'Подожди и получишь ответ!))')


@dp.message_handler()
async def echo_message(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text}
        ],
        temperature=0.2
    )

    await message.reply(response['choices'][0]['message']['content'])


executor.start_polling(dp, skip_updates=True)
