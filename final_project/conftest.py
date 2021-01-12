import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#language choosing is mandatory
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = None
    user_language = request.config.getoption("language")
    options = Options()
    #browser starting with selected parameters
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
