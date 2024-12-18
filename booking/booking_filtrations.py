from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def filteration(self, *filters_to_select):
        
        WebDriverWait(self.driver, 8).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'filterRow'))
        )
        filter_rows = self.driver.find_elements(By.CLASS_NAME, 'filterRow')
        # Loop through the desired filter
        for filter_name in filters_to_select:
            filter_found = False

            # Loop through all filter rows present
            for row in filter_rows:
                try:
                    # Find all list elements in filter
                    filter_list_elements = row.find_elements(By.TAG_NAME, 'li')

                    # Check each list element for matching filter text
                    for item in filter_list_elements:

                        # Get the text and remoev extra spaces
                        filter_text = item.text.strip()

                        # Check if filter to be selected in present in filter_text
                        if filter_name.lower() in filter_text.lower():

                            # Scroll to the filter element and click the checkbox
                            checkbox = item.find_element(By.TAG_NAME, 'input')
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                            self.driver.execute_script("arguments[0].click();", checkbox)
                            print(f"Selected {filter_name} filter!!")

                            # Exit the inner loop once the filter is found
                            filter_found=True
                            break
                        
                except NoSuchElementException:
                    print("Problem with selecting feature!!")
                    continue

            if not filter_found:
                print(f'Filter {filter_name} not found')

    def price_lowest(self):
        xpath='//*[@id="_Hlisting_area"]/div[2]/div/div[1]/ul/li[4]/span'
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        self.driver.find_element(By.XPATH, xpath).click()
        print("Sorted results by Lowest Price First!!")
        time.sleep(3)

    def budget_range(self, min_value, max_value):

        self.driver.implicitly_wait(10)
        # Send minimum budget value
        xpath='//*[@id="PRICE_BUCKET"]/div[2]/div/input[1]'
        # Wait until the element is loaded (after previous action)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        min_element = self.driver.find_element(By.XPATH, xpath)
        min_element.clear()
        min_element.send_keys(min_value)

        # Send maximum budget value
        xpath='//*[@id="PRICE_BUCKET"]/div[2]/div/input[2]'
        max_element = self.driver.find_element(By.XPATH, xpath)
        max_element.clear()
        max_element.send_keys(max_value)

        # Click on submit
        xpath='//*[@id="PRICE_BUCKET"]/div[2]/div/button'
        self.driver.find_element(By.XPATH, xpath).click()

        print(f"Set the Budget Range of {min_value} and {max_value}")
