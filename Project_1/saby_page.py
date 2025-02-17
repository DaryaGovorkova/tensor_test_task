from base_page import BasePage
from links import Links


class SabyPage(BasePage):
    """Главная страница Saby"""
    PAGE_URL = Links.HOST
    CONTACTS_BUTTON_LOCATOR = ("xpath", "//a[text()='Контакты']")
    DOWNLOAD_BUTTON = ("xpath", "//a[text()='Скачать локальные версии']")

    def go_to_contact(self):
        self.click_button(self.CONTACTS_BUTTON_LOCATOR)

    def go_to_download(self):
        self.click_button(self.DOWNLOAD_BUTTON)