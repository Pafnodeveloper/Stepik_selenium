from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_address.send_keys(email)
        pwd = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        pwd.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url == LoginPageLocators.LOGIN_URL, f"Login url is incorrect {url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"
