import discord 
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']

intents = discord.Intends.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


webserver.keep_alive()
bot.run(DISCORD_TOKEN)