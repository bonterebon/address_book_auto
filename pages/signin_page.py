import allure

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class SigninPage:
    def __init__(self, driver):
        self._driver = driver
        self._email_field_locator = (By.ID, 'session_email')
        self._password_field_locator = (By.ID, 'session_password')
        self._submit_button_locator = (By.NAME, 'commit')
        self._alert_locator = (By.XPATH, '/html/body/div/div[1]')
        self._url = 'http://a.testaddressbook.com/sign_in'

    @allure.step('Go to sign in page')
    def get_page(self):
        self._driver.get(self._url)

    @allure.step('Fill in the email field')
    def fill_email_field(self, email):
        self._driver.find_element(*self._email_field_locator).send_keys(email)

    @allure.step('Fill in the password field')
    def fill_password_field(self, password):
        self._driver.find_element(*self._password_field_locator).send_keys(password)

    @allure.step('Press the sign in button')
    def press_signin_button(self):
        self._driver.find_element(*self._submit_button_locator).click()

    @allure.step('Check if alert is displayed')
    def is_alert_displayed(self):
        try:
            self._driver.find_element(*self._alert_locator)
        except NoSuchElementException:
            allure.attach(self._driver.get_screenshot_as_png(), name='Alert_not_displayed',
                          attachment_type=AttachmentType.PNG)
            return False
        return True
