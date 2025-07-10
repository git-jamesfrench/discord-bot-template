from discord.ext import commands
import os

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=os.getenv("PREFIX")
        )