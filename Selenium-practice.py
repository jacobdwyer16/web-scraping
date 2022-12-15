from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(os.environ['driver'])

def driver_maker():
    settings = webdriver.ChromeOptions()
    settings.add_argument("disable-infobars")
    settings.add_argument("start-maximized")
    settings.add_argument("disable-dev-shm-usage")
    settings.add_argument("no-sandbox")
    settings.add_experimental_option("excludeSwitches", ["enable-automation"])
    settings.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options = settings)
    driver.get("https://www.covenantpca.org/")
    return driver

def main():
    driver = driver_maker()
    driver.find_element(by="id", value=os.environ['id_username']).send_keys(os.environ['username'])
    driver.find_element(by="id", value = os.environ['id_password']).send_keys(os.environ['password'] + Keys.RETURN)
    time.sleep(1)
    driver.find_element(by="xpath", value = os.environ['xpath']).click()
    return driver.current_url

print(main())