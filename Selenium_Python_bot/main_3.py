# Importing selenium and it's dependancies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Opening Chrome
driver = webdriver.Chrome()

# Maximizing the window to the entire screen
driver.maximize_window()

# Opening "www.Booking.com"
driver.get("https://www.booking.com")

try:
    # Waiting for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'e135012f1f')))
except Exception as e:
    print(f"Error: {e}")

# Changing currency from Dollar to Euros
time.sleep(1)
select_currency = driver.find_element(By.CLASS_NAME, 'e4adce92df')
select_currency.click()

# Currency changed to EUros
time.sleep(1)
selected_currency = driver.find_element(By.CLASS_NAME, 'ac7953442b')
selected_currency.click()

# Clicking in input field
time.sleep(1)
destination_input = driver.find_element(By.CLASS_NAME, 'eb46370fe1')
destination_input.click()


# Selecting the "Accra-Ghana" option 
time.sleep(1)
destination_input = driver.find_element(By.CLASS_NAME, 'd7430561e2')
destination_input.click()

# Selecting the check-in date







time.sleep(1000)

