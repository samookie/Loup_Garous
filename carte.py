from discord.ext import commands
#hfihif
@commands.command()
async def carte(ctx):
    embed = discord.Embed(
        color=discord.Colour.red().value(),
        description="Le loup garou peut manger un caca chaque nuit",
        title="Tu es le Loup Garou"
    )
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(carte)
