from typing import Optional
from discord import Embed
from discord.utils import get
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
class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
    
    async def command_help(self, context, command):
        embed = Embed(title=f"{command}", description=syntax(command), colour = 0xC70039)
        embed.add_field(name="Command description", value=command.brief)
        await context.send(embed=embed, delete_after=15)

    @command(brief="This command show how to use an specific command send by parameter or lists all the commands available with their description.")
    async def help(self, context, command: Optional[str]):
        await context.message.delete()
        if command is None:
            embed = Embed(title="Help", description="Welcome to the Nero help menu!", colour = 0xC70039)
            embed.set_thumbnail(url= self.bot.guild.me.avatar_url)
            for name, cog in self.bot.cogs.items():
                commands = cog.get_commands()
                if len(commands) != 0:
                    embed.add_field(name=name, value= f"Here are the commands for {name} ", inline=False)
                    for command in commands:
                        embed.add_field(name=syntax(command), value=command.brief, inline=False)
            await context.send(embed=embed, delete_after=30)
        else:
            if (command := get(self.bot.commands, name=command)):
                await self.command_help(context, command)
            else:
                await context.send("That command does not exist.", delete_after=15)
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("Help")

def setup(bot):
    bot.add_cog(Help(bot))