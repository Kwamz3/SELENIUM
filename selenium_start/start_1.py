from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import random


# def setup():
#     # os.environ['PATH'] += r"C:\Subdrive\chromedriver-win64"
#     options = Options()
#     options.add_argument("--disable-extensions")
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     return driver

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


driver = setup()
print("Script initiated... ")
print("")

# driver.get("https://www.wakanow.com.gh/en-gh?gad_campaignid=22361038964")
driver.get("https://www.wakanow.com.gh")
# driver.get("https://www.google.com")
driver.implicitly_wait(8)

def check():
    title = driver.title
    page_title = "Book Cheap Flights, Hotels and Vacation Packages | Wakanow" or "www.wakanow.com.gh"
    # assert title == page_title
    if (title == page_title) == True:
        print("Title matches!")
        print("Script still running...")
        print("")
    else:
        print(f"Expected title'{page_title}' but opened '{title}'")
        
check()

wait = WebDriverWait(driver, 5)
pop_close = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-close")))
pop_close.click()

# To send the user back to the top of the page
try:
    wait_2 = WebDriverWait(driver, 2)
    pop_close_2 = wait_2.until(EC.presence_of_element_located((By.CLASS_NAME, "fa-angle-up")))
    pop_close_2.click()
except:
    print("Button to scroll up not used")
    print("Script still running...")
    print("")

# Pop-up to agree to cookies
try:
    wait_2 = WebDriverWait(driver, 2)
    pop_close_2 = wait_2.until(EC.presence_of_element_located((By.CLASS_NAME, "cm__btn")))
    pop_close_2.click()
except:
    print("Cookie pop up not present yet")
    print("Script still running...")
    print("")

wait_3 = WebDriverWait(driver, 2)
pop_close_3 = wait_3.until(EC.presence_of_element_located((By.CLASS_NAME, "from")))
pop_close_3.click()

wait_4 = WebDriverWait(driver, 3)
pop_close_4 = wait_4.until(EC.presence_of_element_located((By.ID, "itinerary_0_departure")))
pop_close_4.click()
location = "Accra"
for letter in location:
    pop_close_4.send_keys(letter)
    time.sleep(random.uniform(0.1, 0.2))

wait_5 = WebDriverWait(driver, 10)
pop_close_5 = wait_5.until(EC.presence_of_element_located((By.CLASS_NAME, "flex-fill")))
pop_close_5.click()
print("Location input successful...")    
print("Script still running...")    
print("")

wait_6 = WebDriverWait(driver, 3)
pop_close_6 = wait_6.until(EC.presence_of_element_located((By.ID, "itinerary_0_destination")))
pop_close_6.click()
location = "Dubai"
for letter in location:
    pop_close_6.send_keys(letter)
    time.sleep(random.uniform(0.1, 0.2))

wait_7 = WebDriverWait(driver, 10)
pop_close_7 = wait_7.until(EC.presence_of_element_located((By.CLASS_NAME, "flex-fill")))
pop_close_7.click()
print("Destination input successful...")    
print("Script still running...")    
print("")

wait_8 = WebDriverWait(driver, 10)
pop_close_8 = wait_8.until(EC.presence_of_element_located((By.CLASS_NAME, "link")))
pop_close_8.click()
# print("Destination input successful...")    
# print("Script still running...")    
# print("")

wait_9 = WebDriverWait(driver, 10)
pop_close_9 = wait_9.until(EC.presence_of_element_located((By.CLASS_NAME, "link")))
pop_close_9.click()


time.sleep(70)

def teardown(driver):
    if driver.quit() == True:
        print("Script done!")
        print("Closing page...")
       
type(teardown(driver))