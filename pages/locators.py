from selenium.webdriver.common.by import By


# class MainPageLocators():
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    BASKET_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    