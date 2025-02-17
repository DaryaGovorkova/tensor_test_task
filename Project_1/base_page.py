from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 20, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL), message="Неверный адрес")

    def click_button(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_els(self, locator):
        return self.driver.find_elements(*locator)

    def find_el(self, locator):
        return self.driver.find_element(*locator)

    def get_list_window(self):
        list_of_tabs = self.driver.window_handles
        return list_of_tabs

    def switch(self, tab):
        self.driver.switch_to.window(self.get_list_window()[int(tab)])

    def get_title(self):
        return self.driver.title