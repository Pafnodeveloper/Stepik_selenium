import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    if len(browser_language) >= 2:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be entered and must contain minimum 2 letters")
    yield browser
    browser.quit()
