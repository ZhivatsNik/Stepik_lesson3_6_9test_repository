
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# функция вызывает фикстуру browser как параметр
def test_get_basket_button(browser):
    browser.get(link)
# указал 10 секунд времени, при 30 можно свихнуться:)
    time.sleep(10)
    browser.find_element_by_css_selector("#add_to_basket_form button")
    assert True
