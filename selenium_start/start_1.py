from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PATH = r"C:\Subdrive\chromedriver-win64\chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("http://selenium.dev")


time.sleep(50)