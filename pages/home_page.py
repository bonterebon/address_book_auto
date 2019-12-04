import allure

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


class HomePage:
    def __init__(self, driver):
        self._driver = driver
        self._username = (By.CLASS_NAME, 'navbar-text')

    def get_page(self):
        self._driver.get('http://a.testaddressbook.com/')

    def is_page_displayed(self):
        try:
            self._driver.find_element(*self._username)
        except NoSuchElementException:
            allure.attach(self._driver.get_screenshot_as_png(), name='Sign up failed',
                          attachment_type=AttachmentType.PNG)
            return False
        return True
