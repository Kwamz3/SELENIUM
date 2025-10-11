from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.wakanow.com.gh/en-gh?gad_campaignid=22361038964")

wait = WebDriverWait(driver, 10)
pop_close = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-close")))
pop_close.click()

time.sleep(70)
driver.quit()