import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Gives a random number between 1 and 100")
    async def roll(self, context):
        number = random.randrange(1,101)
        await context.send(number)

def setup(bot):
    bot.add_cog(Games(bot))