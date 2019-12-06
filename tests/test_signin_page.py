import allure
import pytest

from pages import signin_page


@allure.feature('Sign in')
@allure.title('Invalid sign in with email: {email} and password: {password}. Expected result: alert is displayed')
@pytest.mark.parametrize('email,password,expected', [
    ('', '', True),
    ('test@gmail.com', '123', True),
    ('test@gmail.com', '', True),
    ('', '123', True),
    ('olatest@protonmail.com', '111', True)])
def test_invalid_signin(email, password, expected, driver):
    signin = signin_page.SigninPage(driver)
    signin.get_page()
    signin.fill_email_field(email)
    signin.fill_password_field(password)
    signin.press_signin_button()
    assert signin.is_alert_displayed() == expected


@allure.feature('Sign in')
@allure.title('Valid sign in')
@allure.description('Test that sign in works with valid password and email')
def test_valid_signin(driver):
    signin = signin_page.SigninPage(driver)
    signin.get_page()
    signin.fill_password_field('olacamera@protonmail.com')
    signin.fill_password_field('123')
    signin.press_signin_button()
    assert signin.is_alert_displayed()
