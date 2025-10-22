import os
import const
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Booking(webdriver.Chrome): 
    def __init__(self, driver_path= r"C:\Subdrive\chromedriver-win64", teardown= False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--incognito")
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            
    # def clear_cache(self):
    #     self.execute._cdp_cmd()
        
    def open_page(self):
        self.get(const.BASE_URL)
        
    def check_page(self):
        if const.PAGE_TITLE == self.title:
            print("Title matches!")
            print("Script still running...")
            print("")
        else:
            self.quit()
            print(f"Expected title'{const.PAGE_TITLE}' but opened '{self.title}'")
            
            
         
    def popup_close(self):
        popup_click = self.find_element(By.CLASS_NAME, "btn-close")
        popup_click.click()
        print("Popup has been cleared successfully!")
        print("Script still running...")
        print("")
        
    # def change_currency(self, currency=None):
    #         if str(self.find_element(By.CLASS_NAME, "country").text) != "GH | EN | GHS":
    #             currency_click = self.find_element(By.CLASS_NAME, "p-3")
    #             currency_click.click()
    #             print("Currency changed successfully!")
    #             print("Script still running...")
    #             print("")
    #             print(str(self.find_element(By.CLASS_NAME, "country").text))
    #         else:
    #             print("Currency already set to GHS!")
    #             print("Script still running...")
    
    def select_city(self, place_from):
        wait = WebDriverWait(self, 8)
        city_trigger = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "from")))
        city_trigger.click()
        
        time.sleep(0.5)
        city_click = wait.until(EC.element_to_be_clickable((By.ID, "itinerary_0_departure")))
        city_click.click()
        for letter in place_from:
            city_trigger.send_keys(letter)
            time.sleep(random.uniform(0.1, 0.2))
        
        first_result = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[contains(text(), '{place_from}')]")))
        first_result.click()
        print(f"City {place_from} entered successfully!")
        print("Script still running...")
        print("")
    
    
    def select_destination(self, place_to):
        wait = WebDriverWait(self, 8)
        city_trigger = wait.until(EC.presence_of_element_located((By.ID, "itinerary_0_destination")))
        city_trigger.click()
        
        time.sleep(0.5)
        for letter in place_to:
            city_trigger.send_keys(letter)
            time.sleep(random.uniform(0.1, 0.2))
        
        first_result = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[contains(text(), '{place_to}')]")))
        first_result.click()
        print(f"Destination {place_to} entered successfully!")
        print("Script still running...")
        print("")
        
    def select_dep_date(self, day:str, month:str, date:str, year:int):
        wait = WebDriverWait(self, 8)
        aria_label = f"{day}, {month} {date}, {year}"
        select_dep_click = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 
            f"div[aria-label='{aria_label}']"
            )))
       
        select_dep_click_2 = select_dep_click.find_element(By.CSS_SELECTOR, "span.custom-day")
        select_dep_click_2.click()
        print(f"Departure date {aria_label} entered successfully!")
        print("Script still running...")
        print("")
    
    
    def select_ret_date(self, day:str, month:str, date:str, year:int):
        wait = WebDriverWait(self, 8)
        aria_label = f"{day}, {month} {date}, {year}"
        select_dep_click = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 
            f"div[aria-label='{aria_label}']"
            )))
        
        select_dep_click_2 = select_dep_click.find_element(By.CSS_SELECTOR, "span.custom-day")
        select_dep_click_2.click()
        print(f"Return date {aria_label} entered successfully!")
        print("Script still running...")
        print("")
    

    def select_passengers(self, adl_cnt:int, chd_cnt:None, inf_cnt:None):
        wait = WebDriverWait(self, 8)
        
        select_adults = wait.until(EC.presence_of_element_located((
            By.XPATH, 
            f"//div[@class='mb-4']//"
            )))
        
        select_adults_2 = select_adults.find_element(By.CSS_SELECTOR, f"span[contains(text(),'{adl_cnt}')]")
        select_adults_2.click()
       
        print(f"{adl_cnt} entered successfully!")
        print("Script still running...")
        print("")
        
    def intentional_wait(self, time_allocated):
        time.sleep(time_allocated)
        
            
    def stop_driver(self):
        self.quit()