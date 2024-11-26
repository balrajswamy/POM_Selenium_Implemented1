from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.POM_OPTIMIZATION2.LoginPage import LoginPage
from tests.POM_OPTIMIZATION2.RegisterPage import RegisterPage
from tests.POM_OPTIMIZATION2.SearchPage import SearchPage


class HomePage():
    search_box_field_name = "search"
    search_button_xpath = '//button[contains(@class,"btn-default")]'
    my_account_drop_menu_xpath = '//span[text()="My Account"]'
    login_menu_link_text = 'Login'
    register_menu_link_text = 'Register'

    def __init__(self, driver):
        self.driver = driver

    def enter_product_name_into_search_box(self,product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def click_on_my_account_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_drop_menu_xpath).click()
    def click_on_login_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.login_menu_link_text).click()
        return LoginPage(self.driver)

    def navigate_login(self):
        self.click_on_my_account_menu()
        return self.click_on_login_menu()

    def click_on_register_menu(self):
        self.driver.find_element(By.LINK_TEXT,self.register_menu_link_text).click()
        return RegisterPage(self.driver)

    def navigate_to_register(self):
        self.click_on_my_account_menu()
        return self.click_on_register_menu()


    def search_for_a_product(self,product_name):
        self.enter_product_name_into_search_box(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)


