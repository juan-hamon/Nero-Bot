from typing import Optional
from discord import Embed
from discord.utils import get
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog
from discord.ext.commands import command

def syntax(command):
    parameters = []
    for key, value in command.params.items():
        if key not in ("self","context"):
            parameters.append(f"[{key}]" if ("Optional" in str(value) or "NoneType" in str(value)) else f"<{key}>")
    parameters = " ".join(parameters)
    if len(parameters) > 0:
        return f"`{str(command)} {parameters}`"
    else:
        return f"`{str(command)} No parameters`"

class HelpMenu(ListPageSource):
    def __init__(self, context, data):
        self.context = context
        super().__init__(data, per_page=3)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)
        embed = Embed(title="Help", description="Welcome to the Nero help menu!", colour = 0xC70039)
        embed.set_thumbnail(url=self.context.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")
        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)
        return embed

    async def format_page(self, menu, entries):
        fields = []
        for entry in entries:
            fields.append((syntax(entry), entry.brief or "No description"))
        return await self.write_page(menu, fields)


class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
    
    async def command_help(self, context, command):
        embed = Embed(title=f"{command}", description=syntax(command), colour = 0xC70039)
        embed.add_field(name="Command description", value=command.brief)
        await context.send(embed=embed)

    @command(brief="This command show how to use an specific command send by parameter or lists all the commands available with their description")
    async def help(self, context, command: Optional[str]):
        if command is None:
            await context.message.delete()
            menu = MenuPages(source=HelpMenu(context, list(self.bot.commands)),
                delete_message_after=True, timeout=60.0)
            await menu.start(context)
        else:
            if (command := get(self.bot.commands, name=command)):
                await self.command_help(context, command)
            else:
                await context.send("That command does not exist.")
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Help")

def setup(bot):
    bot.add_cog(Help(bot))