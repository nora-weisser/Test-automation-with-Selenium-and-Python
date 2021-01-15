from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_SELECTOR = (By.CLASS_NAME, ".col-sm-6.login_form")
    REGISTRATION_SELECTOR = (By.CLASS_NAME, ".col-sm-6.register_form")


class AddToBasketLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info p:first-child strong")
    PRODUCT_PRICE_STORE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")

class RegistrationPage():
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
