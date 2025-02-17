import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def browser(request):
    options = Options()
    preferences = {
        'safebrowsing.enabled': True
    }
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()






