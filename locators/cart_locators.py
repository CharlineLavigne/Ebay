from selenium.webdriver.common.by import By


class CartLocators:

    text_shopping_cart_empty = (By.XPATH, "//span[contains(text(), 'any items')]")
    btn_item_remove = (By.XPATH, "//button[@data-test-id='cart-remove-item']")
    search_box = (By.ID, "gh-ac")
    search_btn = (By.ID, "gh-btn")
    items_search_result = "s-item__link"
    btn_add_item_cart = (By.CSS_SELECTOR, ".x-atc-action a")
    item_quantity_select = (By.XPATH, "//select[@data-test-id='qty-dropdown']")

