import time
def test_find_add_to_basket_button(browser):
    button = browser.find_element_by_css_selector("button[type='submit']")
    assert button, "Button not found"