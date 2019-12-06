import pytest

from selenium import webdriver
from faker import Faker


# @pytest.fixture(scope='module', params=['chrome'])  # , 'firefox'])
@pytest.fixture(scope='module', params=['chrome', 'firefox'])
def driver(request, chrome_driver, firefox_driver):
    if request.param == 'chrome':
        driver = chrome_driver
    if request.param == 'firefox':
        driver = firefox_driver
    yield driver
    driver.close()


@pytest.fixture(scope='module')
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path='E:/Testing/WebDrivers/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope='module')
def firefox_driver():
    driver = webdriver.Firefox(executable_path='E:/Testing/WebDrivers/geckodriver.exe')
    return driver


@pytest.fixture
def fake_email():
    fake = Faker()
    return fake.email()


@pytest.fixture
def fake_name():
    fake = Faker()
    name = fake.name()
    first = ''
    last = ''
    for i in name:
        if i == ' ':
            break
        else:
            first += i
    last = name[len(first) + 1:]
    return first, last


@pytest.fixture
def fake_address():
    fake = Faker()
    return fake.address()
