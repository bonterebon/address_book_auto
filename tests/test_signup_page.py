from pages import signup_page, home_page
import pytest
import allure


@allure.title('Invalid sign up with used email')
@allure.description('Try to sign up with email, which is already in use')
@allure.feature('Sign up')
def test_signup_with_used_email(chrome_driver):
    signup = signup_page.SignupPage(chrome_driver)
    signup.get_page()
    signup.fill_email_field('olacamera@protonmail.com')
    signup.fill_password_field('123')
    signup.press_submit_button()
    home = home_page.HomePage(chrome_driver)
    assert not home.is_page_displayed()


@allure.title('Invalid sign up with empty fields')
@allure.description('Test that sign up doesn\'t occure if email and password fields empty')
@allure.feature('Sign up')
def test_signup_with_empty_fields(chrome_driver):
    signup = signup_page.SignupPage(chrome_driver)
    signup.get_page()
    signup.press_submit_button()
    home = home_page.HomePage(chrome_driver)
    assert not home.is_page_displayed()


@allure.title('Invalid sign up with empty email field')
@allure.description('Test that sign up doesn\'t occure if email field is empty')
@allure.feature('Sign up')
def test_signup_with_empty_email_field(chrome_driver, fake_email):
    signup = signup_page.SignupPage(chrome_driver)
    home = home_page.HomePage(chrome_driver)
    signup.get_page()
    signup.fill_password_field('123')
    signup.press_submit_button()
    assert not home.is_page_displayed()


@allure.title('Invalid sign up with empty password field')
@allure.description('Test that sign up doesn\'t occure if password field is empty')
@allure.feature('Sign up')
def test_signup_with_empty_password_field(chrome_driver, fake_email):
    signup = signup_page.SignupPage(chrome_driver)
    home = home_page.HomePage(chrome_driver)
    signup.get_page()
    signup.fill_email_field(fake_email)
    signup.press_submit_button()
    assert not home.is_page_displayed()


@allure.title('Sign up with valid email and password')
@allure.description('Sign up with valid unused email and password')
@allure.feature('Sign up')
def test_signup_with_valid_data(chrome_driver, fake_email):
    signup = signup_page.SignupPage(chrome_driver)
    signup.get_page()
    signup.fill_email_field(fake_email)
    signup.fill_password_field('123')
    signup.press_submit_button()
    home = home_page.HomePage(chrome_driver)
    assert home.is_page_displayed()
