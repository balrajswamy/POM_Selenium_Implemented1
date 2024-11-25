from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
import os
from dotenv import load_dotenv

from tests.POM.AccountSuccessPage import AccountSuccessPage
from tests.POM.HomePage import HomePage
from tests.POM.RegisterPage import RegisterPage

# Load .env file
load_dotenv()
user_email = os.getenv("user_email")
user_pwd = os.getenv("user_pwd")
user_phone = os.getenv('user_phone')


@pytest.mark.usefixtures('setup_and_teardown')
class TestRegister:
    def generate_invalid_email_with_time_stamp(self):
        from datetime import datetime

        today = datetime.now().strftime("%d%m%Y%H%M%S")
        self.invalid_email = "test_software_"+str(today)+"@gmail.com"
        return self.invalid_email

    @allure.title("TestCase#1 to register with mandary fields!")
    @allure.description("Filling all the mandatory fields")
    def test_register_with_mandatory_fields(self):
        print("1. Running with mandatory fields")
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_menu()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Balaji")
        register_page.enter_last_name("Ramana")
        invalid_email = self.generate_invalid_email_with_time_stamp()
        register_page.enter_email(invalid_email)
        register_page.enter_telephone_num(user_phone)
        register_page.enter_password_first(user_pwd)
        register_page.enter_password_confirm(user_pwd)
        register_page.click_newsletter_yes_option_radio_button()
        register_page.click_privacy_agree_checkbox()
        register_page.click_continue_button()
        account_success_page = AccountSuccessPage(self.driver)
        expecting_success_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__contains__(expecting_success_heading)




    @allure.title("TestCase#2 to register with new email/passwords!")
    @allure.description("Filling all the mandatory fields with new email/passwords")
    def test_register_with_new_email_password(self):
        print("2. Running with new email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_menu()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Balaji")
        register_page.enter_last_name("Ramana")
        invalid_email = self.generate_invalid_email_with_time_stamp()
        register_page.enter_email(invalid_email)
        register_page.enter_telephone_num(user_phone)
        register_page.enter_password_first(user_pwd)
        register_page.enter_password_confirm(user_pwd)
        register_page.click_newsletter_yes_option_radio_button()
        register_page.click_privacy_agree_checkbox()
        register_page.click_continue_button()
        account_success_page = AccountSuccessPage(self.driver)
        expecting_success_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__contains__(expecting_success_heading)



    @allure.title("TestCase#3 to register with existing email/passwords!")
    @allure.description("Filling  with existing email/passwords")
    def test_register_with_existing_email(self):
        print("3. Running with existing email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_menu()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Balaji")
        register_page.enter_last_name("Ramana")
        register_page.enter_email(user_email)
        register_page.enter_telephone_num(user_phone)
        register_page.enter_password_first(user_pwd)
        register_page.enter_password_confirm(user_pwd)
        register_page.click_newsletter_yes_option_radio_button()
        register_page.click_privacy_agree_checkbox()
        register_page.click_continue_button()
        register_page.retrieve_already_registered_message()

        already_registered_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_already_registered_message().__contains__(already_registered_warning_message)




    @allure.title("TestCase#4 to without entering any fields!")
    @allure.description("Leaving as empty at fields and validating the input fields")
    def test_register_without_entering_any_fields(self):
        print("4. Running without entering email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        home_page.click_on_register_menu()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone_num("")
        register_page.enter_password_first("")
        register_page.enter_password_confirm("")
        register_page.click_continue_button()
        policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_warning_message().__contains__(policy_warning_message),"All the fields must be entered!"

        expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning_message().__eq__(
            expected_firstname_warning_message)

        expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning_message().__eq__(
            expected_lastname_warning_message)

        expected_email_warning_message="E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning_message().__eq__(
            expected_email_warning_message)

        text = register_page.retrieve_telephone_warning_message()
        expected_telephone_warning_message="Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning_message().__eq__(
            expected_telephone_warning_message)

        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning_message().__eq__(
            expected_password_warning_message)




