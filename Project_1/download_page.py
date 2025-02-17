from base_page import BasePage
from links import Links
import os
import requests

class DownloadPage(BasePage):
    """Страница загрузок Saby"""
    PAGE_URL = Links.DOWNLOAD_PAGE
    SETUP_BUTTON = ("xpath", "//a[@href='https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")

    def setup_saby_plugin(self):
        file_url = self.find_el(self.SETUP_BUTTON).get_attribute("href")
        response = requests.get(file_url)
        with open("plugin.exe", "wb") as file:
            file.write(response.content)

    def check_plugin(self):
        assert os.path.exists("plugin.exe") == True, "Файла не существует"

    def compare_size(self, size):
        file_size = os.path.getsize("plugin.exe")
        assert round(file_size/1048576, 2) == size, f"Размеры файлов не совпадают {file_size, size}"