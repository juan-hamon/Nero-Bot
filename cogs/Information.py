from typing import Optional
from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command

class Information(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_human_members(self, context):
        for member in context.guild.members:
            if not member.bot:
                self.human_members.append(member)
    
    def get_bot_members(self, context):
        for member in context.guild.members:
            if member.bot:
                self.bot_members.append(member)

    @command(name="userinfo", brief="This command gives information about the user that is mentioned or, if not provided, the user that calls the command.")
    async def user_information(self, context, target: Optional[Member]):
        target = target or context.author
        embed = Embed(title=f"{target.name} information", colour=0xC70039)
        embed.set_thumbnail(url=target.avatar_url)
        embed.add_field(name="ID", value=target.id, inline=True)
        embed.add_field(name="Is Bot?", value=target.bot, inline=True)
        embed.add_field(name="Top role", value=target.top_role.mention, inline=True)
        embed.add_field(name="Status", value=str(target.status).title(), inline=True)
        embed.add_field(name="Joined the server", value=target.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="Boosted", value=bool(target.premium_since), inline=True)
        await context.send(embed=embed)

    @command(name="serverinfo", brief="This command gives information about the server.")
    async def server_information(self, context):
        embed = Embed(title="Server information", colour=0xC70039)
        embed.add_field(name="ID",value=context.guild.id,inline=True)
        embed.add_field(name="Region",value=context.guild.region,inline=True)
        embed.add_field(name="Created at",value=context.guild.created_at.strftime("%d/%m/%Y"),inline=True)
        self.get_human_members(context)
        embed.add_field(name="Humans",value=len(self.human_members),inline=True)
        self.get_bot_members(context)
        embed.add_field(name="Bots",value=len(self.bot_members),inline=True)
        embed.add_field(name="Banned members",value=len(await context.guild.bans()),inline=True)
        embed.add_field(name="Text channels",value=len(context.guild.text_channels),inline=True)
        embed.add_field(name="Voice channels",value=len(context.guild.voice_channels),inline=True)
        embed.add_field(name="Roles",value=len(context.guild.roles),inline=True)
        await context.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.human_members = []
            self.bot_members = []
            self.bot.cogs_ready.ready_up("Information")

def setup(bot):
    bot.add_cog(Information(bot))