from discord.ext.commands import Cog

class Reactions(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.roles = {
                "⌨️": self.bot.guild.get_role(797294423825580063),
                "🇯🇵": self.bot.guild.get_role(797296988630417459),
                "😼": self.bot.guild.get_role(793307074574286848)
            }
            self.reaction_message = await self.bot.get_channel(797289650707759144).fetch_message(797289849626427412)
            self.bot.cogs_ready.ready_up("reactions")

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if self.bot.ready and payload.message_id == self.reaction_message.id:
            current_roles = filter(lambda r: r in roles.values(), payload.member.roles)
            role = self.roles[payload.emoji.name]
            await payload.member.remove_roles(*current_roles, reason="Reaction to role")
            await payload.member.add_roles(role, reason="Reaction to role")
            await reaction_message.remove_reaction(payload.emoji, payload.member)
        

def setup(bot):
    bot.add_cog(Reactions(bot))