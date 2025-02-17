from base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC

class TensorPage(BasePage):
    """Главная страница Тензора"""
    PAGE_URL = Links.TENSOR_PAGE
    BLOCK_TITLE = ("xpath", "//p[text()='Сила в людях']")
    MORE_BUTTON = ("xpath", "(//a[text()='Подробнее'])[3]")

    def check(self):
        self.wait.until(EC.presence_of_element_located(self.BLOCK_TITLE))

    def go_to_about(self):
        self.click_button(self.MORE_BUTTON)
