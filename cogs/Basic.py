from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, context):
        await context.send("Pong")

    @commands.command()
    async def hello(self, context):
        await context.send("Hello, Master")

def setup(bot):
    bot.add_cog(Basic(bot))