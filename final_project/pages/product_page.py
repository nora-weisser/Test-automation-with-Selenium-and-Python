import pytest
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import AddToBasketLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_the_busket(self):
        button = self.browser.find_element(*AddToBasketLocators.ADD_TO_BASKET)
        button.click()

    def guest_can_see_correct_name(self):
        name_in_store = self.browser.find_element(*AddToBasketLocators.PRODUCT_NAME_IN_STORE).text
        name_in_basket = self.browser.find_element(*AddToBasketLocators.PRODUCT_NAME_IN_BASKET).text
        assert name_in_basket == name_in_store, "Product name is not the same"

    def guest_can_see_correct_price(self):
        price_in_store = self.browser.find_element(*AddToBasketLocators.PRODUCT_PRICE_STORE).text
        price_in_basket = self.browser.find_element(*AddToBasketLocators.PRODUCT_PRICE_BASKET).text
        assert price_in_store == price_in_basket, "Product price is not the same"

    def check_message_about_adding_to_basket(self):
        basket_message = self.browser.find_element(*AddToBasketLocators.SUCCESS_MESSAGE)
        assert self.is_not_element_present(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_on_product_page(self):
        assert self.is_not_element_present(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"








