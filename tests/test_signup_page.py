from pages import signup_page, home_page
import pytest
import allure


@allure.title('Invalid sign up with used email')
@allure.description('Try to sign up with email, which is already in use')
def test_signup_with_used_email(chrome_driver):
    """Try to sign up with email, which is already in use"""
    signup = signup_page.SignupPage(chrome_driver)
    signup.get_page()
    signup.fill_email_field('olacamera@protonmail.com')
    signup.fill_password_field('123')
    signup.press_submit_button()
    home = home_page.HomePage(chrome_driver)
    assert not home.is_page_displayed()


@allure.title('Sign up with valid email and password')
@allure.description('Sign up with valid unused email and password')
def test_signup_with_valid_data(chrome_driver, fake_email):
    signup = signup_page.SignupPage(chrome_driver)
    signup.get_page()
    signup.fill_email_field(fake_email)
    signup.fill_password_field('123')
    signup.press_submit_button()
    home = home_page.HomePage(chrome_driver)
    assert home.is_page_displayed()
