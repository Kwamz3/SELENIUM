import os
import const
from selenium import webdriver



class Booking(webdriver.Chrome): 
    def __init__(self, driver_path= r"C:\Subdrive\chromedriver-win64", teardown= False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
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
            print("")
        else:
            self.quit()
            print(f"Expected title'{const.PAGE_TITLE}' but opened '{self.title}'")
            
    def stop_driver(self):
        self.quit()
        