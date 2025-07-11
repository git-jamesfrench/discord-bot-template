from discord.ext import commands
from discord import app_commands
from config.presets import colors
import discord
import time
import os

class Errors(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        
    async def on_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            embed = discord.Embed(
                title = "Cooldown",
                description = f"> Please retry <t:{int(time.time() + error.retry_after)}:R>.",
                color = colors['error']
            )
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        
        elif isinstance(error, app_commands.MissingPermissions):
            missing_permissions = ', '.join(error.missing_permissions) # You can add this to your message
            embed = discord.Embed(
                title = "Permissions missing",
                description = f"> You don't have the right to do that!",
                color = colors['error']
            )
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        
        else:
            embed = discord.Embed(
                title = "An unknown error occured",
                description = 
                f"> {error}" if bool(os.getenv("DEBUG")) else 
                "> Please report this to the developer of this application",
                color = colors['error']
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            raise error
        
async def setup(bot):
    await bot.add_cog(Errors(bot))