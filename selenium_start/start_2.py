import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# os.environ['PATH'] += r"C:\Subdrive\chromedriver-win64"
driver = webdriver.Chrome()

# driver.get("http://selenium.dev")


# def setup():
#     driver.get("http://selenium.dev")
#     driver.implicitly_wait(5)
#     return driver
    
# title = driver.title
# assert title == "Selenium" 
# print(title)

# time.sleep(50)

# driver.quit()


def setup():
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    driver.implicitly_wait(8)
    return driver

driver = setup()

# btn btn-lg
wait = WebDriverWait(driver, 8)
formy_click = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-lg')))
formy_click.click()

time.sleep(70)

def teardown(driver):
    driver.quit()
   
    