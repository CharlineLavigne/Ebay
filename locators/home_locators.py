from selenium.webdriver.common.by import By


class HomeLocators:

    search_box = "gh-ac"
    search_category = (By.CLASS_NAME, "gh-sb ")
    search_btn = (By.ID, "gh-btn")

    nb_search_result = (By.XPATH, "//h1[@class='srp-controls__count-heading']/span[1]")
    keyword_search_result = (By.XPATH, "//h1[@class='srp-controls__count-heading']/span[2]")

    nav_category = (By.LINK_TEXT, "Electronics")
    nav_sub_category = (By.LINK_TEXT, "Computers & Tablets")
    brands_carousel = (By.CSS_SELECTOR, ".b-guidancecard__link--noimg")
    electronics_nav_top_list = (By.XPATH, "//li[@data-currenttabindex='3'] //nav[1] //li")
    electro_home_audio_category = (By.CLASS_NAME, "b-guidancecard__title")


