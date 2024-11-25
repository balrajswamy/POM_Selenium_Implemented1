import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import os
from dotenv import load_dotenv

from tests.POM.AccountPage import AccountPage
from tests.POM.HomePage import HomePage
from tests.POM.LoginPage import LoginPage

# Load .env file
load_dotenv()
user_email = os.getenv("user_email")
user_pwd = os.getenv("user_pwd")

@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    @allure.title("TestCase#1 to Test a Login with Valid Credentials")
    def test_Login_with_valid_credentials(self):
        print("1. Running with valid email/password!")
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_menu()
        login_page = LoginPage(self.driver)
        login_page.enter_into_email_address(user_email)
        login_page.enter_into_password(user_pwd)
        login_page.click_at_Login_button()
        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_account_link_text()

    def generate_invalid_email_with_time_stamp(self):
        from datetime import datetime

        today = datetime.now().strftime("%d%m%Y%H%M%S")
        invalid_email = "test_software_"+str(today)+"@gmail.com"
        return invalid_email

    @allure.title("TestCase#2 to Test a Login with InValid email and Valid password Credentials")
    def test_login_invalid_email_with_valid_password(self):
        print("2. Running with invalid_email_valid_password!")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_menu()
        login_page = LoginPage(self.driver)
        invalid_email = self.generate_invalid_email_with_time_stamp()
        login_page.enter_into_email_address(invalid_email)
        login_page.enter_into_password(user_pwd)
        login_page.click_at_Login_button()
        text_message = login_page.fetching_warning_message_expected_after_login()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.fetching_warning_message_expected_after_login().__contains__(expected_warning_message)

    @allure.title("TestCase#2 to Test a Login with Valid email with invalid password Credentials")
    def test_login_valid_email_with_invalid_password(self):
        print("3. Running with valid_email_invalid_password!")
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_menu()
        login_page = LoginPage(self.driver)

        login_page.enter_into_email_address(user_email)
        login_page.enter_into_password("12345")
        login_page.click_at_Login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.fetching_warning_message_expected_after_login().__contains__(expected_warning_message)

    @allure.title("TestCase#3 to Test a Login with without entering any Credentials")
    def test_login_without_entering_credentials(self):
        print("4. Running without entering credentials")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_login_menu()
        login_page = LoginPage(self.driver)

        login_page.enter_into_email_address("")
        login_page.enter_into_password("")
        login_page.click_at_Login_button()

        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.fetching_warning_message_expected_after_login().__contains__(expected_warning_message)
