from discord.ext import commands
import traceback
import discord

class Cog(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        
    @commands.command("sync")
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx):
        message = await ctx.send("⏱ Syncing tree")
        try:
            await self.bot.tree.sync()
            await message.edit(content="✔ Synced")
        except Exception as e:
            await message.edit(content=f"⚠ {e}")
            traceback.print_exc()
            
async def setup(bot):
    await bot.add_cog(Cog(bot))