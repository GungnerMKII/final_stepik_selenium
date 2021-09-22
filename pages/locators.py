from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class GoodsPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOODS_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    GOODS_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    BASKET_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    