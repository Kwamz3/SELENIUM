import os
import const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class Booking(webdriver.Chrome): 
    def __init__(self, driver_path= r"C:\Subdrive\chromedriver-win64", teardown= False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
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
        
    def change_currency(self, currency=None):
            if str(self.find_element(By.CLASS_NAME, "country").text) != "GH | EN | GHS":
                currency_click = self.find_element(By.CLASS_NAME, "p-3")
                currency_click.click()
                print("Currency changed successfully!")
                print("Script still running...")
                print("")
                print(str(self.find_element(By.CLASS_NAME, "country").text))
            else:
                print("Currency already set to GHS!")
                print("Script still running...")
        
            
    def stop_driver(self):
        self.quit()
        