from discord.ext.commands import Cog
from discord.ext.commands import command

class Basic(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command(brief="Nero responds with pong")
    async def ping(self, context):
        await context.send("Pong")

    @command(brief="Command to greet Nero")
    async def hello(self, context):
        await context.send(f"Hello, Master {context.author.mention}")
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Basic")

def setup(bot):
    bot.add_cog(Basic(bot))