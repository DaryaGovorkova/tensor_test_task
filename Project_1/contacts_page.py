from base_page import BasePage
from links import Links


class ContactsPage(BasePage):
    """"Страница с контактами Ярославской области"""
    PAGE_URL = Links.CONTACTS_PAGE
    TENSOR_BUTTON = ("xpath", "(//img[@alt='Разработчик системы Saby — компания «Тензор»'])[1]")
    REGION_BUTTON = ("xpath", "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']")
    PARTNERS_LIST = ("xpath", "//div[contains(@class, 'sbisru-Contacts-List__name')]")
    KAMCHATKA_BUTTON = ("xpath", "//span[text()='41 Камчатский край']")

    def go_to_tensor(self):
        self.click_button(self.TENSOR_BUTTON)

    def get_region(self, region):
        result = self.find_el(self.REGION_BUTTON).text
        assert region == result, f"Регионы не совпадают {region, result}"

    def check_partners(self):
        partners_list = self.find_els(self.PARTNERS_LIST)
        result = []
        for i in range(len(partners_list)):
            result.append(partners_list[i].text)
        assert len(result) != 0, "Список партнеров не найден"
        return result

    def change_region(self):
        self.click_button(self.REGION_BUTTON)
        self.click_button(self.KAMCHATKA_BUTTON)







