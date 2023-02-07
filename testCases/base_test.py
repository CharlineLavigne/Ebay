class BaseTest:

    def open_page(self, url):
        self.logger.info("**** Test case has started ****")
        self.driver.get(url)
        self.driver.maximize_window()