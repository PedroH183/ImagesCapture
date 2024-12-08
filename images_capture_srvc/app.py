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

while(True):
    # Acessa uma página de exemplo
    driver.get("https://www.google.com")
    logger.info(f"Page Title Captured ::: {driver.title}")

    time.sleep(5)

# Fecha o navegador
driver.quit()
input("Pressione alguma tecla para encerrar ...")
