import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv


load_dotenv("./config.env")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


class TelegramBot:

    def __init__(self):
        self.bot : Bot = Bot(token=TELEGRAM_TOKEN)

    def send_mssg_photo(self, information : dict):
        asyncio.run(self.bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=f"Novo item adicionado na base\n*nome : {information.get('product_title')}*"
        ))