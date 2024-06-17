from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("25816517", default=None, cast=int)
API_HASH = config("810198b441c95931d237aeb7add44212", default=None)
BOT_TOKEN = config("7433062840:AAHdOqB_4sC5AnQoGHTDT8HVPeryqKvalME", default=None)
BOT_UN = config("pitcabyss_vcompressor_bot", default=None)
AUTH_USERS = config("6537859", default=None, cast=int)
LOG_CHANNEL = config("Pitchabyss_VConverter_Log", default=None)
LOG_ID = config("-1002177528466", default=None)
FORCESUB = config("-1002177528466", default=None)
FORCESUB_UN = config("Pitchabyss_VConverter_Log", default=None)
ACCESS_CHANNEL = config("-4234417552", default=None)
MONGODB_URI = config("mongodb+srv://mail2adityakumar1987:987654321@cluster0.lzwt5np.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
