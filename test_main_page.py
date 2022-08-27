import pytest
from pages.product_page import ProductPage


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


if __name__ == "__main__":
    pytest.main()
