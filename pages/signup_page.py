import allure
import pytest

from selenium.webdriver.common.by import By


class SignupPage:
    EMAIL_FIELD_LOCATOR = (By.ID, 'user_email')

    def __init__(self, driver):
        self._driver = driver
        self._email_field_locator = (By.ID, 'user_email')
        self._password_field_locator = (By.ID, 'user_password')
        self._submit_button_locator = (By.NAME, 'commit')

    @allure.step('Go to Sign up page')
    def get_page(self):
        self._driver.get('http://a.testaddressbook.com/sign_up')

    @allure.step('Fill in the email field')
    def fill_email_field(self, email):
        self._driver.find_element(*self._email_field_locator).send_keys(email)

    @allure.step('Fill in the password field')
    def fill_password_field(self, password):
        self._driver.find_element(*self._password_field_locator).send_keys(password)

    @allure.step('Press the submit button')
    def press_submit_button(self):
        self._driver.find_element(*self._submit_button_locator).click()
