import allure

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class AddressesPage:
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://a.testaddressbook.com/addresses'
        self._new_address_link_locator = (By.CLASS_NAME, 'row justify-content-center')
        self._adresses_table_locator = (By.CLASS_NAME, 'table')
        self._addresses_table_xpath_locator = (By.XPATH, '/html/body/div/table/tbody')

    @allure.step('Go to addresses list page')
    def get_page(self):
        self._driver.get(self._url)

    def parse_table_rows(self):
        table = self._driver.find_element(*self._addresses_table_xpath_locator)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        return rows

    def is_address_in_table(self, first_name, last_name, city):
        addresses = self.parse_table_rows()
        for row in addresses:
            cols = row.find_elements_by_tag_name('td')
            if cols[0].text == first_name and cols[1].text == last_name and cols[2].text == city:
                return True
        return False
