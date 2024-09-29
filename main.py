import discord 
from discord.ext import commands
import os
import webserver
import carte

DISCORD_TOKEN = os.environ['discordkey']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.load_extension("carte")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)