def test_check_add_to_card_displayed(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button, 'button is displayed'
