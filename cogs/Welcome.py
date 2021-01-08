from discord.ext.commands import Cog
from discord.ext.commands import command

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_member_join(self, member):
        #Falta agregar el usuario a la bd para el sistema de XP
        channel = self.bot.get_channel(793309421630652416)
        await channel.send(f"Welcome to **{member.guild.name}** {member.mention}!")
        await member.send(f"Hello {member.mention} and Welcome to **{member.guild.name}**, I am Nero the main bot of this server.")
        await member.add_roles(member.guild.get_role(793307074574286848))
    
    @Cog.listener()
    async def on_member_remove(self, member):
        #Falta eliminar el usuairo a la bd para el sistema de XP
        channel = self.bot.get_channel(793309421630652416)
        await channel.send(f"{member.display_name} has left {member.guild.name}")



def setup(bot):
    bot.add_cog(Welcome(bot))