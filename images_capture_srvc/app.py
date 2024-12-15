# system with selenium
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# System debug
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')

# rodando o selenium sem interface grafica
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

try:
    os.mkdir("./images")
except FileExistsError:
    pass

time.sleep(5)

list_products_founded =  driver.find_elements(
    By.CLASS_NAME, "ui-search-result__wrapper"
)
logger.info(f"List of products founded ::: {list_products_founded}")

for index, element in enumerate(list_products_founded):
    try:
        product_title = element.find_element(
            By.CLASS_NAME, "poly-component__title"
        ).find_element(By.CSS_SELECTOR, "a").text

        link_image = element.find_element(
            By.CLASS_NAME, "poly-card__portada"
        ).find_element(By.CLASS_NAME, "poly-component__picture").get_attribute("src")

        logger.info(f"PRODUCT Title :: {product_title}, LINK IMAGE :: {link_image}")

        if link_image or product_title:
            image_binary = requests.get(link_image).content
            img_name = f"./images/img_{index + 1}.jpg"

            with open(img_name, 'ab') as f:
                logger.info(f"Saved Image ::: {img_name}")
                f.write(image_binary)
    except:
        pass
    time.sleep(10)

logger.info(f"Finalizando Indian Bot to Capture Images")
driver.quit()
