import allure

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class NewAddressPage:
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://a.testaddressbook.com/addresses/new'
        self._first_name_field_locator = (By.ID, 'address_first_name')
        self._last_name_field_locator = (By.ID, 'address_last_name')
        self._address1_field_locator = (By.ID, 'address_street_address')
        self._city_field_locator = (By.ID, 'address_city')
        self._zipcode_field_locator = (By.ID, 'address_zip_code')
        self._errors_explanation_locator = (By.XPATH, '//*[@id="error_explanation"]/h4')
        self._errors_list_locator = (By.XPATH, '//*[@id="error_explanation"]/ul')
        self._create_address_button_locator = (By.NAME, 'commit')

    @allure.step('Go to new address page')
    def get_page(self):
        self._driver.get(self._url)

    def get_errors_list(self):
        errors_container = self._driver.find_element(*self._errors_list_locator)
        errors = errors_container.find_elements(By.TAG_NAME, 'li')
        # errors = errors_container.find_elements_by_tag('li')
        return errors

    @allure.step('Fill in first name field')
    def fill_first_name_field(self, name):
        self._driver.find_element(*self._first_name_field_locator).send_keys(name)

    @allure.step('Fill in last name field')
    def fill_last_name_field(self, name):
        self._driver.find_element(*self._last_name_field_locator).send_keys(name)

    @allure.step('Fill in address1 field')
    def fill_address1_field(self, address):
        self._driver.find_element(*self._address1_field_locator).send_keys(address)

    @allure.step('Fill in city field')
    def fill_city_field(self, city):
        self._driver.find_element(*self._city_field_locator).send_keys(city)

    @allure.step('Fill in zip code field')
    def fill_zipcode_field(self, zipcode):
        self._driver.find_element(*self._zipcode_field_locator).send_keys(zipcode)

    @allure.step('Click on create address button')
    def click_create_address_button(self):
        self._driver.find_element(*self._create_address_button_locator).click()

    @allure.step('Check if errors list is displayed')
    def is_errors_list_displayed(self):
        try:
            self._driver.find_element(*self._errors_list_locator)
        except NoSuchElementException:
            return False
        return True

    def is_error_in_list(self, error):
        errors_list = self.get_errors_list()
        for e in errors_list:
            if e.text == error:
                return True
        return False

    @allure.step('Check if number of errors is correct')
    def is_error_number_correct(self, actual, expected):
        if actual == expected:
            return True
        else:
            allure.attach(self._driver.get_screenshot_as_png(), name='Errors number isn\'t correct',
                          attachment_type=AttachmentType.PNG)
            return False
