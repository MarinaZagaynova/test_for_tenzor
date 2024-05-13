import data
from locators.contacts_locator import ContactsLocators
from pages.base_page import BasePage
import allure


class ContactsPage(BasePage):

    @allure.step("Нажимаем на кнопку Контакты")
    def click_contacts(self):
        self.click_to_element(ContactsLocators.contacts)

    @allure.step("Нажимаем на баннер Тензор")
    def click_tenzor(self):
        self.click_to_element(ContactsLocators.logo_tenzor)

    @allure.step("Проверяем открытие страницы Тензор")
    def check_open_tenzor(self):
        assert self.switch_to_page(ContactsLocators.force) == data.DataUrl.TENZOR

    @allure.step("Проверяем наличие блока Сила в людях")
    def check_block_force(self):
        assert self.get_text_from_element(ContactsLocators.force_text) == "Сила в людях"

    @allure.step("Проверяем автоматическое определение региона")
    def check_region(self):
        assert self.get_text_from_element(ContactsLocators.region) == data.region

    @allure.step("Проверяем наличие партнеров")
    def check_partners(self):
        assert self.get_text_from_element(ContactsLocators.partners) == data.partners

    @allure.step("Меняем регион на камчатский край")
    def click_change_region(self):
        self.click_to_element(ContactsLocators.region)
        self.click_to_element(ContactsLocators.region_kamchatka)

    @allure.step("Проверяем изменение партнеров")
    def check_change_partners(self):
        assert self.get_text_from_element(ContactsLocators.partners_kamchatka) == "СБИС - Камчатка"

    @allure.step("Проверяем изменение url")
    def check_change_url(self):
        assert self.get_current_url() == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"

    @allure.step("Проверяем изменение title")
    def check_change_title(self):
        assert self.get_title() == "СБИС Контакты — Камчатский край"



