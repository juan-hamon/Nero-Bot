import os
from discord.ext import commands

from settings import *
from bot import Nero

#bot = commands.Bot(command_prefix="$")

#se cargan los cogs de forma automática utilizandolos como modulos
#for filename in os.listdir("./cogs"):
#    if filename.endswith(".py") and filename != "__init__.py":
#        bot.load_extension(f'cogs.{filename[:-3]}')

#bot.load_extension(f'cogs.test')
#bot.load_extension(f'cogs.basic')

#bot.run(TOKEN)
Nero.run(TOKEN)