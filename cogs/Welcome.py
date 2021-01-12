from discord.ext.commands import Cog
from settings import WELCOME_CHANNEL, WELCOME_ROLE

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(WELCOME_CHANNEL)
        await channel.send(f"Welcome to **{member.guild.name}** {member.mention}!")
        await member.send(f"Hello {member.mention} and Welcome to **{member.guild.name}**, I am Nero the main bot of this server.")
        await member.add_roles(member.guild.get_role(WELCOME_ROLE))
    
    @Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(WELCOME_CHANNEL)
        await channel.send(f"{member.display_name} has left {member.guild.name}")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Welcome")

def setup(bot):
    bot.add_cog(Welcome(bot))