from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SELECTOR), "There are no login panel"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SELECTOR), "There are no registration panel"


    def register_new_user(self, email, password, browser):
        email_adress = browser.find_element(*RegistrationPage.EMAIL)
        email_adress.send_keys(email)
        input_password = browser.find_element(*RegistrationPage.PASSWORD)
        input_password.send_keys(password)
        confirm_password = browser.find_element(*RegistrationPage.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        button_register = browser.find_element(By.CSS_SELECTOR, "#register_form .btn-primary")
        button_register.click()
