from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
import pytest
from tests.POM.HomePage import HomePage
from tests.POM.SearchPage import SearchPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestSearch:
    @allure.title("TestCase#1 to Search a valid product!")
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_name_into_search_box("HP")
        home_page.click_on_search_button()

        search_page = SearchPage(self.driver)
        search_page.display_status_of_valid_product()


    @allure.title("TestCase#2 to Search a Invalid product!")
    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_name_into_search_box("Honda")
        home_page.click_on_search_button()

        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.no_product_error_message().__eq__(expected_text)



    @allure.title("TestCase#3 to Search without entering any valid product!")
    def test_search_without_entering_any_product_input(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_name_into_search_box("")
        home_page.click_on_search_button()

        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.no_product_error_message().__eq__(expected_text)


