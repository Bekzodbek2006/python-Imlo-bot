
import logging
from aiogram import Bot, Dispatcher, executor, types
from cheack import cheack
API_TOKEN = '5727920030:AAHg43bDLm19BA_BZagmwdAWaY0TfMJ4pxk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Salom men orqali faqat krilcha so`zlarni tekshirishingiz mumkin.")


@dp.message_handler()
async def result(message: types.Message):
    word = message.text
    checker = cheack(word)
    if checker['available']:
        javob = f"To`g`ri: {word.capitalize()}"
    else:
        javob = f"Xato: {word.capitalize()} \n"
        for msg in checker["matches"]:
            javob += f"{msg.capitalize()}\n"
    await message.answer(javob)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)