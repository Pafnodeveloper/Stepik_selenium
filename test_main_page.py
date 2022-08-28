import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link_on_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()


@pytest.mark.parametrize('link', [
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
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


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_good()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(strict=True, reason="Unexpected second alert")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_good()
    page.should_disappear()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()


if __name__ == "__main__":
    pytest.main()
