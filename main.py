import discord 
from discord.ext import commands
import os
import webserver
import carte

DISCORD_TOKEN = os.environ['discordkey']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
#bot.load_extension("carte")


@bot.event
async def on_ready():
    print("I'm ready.")
    global target_channel
    target_channel = bot.get_channel("1290026577291120643")

@bot.command()
async def carte(*,ctx):
    embed = discord.Embed(
        color=discord.Colour.red().value(),
        description="Le loup garou peut manger un caca chaque nuit",
        title="Tu es le Loup Garou"
    )
    global target_channel
    await bot.send_message(target_channel,embed=embed)
    #await ctx.send(embed=embed)
webserver.keep_alive()
bot.run(DISCORD_TOKEN)