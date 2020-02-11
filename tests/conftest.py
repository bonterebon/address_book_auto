import random
import pytest
import allure

from selenium import webdriver
from faker import Faker


# @pytest.fixture(scope='module', params=['chrome', 'firefox'])
# def driver(request, chrome_driver, firefox_driver):
#     if request.param == 'chrome':
#         driver = chrome_driver
#     if request.param == 'firefox':
#         driver = firefox_driver
#     yield driver
#     driver.close()


@pytest.fixture(scope='module', params=['chrome'], autouse=True)
def driver(request, chrome_driver):
    if request.param == 'chrome':
        driver = chrome_driver
    elif request.param == 'firefox':
        driver = firefox_driver
    else:
        print('Only chrome and firefox are supported')
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


@pytest.fixture
def fake_city():
    cities = ['Toronto', 'Montreal', 'Calgary', 'Edmonton', 'Ottawa', 'Vancouver', 'Winnipeg', 'Halifax']
    return cities[random.randint(0, len(cities) - 1)]


@pytest.fixture
def fake_zipcode(fake_address):
    return fake_address[-5:]


@pytest.fixture
def address_creation_errors():
    errors = {
        'firstname_error': 'First name can\'t be blank',
        'lastname_error': 'Last name can\'t be blank',
        'address_error': 'Address1 can\'t be blank',
        'city_error': 'City can\'t be blank',
        'zip_error': 'Zip code can\'t be blank'
    }
    return errors
