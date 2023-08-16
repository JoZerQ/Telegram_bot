import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import random

bot = Bot(config("API_TOKEN"))
dp = Dispatcher(bot)

Category = {
    "привет": "hi.txt",
    "здравствуй": "hi.txt",
    "как дела?": "HowAreYou.txt",
    "какая погода за окном?": "weather.txt",
    "как тебя зовут?": "name.txt",
    "сколько тебе дней?": "age.txt",
    "который час?": "time.txt"
}

def Random_Response(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return random.choice(lines).strip()

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! \nЗадавайте вопросы!")

@dp.message_handler(lambda message: message.text.lower() in Category)
async def reply_to_message(message: types.Message):
    user_message = message.text.lower()
    if user_message in Category:
        file_path = Category[user_message]
        response = Random_Response(file_path)
        await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

