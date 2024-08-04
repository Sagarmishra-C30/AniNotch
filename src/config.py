import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
ANIME_DATABASE_ID = os.getenv('ANIME_DATABASE_ID')
SEASONS_DATABASE_ID = os.getenv('SEASONS_DATABASE_ID')
EPISODES_DATABASE_ID = os.getenv('EPISODES_DATABASE_ID')
CHARACTERS_DATABASE_ID = os.getenv('CHARACTERS_DATABASE_ID')