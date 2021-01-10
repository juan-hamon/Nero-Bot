from typing import Optional
from discord import Embed, Member, NotFound, Object
from discord.utils import find
from discord.ext.commands import Cog, Greedy, Converter
from discord.ext.commands import CheckFailure, BadArgument
from discord.ext.commands import command, has_permissions, bot_has_permissions
from settings import LOG_CHANNEL

class BannedUser(Converter):
	async def convert(self, context, arg):
		if context.guild.me.guild_permissions.ban_members:
			if arg.isdigit():
				try:
					return (await context.guild.fetch_ban(Object(id=int(arg)))).user
				except NotFound:
					raise BadArgument

		banned = [e.user for e in await context.guild.bans()]
		if banned:
			if (user := find(lambda u: str(u) == arg, banned)) is not None:
				return user
			else:
				raise BadArgument

class Mod(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command(name="kick", brief="This command kicks members from the server, you can attach the reason so the members know why they are been kicked")
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick_members(self, context, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided"):
        if not len(targets):
            await context.send("One or more required arguments missing.")
        else:
            for target in targets:
                if (context.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator):
                    await target.kick(reason=reason)
                    embed = Embed(title="Member kicked", colour=0xC70039)
                    embed.set_thumbnail(url=target.avatar_url)
                    embed.add_field(name="Member", value=target.name, inline=False)
                    embed.add_field(name="Actioned by", value=f"{context.author.display_name}", inline=False)
                    embed.add_field(name="Reason", value=reason, inline=False)
                    await self.bot.get_channel(LOG_CHANNEL).send(embed=embed)
                else:
                    await context.send(f"{target.display_name} could not be kicked")
    
    @kick_members.error
    async def kick_members_error(self, context, exc):
        if isinstance(exc, CheckFailure):
            await context.send("Insufficient permissions to perfom that task.")

    @command(name="ban", brief="This command bans members from the server, you can attach the reason so the members know why they are been banned")
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban_members(self, context, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided"):
        if not len(targets):
            await context.send("One or more required arguments missing.")
        else:
            for target in targets:
                if (context.guild.me.top_role.position > target.top_role.position and not target.guild_permissions.administrator):
                    await target.ban(reason=reason)
                    embed = Embed(title="Member banned", colour=0xC70039)
                    embed.set_thumbnail(url=target.avatar_url)
                    embed.add_field(name="Member", value=target.name, inline=False)
                    embed.add_field(name="Actioned by", value=f"{context.author.display_name}", inline=False)
                    embed.add_field(name="Reason", value=reason, inline=False)
                    await self.bot.get_channel(LOG_CHANNEL).send(embed=embed)
                else:
                    await context.send(f"{target.display_name} could not be banned")
    
    @ban_members.error
    async def ban_members_error(self, context, exc):
        if isinstance(exc, CheckFailure):
            await context.send("Insufficient permissions to perfom that task.")

    @command(name="unban", brief="This command unbans members from the server, you can attach the reason so the members know why they are been unbanned")
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def unban_members(self, context, targets: Greedy[BannedUser], *, reason: Optional[str] = "No reason provided"):
        if not len(targets):
            await context.send("One or more required arguments missing.")
        else:
            for target in targets:
                await context.guild.unban(target, reason=reason)
                embed = Embed(title="Member unbanned", colour=0xC70039)
                embed.set_thumbnail(url=target.avatar_url)
                embed.add_field(name="Member", value=target.name, inline=False)
                embed.add_field(name="Actioned by", value=f"{context.author.display_name}", inline=False)
                embed.add_field(name="Reason", value=reason, inline=False)
                await self.bot.get_channel(LOG_CHANNEL).send(embed=embed)
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Mod")

def setup(bot):
    bot.add_cog(Mod(bot))