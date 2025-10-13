import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r"C:\Subdrive\chromedriver-win64"
driver = webdriver.Chrome()

driver.get("http://selenium.dev")


# def setup():
#     driver.get("http://selenium.dev")
#     driver.implicitly_wait(5)
#     return driver
    

# title = driver.title
# assert title == "Selenium" 
# print(title)

time.sleep(50)

driver.quit()