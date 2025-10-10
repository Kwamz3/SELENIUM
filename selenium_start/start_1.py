from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

title = driver.title
assert title == "Selenium" 
print(title + " is the right webpage")

time.sleep(50)