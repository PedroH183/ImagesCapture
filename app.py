import asyncio
from services.TelegramBot.app import TelegramBot
from services.CaptureImages.app import ScrapperDriver
from services.CaptureImages.app import ScrapperProducts
from utils.DependencyInjector import DependencyInjector

injector = DependencyInjector()

if __name__ == "__main__":
    injector.add_provider('bot_telegram', TelegramBot)
    injector.add_provider('scrapper_products', ScrapperProducts)

    ScrapperDriver().start()