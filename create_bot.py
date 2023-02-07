import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

bot = Bot("TOKEN")
dp = Dispatcher(bot)
