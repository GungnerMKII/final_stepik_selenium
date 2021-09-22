from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        # self.solve_quiz_and_get_code()

    def is_goods_in_basket(self):
        self.product_name_in_basket_should_be_correct()
        self.product_price_in_basket_should_be_correct()

    def product_name_in_basket_should_be_correct(self):
        message = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        goods_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message == goods_name, 'Product name is incorrect in basket'

    def product_price_in_basket_should_be_correct(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        goods_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_in_basket == goods_price, 'Product price is incorrect in basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeared"

