from selenium import webdriver
from infra.database import repository
from ..TelegramBot.app import TelegramBot
from selenium.webdriver.common.by import By
from utils.Singleton import SingletonInterface
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.DependencyInjector import DependencyInjector

import sys, logging, time


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Pesquisando imagens no mercado livre
driver.get("https://www.mercadolivre.com.br/")
search_box = driver.find_element(By.ID, "cb1-edit")

search_box.send_keys("Acer Predator")
search_box.send_keys(Keys.RETURN)



class InformationsInvalid(Exception):
    def __init__(self, message):
        self.message = message

class ScrapperProducts:

    __metaclass__ = SingletonInterface

    # TODO : CREATE A VALIDATIOR TO DATA OUTPUT

    def get_product_title(self, product_element):
        return product_element.find_element(
            By.CLASS_NAME, "poly-component__title"
        ).find_element(By.CSS_SELECTOR, "a").text

    def get_product_link(self, product_element):
        return product_element.find_element(
            By.CLASS_NAME, "poly-card__portada"
        ).find_element(By.CLASS_NAME, "poly-component__picture").get_attribute("src")

    def build_information(self, product_element):
        return {
            "product_title" : self.get_product_title(product_element), 
            "product_link_image" : self.get_product_link(product_element)
        }

class ScrapperDriver:

    LIST_PRODUCT_ELEMENT_HTML = "ui-search-result__wrapper"

    def __init__(self):
        self.list_products = driver.find_elements(
            By.CLASS_NAME, self.LIST_PRODUCT_ELEMENT_HTML
        )
        logger.info(f"List of products founded ::: {self.list_products}")

    @DependencyInjector.inject('scrapper_products', 'bot_telegram')
    def start(self, scrapper_products: ScrapperProducts, bot_telegram : TelegramBot):
        for product in self.list_products:
            try :
                information = scrapper_products.build_information(product)
                logger.info(f"Informações capturada do link : {information}")

                if not information:
                    raise InformationsInvalid(
                        f"Não foi possível capturar as informações do produto {product}, state of information : {information}"
                    )

                repository.ins_informations_captured(information)
                bot_telegram.send_mssg_photo(information)

                logger.info(f"Mensagem enviada com sucesso !")
            except Exception as e:
                logger.info(f"Ocorreu um exceção no projeto ao tentar processar : {product} , stacktrace : {str(e)}")

        logger.info(f"Finalizando Indian Bot to Capture Images")
        driver.quit()