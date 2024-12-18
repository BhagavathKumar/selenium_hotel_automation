# This file is responsible for creating a report of the hotels
# That are shown after using certain filters, their rating and price.

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
import time

class BookingReport:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def report_hotels(self):
        time.sleep(4)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(4)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(4)

        class_name='listingRowOuter.hotelTileDt.makeRelative'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        hotel_list = self.driver.find_elements(By.CLASS_NAME, class_name)
        collection = []
        self.driver.implicitly_wait(5)
        for hotels in hotel_list:
            hotel_name = hotels.find_element(By.ID, 'hlistpg_hotel_name').text
            hotel_location = hotels.find_element(
                By.CLASS_NAME, 'persuasion__item.pc__locationPerNew'
                ).text.split(sep='|')[0]
            hotel_rating = hotels.find_element(By.XPATH, '//*[@id="hlistpg_hotel_user_rating"]').text
            hotel_price = hotels.find_element(By.ID, 'hlistpg_hotel_shown_price').text
            collection.append(
                [hotel_name, hotel_location, hotel_rating, hotel_price]
            )
        return collection
        
