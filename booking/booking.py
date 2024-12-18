import booking.constants as const
from booking.booking_filtrations import BookingFiltration
from booking.booking_report import BookingReport
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from tabulate import tabulate
import os, time

class Booking(webdriver.Chrome):
    # Initialize method
    # A varaiable teardown to let the browser close or not
    def __init__(self, driver_path=const.DRIVER_PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path

        # Configure Chrome options to supress logs
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")    # Suppress error level logs
        chrome_options.add_argument("--disable-logging")
        # chrome_options.add_argument("--headless")  # Uncomment to Run in headless mode

        # Initialize Chromedriver with options
        super(Booking, self).__init__(options=chrome_options)
        self.implicitly_wait(10)
        self.maximize_window()

    # Automatically executes when interpreter finish with "with" method in run.py
    def __exit__(self, exc_type, exc, traceback):
        time.sleep(10)
        if self.teardown:
            self.quit()

    # Initially load and land on the first page
    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_sign_in_popup(self):
        try:
            if (self.find_element(By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div[2]/div')):
                print("Sign In pop up been detected!!")
                close_button = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div[2]/div/section/span')
                    ))
                close_button.click()
                print("Successfully closed Sign-In pop up!!")
        except NoSuchElementException:
            print("Sign-in pop up not found. Continuing!!!")           

    # Click on Accept Cookie button
    def allow_cookies(self):
        try:
            # Ensure the "Accept" button is visible and clickable
            accept_button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-banner"]/div[3]/div/div/div/div[2]/button'))
            )

            # Click the "Accept" button
            accept_button.click()

            print("Successfully Cliked on the Accep Cookie button!!!")
        except Exception as ex:
            print(f"An error occured in clicking the accept cookie button : {ex}")

    def change_currency(self, currency=None):

        # Click on currency dropdown
        xpath='//*[@id="SW"]/div[1]/div[1]/ul/li[6]/span'
        self.find_element(By.XPATH, xpath).click()

        # Enter the currency type
        xpath='//*[@id="SW"]/div[1]/div[1]/ul/li[6]/div/div[1]/input'
        currency_search = self.find_element(By.XPATH, xpath)
        currency_search.clear()
        currency_search.send_keys(currency)

        # Select the first one
        xpath='//*[@id="SW"]/div[1]/div[1]/ul/li[6]/div/div[2]/div'
        self.find_element(By.XPATH, xpath).click()

    def destination_to_go(self, place_to_go):

        # Selecting the destination input tag and entering the place_to_go input
        xpath='/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/label/input'
        self.find_element(By.XPATH, xpath).click()
        xpath='/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input'
        self.find_element(By.XPATH, xpath).send_keys(place_to_go)
        time.sleep(2)   # Wait to load the results

        # Click on the first destination from dropdown
        xpath='/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li[1]'
        self.find_element(By.XPATH, xpath).click()
 
    def date_selection(self, check_in_date, check_out_date):

        # Select Check-In and Check-Out dates
        self.find_element(By.CSS_SELECTOR, f'div[aria-label="{check_in_date}"]').click()
        self.find_element(By.CSS_SELECTOR, f'div[aria-label="{check_out_date}"]').click()

    def guest_selection(self, no_of_rooms, no_of_adults):

        # Number of Rooms
        # Click on Room input object and select the no. of rooms dropdown
        xpath='/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]'
        self.find_element(By.XPATH, xpath).click()
        self.implicitly_wait(5)
        xpath='//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li'
        rooms_dropdown = self.find_elements(By.XPATH, xpath)
        # Loop through dropdown to match the no_of_rooms input text
        for rooms in rooms_dropdown:
            if rooms.text.strip() == no_of_rooms:
                rooms.click()
                print(f'Selecting the number of rooms: {no_of_rooms}')
                break
        else:
            print('Input value of rooms doesnot match any value from the dropdown')

        # Number of Adults
        # Click on adults input object and select the no. of adults dropdown
        xpath='//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div'
        self.find_element(By.XPATH, xpath).click()
        self.implicitly_wait(5)
        xpath='//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/ul/li'
        adults_dropdown = self.find_elements(By.XPATH, xpath)
        # Loop through dropdown to match the no_of_adults input text
        for adults in adults_dropdown:
            if adults.text.strip() == no_of_adults:
                adults.click()
                print(f'Selecting the number of adults: {no_of_adults}')
                break
        else:
            print('Input value of adults doesnot match any value from the dropdown')

        # Apply the no_of_rooms and no_of_adults selection
        xpath='//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[2]/button'
        self.find_element(By.XPATH, xpath).click()

    def click_submit_button(self):

        # Submit the search entries
        xpath='//*[@id="hsw_search_button"]'
        self.find_element(By.XPATH, xpath).click()
        time.sleep(4)

    def apply_filteration(self):
        time.sleep(1)
        filters = BookingFiltration(driver=self)
        filters.price_lowest()
        filters.budget_range(
            min_value=input('Enter Minimum Budget Value: '),
            max_value=input('Enter Maximum Budget Value: ')
        )
        filters.filteration("Very Good: 3.5+", "Public transport within 2 km")
        time.sleep(2)
        
    def report_hotel_table(self):
        time.sleep(2)
        report = BookingReport(driver=self)
        collections = report.report_hotels()
        headers=["Hotel Name", "Hotel Location", "Hotel Rating", "Hotel Prices"]
        print(tabulate(collections, headers=headers, tablefmt="grid"))
