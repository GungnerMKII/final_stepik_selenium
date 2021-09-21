def test_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    button = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Can't find 'add to basket' button"
