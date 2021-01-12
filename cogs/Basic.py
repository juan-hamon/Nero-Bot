from time import time
from discord.ext.commands import Cog
from discord.ext.commands import command

class Basic(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command(brief="Nero responds with pong and the response time.")
    async def ping(self, context):
        start = time()
        message = await context.send("Pong")
        finish = time()
        await message.edit(content=f"Pong! Response time {(finish-start)*1000:,.0f} ms.")

    @command(brief="Command to greet Nero")
    async def hello(self, context):
        await context.send(f"Hello, Master {context.author.mention}")
    
    @command(brief="Shutdowns Nero")
    async def shutdown(self, context):
        if context.author.guild_permissions.administrator:
            await context.send("Shutting down...")
            await self.bot.logout()
        else:
            await context.send("Insufficient permissions to perform that task.")
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Basic")

def setup(bot):
    bot.add_cog(Basic(bot))