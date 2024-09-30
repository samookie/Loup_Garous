from discord.ext import commands
#hfihif
@commands.command()
async def hello(ctx):
<<<<<<< Updated upstream
    await ctx.send('Hello {0.display_name}.'.format(ctx.author))
    
=======
    embed = discord.embed(
        colour=discord.Colour.blue()
        description="Le loup garou peut éliminé un joueur au choix chaque nuit",
        title="Tu es le Loup Garou"
    )
    await ctx.send(embed=embed)
>>>>>>> Stashed changes

async def setup(bot):
    bot.add_command(hello)
