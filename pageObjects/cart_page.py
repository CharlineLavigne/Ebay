import os

from dotenv import load_dotenv
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage:

    load_dotenv()

    def check_presence_items_cart(self):
        try:
            btn_remove = self.driver.find_elements(*self.locator.btn_item_remove)
            for btn in range(len(btn_remove)):
                btn_remove[btn].click()
            return True

        except NoSuchElementException:
            print("The shopping cart is not empty")
            return False

    def add_input_search_box(self):
        search_box = self.driver.find_element(*self.locator.search_box)
        search_box.send_keys(os.getenv("SEARCH_INPUT"))

    def click_search_btn(self):
        self.driver.find_element(*self.locator.search_btn).click()

    def click_item_search_result(self):
        item = self.driver.find_elements(By.CLASS_NAME, "s-item__link")
        self.driver.execute_script("arguments[0].click();",item[1])

    def click_btn_add_item_cart(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(*self.locator.btn_add_item_cart).click()

    def change_quantity_item_in_cart(self, item_quantity):
        select = Select(self.driver.find_element(*self.locator.item_quantity_select))
        select.select_by_visible_text(item_quantity)

    def get_selected_quantity(self):
        select = Select(self.driver.find_element(*self.locator.item_quantity_select))
        return select.first_selected_option.text

