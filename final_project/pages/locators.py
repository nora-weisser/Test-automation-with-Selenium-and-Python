from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_SELECTOR = (By.CLASS_NAME, ".col-sm-6.login_form")
    REGISTRATION_SELECTOR = (By.CLASS_NAME, ".col-sm-6.register_form")
