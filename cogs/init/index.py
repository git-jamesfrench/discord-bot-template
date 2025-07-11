from discord.ext import commands
from discord import app_commands
import discord
import traceback
import os

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = os.getenv("PREFIX"),
            intents = discord.Intents.all(),
        )
        self.remove_command('help')
        self.cogs_path = os.getenv("COGS_FOLDER")
        
    async def load_cogs(self):
        self.load_extension(f'{self.cogs_path}.init.errors')
        
        for folder in os.listdir(self.cogs_path):
            if folder != "__pycache__" and folder != "init":
                for cog in os.listdir(os.path.join(self.cogs_path, folder)):
                    if cog.endswith(".py"):
                        try:
                            await self.load_extension(f'{self.cogs_path}.{folder}.{cog[:-3]}')
                            print(f'\033[32m{cog} was successfully added to the cogs.\033[0m')
                        except:
                            print(f'\033[31mAn error occured when installing {cog}:\033[0m')
                            traceback.print_exc()
                            
    async def on_ready(self):
        print(f'\033[34m{self.user} is now up! Latency: {self.latency*1000:.0f}ms\033[0m')
        
        await self.load_cogs()