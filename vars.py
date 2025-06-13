# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "27612149"))
API_HASH = environ.get("API_HASH", "9843377992b0b1fbc61d80be068c8d94")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
