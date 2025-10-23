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
        month_check = self.find_element(By.XPATH, f"//div[normalize-space()='{month} {year}']")
        user_date = f"{month} {year}"
        
                correct_month = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[@class='date-label visible.{date}']")))
        # try:
        #     if month_check == user_date:
        #         correct_month = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[@class='date-label visible.{date}']")))
                
                
                
                # next_month = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "button[title='Next month']")))
                # next_month_2 = wait.until(EC.element_to_be_clickable(next_month))
                # next_month_2.click()
                
        
        # select_dep_click = wait.until(EC.presence_of_element_located((
        #     By.CSS_SELECTOR, 
        #     f"div[aria-label='{aria_label}']"
        #     )))
       
        # select_dep_click_2 = select_dep_click.find_element(By.CSS_SELECTOR, "span.custom-day")
        # select_dep_click_2.click()
        # print(f"Departure date {aria_label} entered successfully!")
        # print("Script still running...")
        # print("")
    
    
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

        
    def select_passengers(self, adl_cnt: int, chd_cnt: int , inf_cnt: int):
        wait = WebDriverWait(self, 10)
        adult_section = wait.until(EC.presence_of_element_located((
            By.XPATH, 
            f"//a[@class='passenger-number']//span[contains(text(),'{adl_cnt}')]"
            )))  
        adult_section_2 = wait.until(EC.element_to_be_clickable(adult_section))
        adult_section_2.click()
        time.sleep(0.5) 
        
        adult_section_3 = wait.until(EC.presence_of_element_located((
            By.XPATH, 
            f"//div[@class='d-flex gap-4 mb-4']//div//a[@class='passenger-number']//span[contains(text(),'2')]"
            )))  
        # f"//a[@class='passenger-number']//span[contains(text(),'{adl_cnt}')]"
        adult_section_4 = wait.until(EC.element_to_be_clickable(adult_section_3))
        adult_section_4.click() 
        time.sleep(0.5) 
        
        adult_section_5 = wait.until(EC.presence_of_element_located((
            By.XPATH, 
            f"(//span[contains(text(),'{inf_cnt}')])[3]"
            )))  
        adult_section_6 = wait.until(EC.element_to_be_clickable(adult_section_5))
        adult_section_6.click() 
        time.sleep(0.5) 
        
        apply_button = wait.until(EC.presence_of_element_located(((
            By.XPATH, 
            "//button[normalize-space()='Apply']"
            ))))
        apply_button_2 = wait.until(EC.element_to_be_clickable(apply_button))
        apply_button_2.click()
        
        time.sleep(0.5)
        
        search_button = wait.until(EC.presence_of_element_located((
            By.XPATH, 
            "//button[normalize-space()='Apply']"
            )))
        search_button_2 = wait.until(EC.element_to_be_clickable(search_button))
        search_button_2.click()
        
        tot_passengers = adl_cnt + chd_cnt + inf_cnt
        
        print(f"Passengers section completed successfully")
        print(f"{tot_passengers} Passengers in total: {adl_cnt} Adult(s), {chd_cnt} child(ren) and {inf_cnt}infant(s)")
        print("Script still running...")
        print("")
        
    def intentional_wait(self, time_allocated):
        time.sleep(time_allocated)
        
            
    def stop_driver(self):
        self.quit()