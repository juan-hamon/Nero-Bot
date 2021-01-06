from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Nero responds with pong")
    async def ping(self, context):
        await context.send("Pong")

    @commands.command(brief="Command to greet Nero")
    async def hello(self, context):
        await context.send(f"Hello, Master {context.author.mention}")

def setup(bot):
    bot.add_cog(Basic(bot))