import pytest

from selenium import webdriver
from faker import Faker


@pytest.fixture(scope='module')
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path='E:/Testing/WebDrivers/chromedriver.exe', options=options)
    yield driver
    driver.close()


@pytest.fixture
def fake_email():
    fake = Faker()
    return fake.email()
