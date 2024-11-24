from selenium.webdriver.common.by import By


class SearchPage:
    valid_hp_link_text = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def __init__(self,driver):
        self.driver = driver
    def display_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_hp_link_text).is_displayed()
    def no_product_error_message(self):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text
