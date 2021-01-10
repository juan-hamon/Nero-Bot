import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
OWNER_ID = int(os.getenv('OWNER_ID'))
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL_ID'))
WELCOME_CHANNEL = int(os.getenv('WELCOME_CHANNEL_ID'))
ROLES_CHANNEL = int(os.getenv('ROLES_CHANNEL_ID'))
REACTION_MESSAGE = int(os.getenv('REACTION_MESSAGE_ID'))
WELCOME_ROLE = int(os.getenv('WELCOME_ROLE_ID'))