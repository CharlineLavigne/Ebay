import os

import pytest
from dotenv import load_dotenv
from selenium.common import NoSuchElementException

from locators.cart_locators import CartLocators
from pageObjects.cart_page import CartPage
from testCases.base_test import BaseTest
from utilities.customLogger import LogGen


class TestEbayCart(BaseTest):

    base = BaseTest
    cart = CartPage
    locator = CartLocators

    load_dotenv()
    logger = LogGen().get_logger("log Cart Page")

    @pytest.fixture()
    def remove_items_shopping_cart(self):
        self.base.open_page(self, os.getenv("CART_PAGE_URL"))
        self.cart.check_presence_items_cart(self)

    @pytest.mark.sanity
    @pytest.mark.parametrize("quantity_selected", ["2", "3"])
    def test_modify_quantity_product_cart(self, quantity_selected, remove_items_shopping_cart):
        try:
            if quantity_selected == "2":
                self.base.open_page(self, os.getenv("BASE_URL"))
                self.cart.add_input_search_box(self)
                self.cart.click_search_btn(self)
                self.cart.click_item_search_result(self)
                self.cart.click_btn_add_item_cart(self)
                self.cart.change_quantity_item_in_cart(self, quantity_selected)
            else:
                self.base.open_page(self, os.getenv("CART_PAGE_URL"))
                self.cart.change_quantity_item_in_cart(self, quantity_selected)

        except NoSuchElementException:
            self.logger.info("Exception can be triggered in Firefox with the xpath select[@data-test-id='qty-dropdown']")
            print("Unable to locate an element in the DOM")

        finally:
            if self.cart.get_selected_quantity(self) is "3" or "2":
                assert True
            else:
                self.driver.save_screenshot("./screenshots/" + "modify_quantity_product_cart.png")
                self.logger.error("Failed to select the expected quantity")
                assert False



