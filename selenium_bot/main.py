from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver (use the appropriate path for your WebDriver)
driver = webdriver.Chrome()

# Open Booking.com
driver.get("https://www.booking.com")

driver.maximize_window()

# Wait until the page loads and find the search box
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "b769347817")))

# Input location (e.g., "New York")
location ="Accra"
search_box.send_keys(location)

# Select check-in and check-out dates
check_in_date = "2025-12-15"
check_out_date = "2025-12-20"
driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]').click()
driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]').click()

# Submit the search form
search_box.send_keys(Keys.RETURN)

# Wait for the results page to load and sort by lowest price
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sort_option"))).click()
time.sleep(1)
lowest_price_option = driver.find_element(By.XPATH, "//li[contains(@data-id, 'price')]")
lowest_price_option.click()

# Wait for sorted results to load
time.sleep(3)

# Scrape hotel names and prices
hotels = driver.find_elements(By.CLASS_NAME, "sr_property_block_main_row")

for hotel in hotels[:10]:  # Limit to top 10 results
    try:
        name = hotel.find_element(By.CLASS_NAME, "sr-hotel__name").text
        price = hotel.find_element(By.CLASS_NAME, "bui-price-display__value").text
        print(f"Hotel: {name} - Price: {price}")
    except:
        continue

# Close the driver
driver.quit()


