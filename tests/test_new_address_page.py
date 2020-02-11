import random

import allure
import pytest

from pages import signin_page, new_address_page, addresses_page


@allure.feature('Add new address')
@allure.title('Invalid new address adding without any info')
@allure.description('Check that new address isn\'t created without mandatory fields and errors list are displayed')
def test_invalid_address_adding(driver, address_creation_errors):
    new_address = new_address_page.NewAddressPage(driver)
    addresses = addresses_page.AddressesPage(driver)
    signin = signin_page.SigninPage(driver)

    signin.authorise('olacamera@protonmail.com', '123')

    new_address.get_page()
    new_address.click_create_address_button()

    assert new_address.is_errors_list_displayed()


@allure.feature('Add new address')
@allure.title('Check if errors list is correct')
@allure.description('Check that errors list corresponds correctly to made mistakes')
@pytest.mark.parametrize('fname, lname, addr, city, zipcode, number_of_errors', [
    (' ', ' ', ' ', ' ', ' ', 5),
    ('first name', ' ', ' ', ' ', ' ', 4),
    ('first name', 'last name', ' ', ' ', ' ', 3),
    ('first name', 'last name', 'address', ' ', ' ', 2),
    ('first name', 'last name', 'address', random.randint(1000, 10000), ' ', 1)])
def test_errors_corresponding(driver, address_creation_errors, fname, lname, addr, city, zipcode, number_of_errors):
    signin = signin_page.SigninPage(driver)
    new_address = new_address_page.NewAddressPage(driver)

    # signin.authorise('olacamera@protonmail.com', '123')

    new_address.get_page()
    new_address.fill_first_name_field(fname)
    new_address.fill_last_name_field(lname)
    new_address.fill_address1_field(addr)
    new_address.fill_city_field(city)
    new_address.fill_zipcode_field(zipcode)
    new_address.click_create_address_button()

    errors_count = 0
    for e in address_creation_errors:
        if new_address.is_error_in_list(address_creation_errors.get(e)):
            errors_count += 1

    assert new_address.is_error_number_correct(errors_count, number_of_errors)



@allure.feature('Add new address')
@allure.title('Valid new address adding only with mandatory fields')
def test_valid_adding_with_mandatory_fields(driver, fake_name, fake_address, fake_city, fake_zipcode):
    signin = signin_page.SigninPage(driver)
    new_address = new_address_page.NewAddressPage(driver)
    addresses = addresses_page.AddressesPage(driver)

    # signin.authorise('olacamera@protonmail.com', '123')
    new_address.get_page()
    new_address.fill_first_name_field(fake_name[0])
    new_address.fill_last_name_field(fake_name[1])
    new_address.fill_address1_field(fake_address)
    new_address.fill_city_field(fake_city)
    new_address.fill_zipcode_field(fake_zipcode)
    new_address.click_create_address_button()

    addresses.get_page()
    assert addresses.is_address_in_table(fake_name[0], fake_name[1], fake_city)
