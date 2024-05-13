import data
from locators.about_locators import AboutLocators
from pages.base_page import BasePage


import allure


class AboutPage(BasePage):
    @allure.step("Нажимаем на кнопку Подробнее")
    def click_about(self):
        self.switch_to_page(AboutLocators.more)
        self.click_to_element(AboutLocators.more)

    @allure.step("Проверка открытия страицы О компании")
    def check_open_about(self):
        assert self.get_current_url() == data.DataUrl.TENZOR + data.DataUrl.ABOUT

    def check_image_width(self):
        assert self.get_width(AboutLocators.image_one) == self.get_width(AboutLocators.image_two) == self.get_width(
            AboutLocators.image_three) == self.get_width(AboutLocators.image_four)

    def check_image_height(self):
        assert self.get_height(AboutLocators.image_one) == self.get_height(AboutLocators.image_two) == self.get_height(
            AboutLocators.image_three) == self.get_height(AboutLocators.image_four)
