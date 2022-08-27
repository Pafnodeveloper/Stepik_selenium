from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    FINAL_PRICE = (By.CSS_SELECTOR, ".alertinner > p")
    SUCCESS_PRODUCT_NAME = (By.CLASS_NAME, "alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")

    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
