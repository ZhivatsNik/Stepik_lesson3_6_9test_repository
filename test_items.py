
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

language = request.config.getoption("language")

def get_basket_button():
    browser.get(link)
    add_to_basket_button = browser.find_element_by_css_selector("#add_to_basket_form button").text
    assert add_to_basket_button == 'Add to basket', f'Кнопка содержит текст {add_to_basket_button}'

