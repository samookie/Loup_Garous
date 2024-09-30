from discord.ext import commands
#hfihif
@commands.command()
async def hello(ctx):
    await ctx.send('Hello {0.display_name}.'.format(ctx.author))
    

async def setup(bot):
    bot.add_command(hello)