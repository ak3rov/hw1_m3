import os
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def begin(message: types.Message):
    user = message.from_user.full_name
    await message.answer(
        f"Hello, {user}"
    )


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer("Available commands:\n"
                         "/start - starting\n"
                         "/help - you are here\n"
                         "/myinfo - inf\n"
                         "/picture - photos")


@dp.message_handler(commands='myinfo')
async def cmd_myinfo(message: types.Message):
    await message.answer(f"Ваш id: {message.from_user.id}\n"
                         f"Ваш nickname: {message.from_user.first_name}\n"
                         f"Ваш username: {message.from_user.username}")


@dp.message_handler(commands='picture')
async def picture(message: types.Message):
    images = os.listdir("images")
    image = random.choice(images)
    with open(f"images/{image}", "rb") as f:
        await bot.send_photo(chat_id=message.from_user.id, photo=f)


@dp.message_handler()
async def upper_message(message: types.Message):
    if len(message.text.split()) >= 3:
        await message.answer(message.text.upper())


executor.start_polling(dp)