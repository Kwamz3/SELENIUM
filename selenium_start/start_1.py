from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://www.wakanow.com.gh/en-gh?gad_campaignid=22361038964")


driver.quit()