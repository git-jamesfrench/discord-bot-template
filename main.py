from config.index import Bot
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot()
bot.run(os.getenv("TOKEN"))