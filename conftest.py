import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option(
    'prefs', {'intl.accept_languages': "es"})
browser = webdriver.Chrome(options=options)

language = request.config.getoption("language")

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language: en, es")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "es":
        print("\nstart chrome browser loc. 'es' for test..")
        browser = webdriver.Chrome()
    elif language == "en":
        print("\nstart firefox browser loc 'en' for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser language {} still is not implemented".format(language))
    yield browser
    print("\nquit browser..")
    browser.quit()


#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nquit browser..")
#    browser.quit()
