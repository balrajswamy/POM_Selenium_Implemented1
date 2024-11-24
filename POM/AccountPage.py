from selenium import webdriver
from selenium.webdriver.common.by import By

class AccountPage:

    edit_your_account_linktext = "Edit your account information"
    def __init__(self, driver):
        self.driver = driver
    def display_status_of_edit_account_link_text(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_linktext).is_displayed()
