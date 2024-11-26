from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
import os
from dotenv import load_dotenv

from tests.POM_OPTIMIZATION2.AccountSuccessPage import AccountSuccessPage
from tests.POM_OPTIMIZATION2.HomePage import HomePage
from tests.POM_OPTIMIZATION2.RegisterPage import RegisterPage

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
        register_page = home_page.navigate_to_register()
        invalid_email = self.generate_invalid_email_with_time_stamp()
        account_success_page = register_page.register_an_account("Balaji","Ramana",invalid_email,user_phone,user_pwd,user_pwd,"yes")

        expecting_success_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__contains__(expecting_success_heading)

    @allure.title("TestCase#2 to register with new email/passwords!")
    @allure.description("Filling all the mandatory fields with new email/passwords")
    def test_register_with_new_email_password(self):
        print("2. Running with new email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        register_page = home_page.click_on_register_menu()
        invalid_email = self.generate_invalid_email_with_time_stamp()
        account_success_page = register_page.register_an_account("Balaji", "Ramana", invalid_email, user_phone,
                                                                 user_pwd, user_pwd, "yes")

        expecting_success_heading = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__contains__(expecting_success_heading)

    @allure.title("TestCase#3 to register with existing email/passwords!")
    @allure.description("Filling  with existing email/passwords")
    def test_register_with_existing_email(self):
        print("3. Running with existing email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        register_page = home_page.click_on_register_menu()
        account_success_page = register_page.register_an_account("Balaji", "Ramana", user_email, user_phone,
                                                                 user_pwd, user_pwd, "yes")


        #register_page.retrieve_already_registered_message()

        already_registered_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_already_registered_message().__contains__(already_registered_warning_message)

    @allure.title("TestCase#4 to without entering any fields!")
    @allure.description("Leaving as empty at fields and validating the input fields")
    def test_register_without_entering_any_fields(self):
        print("4. Running without entering email/password")

        home_page = HomePage(self.driver)
        home_page.click_on_my_account_menu()
        register_page = home_page.click_on_register_menu()

        account_success_page = register_page.register_an_account("", "", "", "","", "", "")
        expected_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
        expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        expected_password_warning_message = "Password must be between 4 and 20 characters!"


        assert register_page.verify_all_warnings(\
                    expected_policy_warning_message,\
                    expected_firstname_warning_message,\
                    expected_lastname_warning_message,\
                    expected_email_warning_message,\
                    expected_telephone_warning_message,\
                    expected_password_warning_message\
                    )






