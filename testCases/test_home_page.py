import time

import pytest
from dotenv import load_dotenv
import os

from locators.home_locators import HomeLocators
from pageObjects.home_page import HomePage
from testCases.base_test import BaseTest
from utilities.customLogger import LogGen
from utilities.excelReader import ExcelReader


class TestHomePage(BaseTest):

    home = HomePage
    locator = HomeLocators
    base = BaseTest
    excelReader = ExcelReader
    excel_data_file = "./testData/DataEbay.xlsx"
    test_cases_file = "./testCases/testCases.xlsx"

    load_dotenv()
    logger = LogGen().get_logger("log Home Page")

    @pytest.fixture()
    def clear_input(self):
        self.home.clear_search_box(self)

    @pytest.mark.dependency()
    def test_load_home_page(self):
        self.base.open_page(self, os.getenv("BASE_URL"))
        page_url = self.driver.current_url
        if os.getenv("BASE_URL") == page_url and self.driver.title == "Electronics, Cars, Fashion, Collectibles & More | eBay":
            self.excelReader.write_test_results(self, self.test_cases_file, "Home Page", 2, 8, "PASS")
            self.excelReader.fill_color(self, self.test_cases_file, "Home Page", 2, 8, "C9F297")
            assert True
        else:
            self.excelReader.write_test_results(self, self.test_cases_file, "Home Page", 2, 8, "FAIL")
            self.excelReader.fill_color(self, self.test_cases_file, "Home Page", 2, 8, "F78D7B")
            assert False

    @pytest.mark.parametrize("row_excel_data", [1, 2, 3])
    @pytest.mark.dependency(depends=['TestHomePage::test_load_home_page'])
    def test_search_by_category(self, row_excel_data, clear_input):
        self.home.add_input_search_box(self, row_excel_data)
        self.home.select_search_category(self, row_excel_data)
        self.home.click_search_btn(self)

        if self.home.get_nb_search_result(self) is not None:
            assert True
        else:
            self.logger.error("Product results are not displayed or search keyword is not displayed in results")
            assert False

    @pytest.mark.regression
    def test_search_with_navbar(self):
        self.driver.back()
        self.home.hover_nav_category(self)
        time.sleep(2)
        self.home.click_nav_sub_category(self)
        self.home.scroll_by_brand(self)

        if self.home.check_visibility_electronic_home_audio_category(self) is True:
            assert True
        else:
            self.driver.save_screenshot("./screenshots/" + "test_search_with_navbar.png")
            self.logger.error("search with navbar has failed")
            assert False

        self.logger.info("**** Home Page test case is completed ****")




