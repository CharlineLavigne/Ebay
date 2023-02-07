from dotenv import load_dotenv

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:

    def add_input_search_box(self, row_tested):
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.locator.search_box)))
        input_data_search = self.excelReader.read_excel_data(self, self.excel_data_file, "DataEbay", row_tested)[0]
        search_box.send_keys(input_data_search)

    def select_search_category(self,row_tested):
        select = Select(self.driver.find_element(*self.locator.search_category))
        category_data = self.excelReader.read_excel_data(self, self.excel_data_file, "DataEbay", row_tested)[1]
        select.select_by_visible_text(category_data)

    def click_search_btn(self):
        self.driver.find_element(*self.locator.search_btn).click()

    def get_nb_search_result(self):
        return self.driver.find_element(*self.locator.nb_search_result).text

    def clear_search_box(self):
        self.driver.find_element(By.ID, self.locator.search_box).clear()

    def get_keyword_search_result(self):
        return self.driver.find_element(*self.locator.keyword_search_result).text

    def hover_nav_category(self):
        move = ActionChains(self.driver)
        nav_category = self.driver.find_element(*self.locator.nav_category)
        move.move_to_element(nav_category).perform()

    def click_nav_sub_category(self):
        self.driver.find_element(*self.locator.nav_sub_category).click()

    def scroll_by_brand(self):
        scroll = ActionChains(self.driver)
        origin = ScrollOrigin.from_element(self.driver.find_elements(*self.locator.brands_carousel)[0], 0, 0)
        scroll.scroll_from_origin(origin, 100, 0).pause(0.2).perform()

    def get_text_last_electronic_top_category(self):
        electro_top_category = self.driver.find_elements(*self.locator.electronics_nav_top_list)
        return electro_top_category[len(electro_top_category) - 1].text

    def check_visibility_electronic_home_audio_category(self):
        return self.driver.find_elements(*self.locator.electro_home_audio_category)[0].is_displayed()
