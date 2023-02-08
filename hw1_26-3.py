from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = message.from_user.full_name
    # await message.answer(
    #     f"Привет, {user}"
    # )
    await   message.reply(
        f"Привет, {user}"
    )
    await message.delete()


@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.answer(
        """ 
        /start - для старта бота 
        /help - вы сейчас здесь 
        """
    )


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    # await message.answer(
    #     message.text
    # )
    with open('./images/cat.webp', 'rb') as cat:
        await message.answer_photo(
            photo=cat,
            caption='Кот'
        )


executor.start_polling(dp)