import random
from discord.ext.commands import Cog
from discord.ext.commands import command

class Games(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command(brief="Gives a random number between 1 and 100")
    async def roll(self, context):
        number = random.randrange(1,101)
        await context.send(number)
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Games")

def setup(bot):
    bot.add_cog(Games(bot))