import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "7211896"))
API_HASH = os.environ.get("API_HASH", "d22a4d25860c6673209ea07dc194857a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", 2064609555:AAGeElYciRg-nIKYEsH-53zZkklxB3oyt54)
ARQ_API_KEY = "PCGCCA-FUAEEL-DZPGGH-ZESZXF-ARQ" 
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
