from config.index import Bot
from dotenv import load_dotenv
import asyncio
import os

print('\033[33m⏱ Starting\033[0m')

load_dotenv()

bot = Bot()
asyncio.run(bot.start(os.getenv("TOKEN")))