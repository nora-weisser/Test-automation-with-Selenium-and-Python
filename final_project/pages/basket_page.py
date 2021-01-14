from .locators import BasketLocators, BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def guest_can_go_to_basket_page(self):
        basket_page = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_page.click()

    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.PRODUCT_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def guest_can_see_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET)
