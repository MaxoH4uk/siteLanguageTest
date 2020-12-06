import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, es, fr, etc")

@pytest.mark.parametrize('language', ["ru", "en-gb", "es", "fr"])
@pytest.fixture(scope="function")
def browser(request):
    site_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    options = Options()
    browser = webdriver.Chrome(options=options)
    link = f"http://selenium1py.pythonanywhere.com/{site_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    yield browser
    browser.quit()