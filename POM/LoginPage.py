from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_Login import user_email


class LoginPage:
    email_address_xpath = "//input[@id='input-email']"
    password_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"

    warning_message_xpath = '//div[@id="account-login"]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def enter_into_email_address(self, email_address):
        self.driver.find_element(By.XPATH, self.email_address_xpath).click()
        self.driver.find_element(By.XPATH, self.email_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_address_xpath).send_keys(email_address)

    def enter_into_password(self,user_pwd):
        self.driver.find_element(By.XPATH,self.password_xpath).click()
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(user_pwd)

    def click_at_Login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def fetching_warning_message_expected_after_login(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text



