from selenium.webdriver.common.by import By

from tests.POM_OPTIMIZATIONS.AccountSuccessPage import AccountSuccessPage
from tests.test_Login import user_email


class RegisterPage:
    first_name_xpath = "//input[@name='firstname']"
    last_name_xpath = "//input[@name='lastname']"
    email_xpath = "//input[@name='email']"
    telephone_xpath = "//input[@name='telephone']"
    password_first_xpath = "//input[@name='password']"
    confirm_password_xpath = "//input[@name='confirm']"
    newsletter_radio_button_xpath = "//input[@name='newsletter' and @value = '1']"
    privacy_agree_xpath = "//input[@name='agree' and @value = '1']"
    continue_button_xpath = "//input[@value='Continue']"
    already_registered_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = '//input[@name="firstname"]/following-sibling::div'
    last_name_warning_message_xpath = '//input[@name="lastname"]/following-sibling::div'
    email_warning_message_xpath = '//input[@name="email"]/following-sibling::div'
    telephone_warning_message_xpath = '//input[@name="telephone"]/following-sibling::div'
    password_warning_message_xpath = '//input[@name="password"]/following-sibling::div'


    def __init__(self, driver):
        self.driver = driver



    def enter_first_name(self, first_name_txt):
        self.driver.find_element(By.XPATH, self.first_name_xpath).click()
        self.driver.find_element(By.XPATH, self.first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(first_name_txt)

    def enter_last_name(self, last_name_txt):
        self.driver.find_element(By.XPATH, self.last_name_xpath).click()
        self.driver.find_element(By.XPATH, self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(last_name_txt)

    def enter_email(self, email_txt):
        self.driver.find_element(By.XPATH, self.email_xpath).click()
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email_txt)

    def enter_telephone_num(self,telephone_num):
        self.driver.find_element(By.XPATH, self.telephone_xpath).click()
        self.driver.find_element(By.XPATH, self.telephone_xpath).clear()
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone_num)

    def enter_password_first(self,password_first_txt):
        self.driver.find_element(By.XPATH, self.password_first_xpath).click()
        self.driver.find_element(By.XPATH, self.password_first_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_first_xpath).send_keys(password_first_txt)

    def enter_password_confirm(self,password_confirm_txt):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).click()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password_confirm_txt)

    def click_newsletter_yes_option_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_button_xpath).click()

    def click_privacy_agree_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_agree_xpath).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def register_an_account(self, first_name_txt,last_name_txt,email_txt,telephone_num,password_first_txt,password_confirm_txt,yes_or_no):
        self.enter_first_name(first_name_txt)
        self.enter_last_name(last_name_txt)
        self.enter_email(email_txt)
        self.enter_telephone_num(telephone_num)
        self.enter_password_first(password_first_txt)
        self.enter_password_confirm(password_confirm_txt)
        if yes_or_no == "yes":
            self.click_newsletter_yes_option_radio_button()
            self.click_privacy_agree_checkbox()
        return self.click_continue_button()

    def retrieve_already_registered_message(self):
        return self.driver.find_element(By.XPATH, self.already_registered_warning_message_xpath).text

    def retrieve_privacy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_warning_message_xpath).text
    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_message_xpath).text
    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_message_xpath).text

    def retrieve_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_warning_message_xpath).text


    def verify_all_warnings(self, expected_policy_warning_message,\
                            expected_firstname_warning_message,
                            expected_lastname_warning_message,\
                            expected_email_warning_message,\
                            expected_telephone_warning_message,\
                            expected_password_warning_message):
        """

        :param expected_policy_warning_message:
        :param expected_firstname_warning_message:
        :param expected_lastname_warning_message:
        :param expected_email_warning_message:
        :param expected_telephone_warning_message:
        :param expected_password_warning_message:
        :return:

        expected_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_warning_message().__contains__(expected_policy_warning_message),"All the fields must be entered!"

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

        """
        actual_expected_policy_warning_message = self.retrieve_privacy_warning_message()
        actual_expected_firstname_warning_message = self.retrieve_first_name_warning_message()
        actual_expected_lastname_warning_message = self.retrieve_last_name_warning_message()
        actual_expected_email_warning_message = self.retrieve_email_warning_message()
        actual_expected_telephone_warning_message = self.retrieve_telephone_warning_message()
        actual_expected_password_warning_message = self.retrieve_password_warning_message()

        status = False
        if expected_policy_warning_message.__contains__(actual_expected_policy_warning_message):
            if expected_firstname_warning_message.__eq__(actual_expected_firstname_warning_message):
                if expected_lastname_warning_message.__eq__(actual_expected_lastname_warning_message):
                    if expected_email_warning_message.__eq__(actual_expected_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_expected_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_expected_password_warning_message):
                                status = True
        return status
