from saby_page import SabyPage
from contacts_page import ContactsPage
from tensor_page import TensorPage
from about_page import AboutPage
from contacts_kam_page import ContactsKamPage
from download_page import DownloadPage

class TestPage:
    def setup_method(self):
        self.saby_page = SabyPage(self.driver)
        self.contacts_page = ContactsPage(self.driver)
        self.tensor_page = TensorPage(self.driver)
        self.about_page = AboutPage(self.driver)
        self.contacts_kam_page = ContactsKamPage(self.driver)
        self.download_page = DownloadPage(self.driver)

    def test_for_1script(self):
        self.saby_page.open()
        self.saby_page.go_to_contact()
        self.contacts_page.go_to_tensor()
        self.tensor_page.get_list_window()
        self.tensor_page.switch(tab=1)
        self.tensor_page.check()
        self.tensor_page.go_to_about()
        self.about_page.is_opened()
        self.about_page.check_pictures()

    def test_for_2script(self):
        self.saby_page.open()
        self.saby_page.go_to_contact()
        title_yar = self.contacts_page.get_title()
        self.contacts_page.get_region(region="Ярославская обл.")
        self.contacts_page.check_partners()
        partners_yar_list = self.contacts_page.check_partners()
        self.contacts_page.change_region()
        self.contacts_kam_page.is_opened()
        self.contacts_kam_page.get_region(region="Камчатский край")
        assert partners_yar_list != self.contacts_kam_page.check_partners(), "Список партнеров не изменился"
        assert self.contacts_kam_page.get_title() != title_yar, "Заголовок страницы не изменен"

    def test_for_3script(self):
        self.saby_page.open()
        self.saby_page.go_to_download()
        self.download_page.setup_saby_plugin()
        self.download_page.check_plugin()
        self.download_page.compare_size(size=10.42)