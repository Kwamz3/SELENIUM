import os
from selenium_start import const
from selenium import webdriver



class Booking(webdriver.Chrome): 
    def __init__(self, driver_path= r"C:\Subdrive\chromedriver-win64"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        
    def open_page(self):
        self.get(const.BASE_URL)
        self.maximize_window()