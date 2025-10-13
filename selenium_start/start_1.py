from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


def setup():
    os.environ['PATH'] += r"C:\Subdrive\chromedriver-win64"
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

driver = setup()
driver.get("https://www.wakanow.com.gh/en-gh?gad_campaignid=22361038964")
# driver.get("https://www.google.com")
driver.implicitly_wait(8)

def check():
    title = driver.title
    page_title = "Book Cheap Flights, Hotels and Vacation Packages | Wakanow"
    # assert title == page_title
    if (title == page_title) == True:
        print("Title matches!")
    else:
        print(f"Expected title'{page_title}' but opened '{title}'")

wait = WebDriverWait(driver, 10)
pop_close = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-close")))
pop_close.click()
wait_2 = WebDriverWait(driver, 10)
pop_close_2 = wait_2.until(EC.presence_of_element_located((By.CLASS_NAME, "cm__btn")))
pop_close_2.click()

# wait2 = WebDriverWait(driver, 10)
# pop_close2 = wait2.until(EC.presence_of_element_located((By.ID, "webklipper-publisher-widget-container-notification-close-div")))
# pop_close2.click


time.sleep(70)

def teardown(driver):
    driver.quit()   