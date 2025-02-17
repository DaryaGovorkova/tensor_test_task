from base_page import BasePage
from links import Links


class AboutPage(BasePage):
    """Раздел: о компании"""
    PAGE_URL = Links.ABOUT_PAGE
    PICTURES = ("xpath", "//div[@class='tensor_ru-About__block3-image-wrapper']/img")

    def check_pictures(self):
        list_pictures = self.find_els(self.PICTURES)
        for i in range(1, len(list_pictures)):
            assert list_pictures[0].size == list_pictures[i].size, "Разные размеры картинок"
