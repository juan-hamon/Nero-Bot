from discord.utils import get
from discord.ext.commands import Cog
from settings import ROLES_CHANNEL, REACTION_MESSAGE

class Reactions(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if self.bot.ready and payload.message_id == self.reaction_message.id:
            Welcome_role = get(self.bot.guild.roles, name="New")
            current_roles = filter(lambda r: r in self.roles.values(), payload.member.roles)
            role = self.roles[payload.emoji.name]
            if Welcome_role in payload.member.roles:
                await payload.member.remove_roles(Welcome_role, reason="Reaction to role for first time")
                await payload.member.add_roles(role, reason="Reaction to role")
                await self.reaction_message.remove_reaction(payload.emoji, payload.member)
            else:
                await payload.member.remove_roles(*current_roles, reason="Reaction to role")
                await payload.member.add_roles(role, reason="Reaction to role")
                await self.reaction_message.remove_reaction(payload.emoji, payload.member)
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.roles = {
                "⌨️": self.bot.guild.get_role(797294423825580063),
                "🇯🇵": self.bot.guild.get_role(797296988630417459),
                "😼": self.bot.guild.get_role(793307074574286848)
            }
            self.reaction_message = await self.bot.get_channel(ROLES_CHANNEL).fetch_message(REACTION_MESSAGE)
            self.bot.cogs_ready.ready_up("Reactions")

def setup(bot):
    bot.add_cog(Reactions(bot))