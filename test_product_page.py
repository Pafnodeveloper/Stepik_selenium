import pytest
import time
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "12345678QWERTYUIOP")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        book_price = page.get_product_price()
        product_name = page.get_real_product_name()
        product_name = product_name.text
        page.add_good()
        page.solve_quiz_and_get_code()
        total_price = page.get_total_price()
        product_in_basket = page.get_product_in_basket()
        product_in_basket = product_in_basket.text

        assert book_price in total_price, F"book costs {book_price} but total price is {total_price}"
        assert product_name in product_in_basket, f"{product_name} was ordered but {product_in_basket} was bought"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
