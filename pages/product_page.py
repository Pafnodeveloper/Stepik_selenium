from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_good(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def get_product_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRICE)
        book_price = book_price.text
        return book_price

    def get_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME)
        return product_name

    def get_real_product_name(self):
        real_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return real_product_name

    def get_total_price(self):
        total_price = self.browser.find_element(*ProductPageLocators.FINAL_PRICE)
        total_price = total_price.text
        return total_price
