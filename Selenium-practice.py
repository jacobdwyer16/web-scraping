from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
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

def cleaner(string):
    string = string.split(":")
    if len(string)>1:
        return string[:-1]
    return string[0]

def main():
    driver = driver_maker()
    time.sleep(2)
    element = driver.find_element(by="xpath", value=os.environ['xpath'])
    return cleaner(element.text)
    
print(main())