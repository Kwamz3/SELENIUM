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
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException



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
        
        # Wait for dropdown to stabilize after typing
        time.sleep(0.5)
        
        # Retry mechanism for stale element
        max_retries = 3
        for attempt in range(max_retries):
            try:
                first_result = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[contains(text(), '{place_to}')]")))
                first_result.click()
                print(f"Destination {place_to} entered successfully!")
                print("Script still running...")
                print("")
                break
            except StaleElementReferenceException:
                if attempt < max_retries - 1:
                    print(f"Stale element, retrying... (attempt {attempt + 1})")
                    time.sleep(0.3)
                else:
                    raise
        
    def select_dep_date(self, day:str, month:str, date:str, year:int):
        wait = WebDriverWait(self, 8)
        aria_label = f"{day}, {month} {date}, {year}"
        # month_check = self.find_element(By.XPATH, f"//div[normalize-space()='{month} {year}']")
        # user_date = f"{month} {year}"
        
        max_attempts = 12
        
        for attempt in range(max_attempts):
            try:
                select_dep_click = wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    f"div[aria-label='{aria_label}']"
                    ))) 
                    
                select_dep_click_2 = select_dep_click.find_element(
                    By.CSS_SELECTOR, 
                    "span.custom-day"
                    )
                select_dep_click_2.click()
                
                print(f"Date {aria_label} selected successfully")
                break
                
            except TimeoutException:
                try:
                    next_month = wait.until(EC.element_to_be_clickable((
                        By.CSS_SELECTOR, 
                        "button[title='Next month']"
                        )))
                    next_month.click()
                    print("Moved to next  month...")
                    
                except Exception as e:
                    print(f"Next month button not found: {e}")
                    break
        else:
            print(f"Could not find date: {aria_label}")            
    
    def select_ret_date(self, day:str, month:str, date:str, year:int):
        wait = WebDriverWait(self, 15)
        aria_label = f"{day}, {month} {date}, {year}"
        
        # Calendar should already be open after departure date selection
        # Add a small delay to let the calendar stabilize
        time.sleep(1.5)
        
        print(f"Attempting to select return date: {aria_label}")
        print("Script still running...")
        print("")
        
        max_attempts = 14  # Increased to handle more months if needed
        
        for attempt in range(max_attempts):
            try:
                # Locate the date element
                select_ret_click = wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    f"div[aria-label='{aria_label}']"
                    ))) 
                
                # Scroll into view
                self.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_ret_click)
                time.sleep(0.4)
                
                # Find and click the span inside it
                select_ret_click_2 = select_ret_click.find_element(
                    By.CSS_SELECTOR, 
                    "span.custom-day"
                    )
                
                # Use JavaScript click for reliability
                self.execute_script("arguments[0].click();", select_ret_click_2)
                
                print(f"Return date {aria_label} selected successfully")
                print("Script still running...")
                print("")
                break
                
            except (TimeoutException, NoSuchElementException):
                print(f"Date not found on current view (attempt {attempt + 1}), moving to next month...")
                # Date not found, try clicking next month
                try:
                    next_month = wait.until(EC.element_to_be_clickable((
                        By.CSS_SELECTOR, 
                        "button[title='Next month']"
                        )))
                    next_month.click()
                    time.sleep(0.7)  # Wait for calendar to update
                    
                except Exception as next_e:
                    print(f"Next month button not found: {next_e}")
                    break
                    
            except Exception as e:
                print(f"Unexpected error on attempt {attempt + 1}: {type(e).__name__} - {str(e)[:100]}")
                time.sleep(0.5)
                if attempt >= max_attempts - 1:
                    print(f"Failed after {max_attempts} attempts")
        else:
            print(f"Could not find return date: {aria_label}")
            raise Exception(f"Could not find return date: {aria_label} after {max_attempts} attempts")

        
    def select_passengers(self, adl_cnt: int, chd_cnt: int , inf_cnt: int):
        wait = WebDriverWait(self, 10)
        
        # Click on passenger selector dropdown
        adult_section = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            f"//a[@class='passenger-number']//span[contains(text(),'{adl_cnt}')]"
            )))  
        adult_section.click()
        time.sleep(0.5) 
        
        # Select adult count
        adult_section_3 = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            f"//div[@class='d-flex gap-4 mb-4']//div//a[@class='passenger-number']//span[contains(text(),'{chd_cnt}')]"
            )))  
        adult_section_3.click() 
        time.sleep(0.5) 
        
        # Select infant count
        adult_section_5 = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            f"(//span[contains(text(),'{inf_cnt}')])[3]"
            )))  
        adult_section_5.click() 
        time.sleep(0.5) 
        
        # Click Apply button
        apply_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            "//button[normalize-space()='Apply']"
            )))
        apply_button.click()
        
        time.sleep(1)
        
        # Click Search button (not Apply again)
        try:
            search_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, 
                "//button[normalize-space()='Search']"
                )))
            search_button.click()
        except TimeoutException:
            # If "Search" button not found, try looking for a submit button
            try:
                search_button = wait.until(EC.element_to_be_clickable((
                    By.XPATH, 
                    "//button[@type='submit']"
                    )))
                search_button.click()
            except TimeoutException:
                print("Search button not found, may already be on results page")
        
        tot_passengers = adl_cnt + chd_cnt + inf_cnt
        
        print(f"Passengers section completed successfully")
        print(f"{tot_passengers} Passengers in total: {adl_cnt} Adult(s), {chd_cnt} child(ren) and {inf_cnt}infant(s)")
        print("Script still running...")
        print("")
        
    def intentional_wait(self, time_allocated):
        print("Script run successfully!")
        print("Booking has been been completed successfully!")
        print(f"Script will auto-close in {time_allocated} seconds")
        time.sleep(time_allocated)
        
    def stop_driver(self):
        self.quit()