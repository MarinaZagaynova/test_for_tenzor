import allure


@allure.suite('Переход страницы О компании')
class TestAboutPage:
    @allure.title('Проверка перехода к странице "О компании" и одинаковой высоты/ширины в фотографиях')
    def test_open_about(self, about_page, contacts_page):
        contacts_page.click_contacts()
        contacts_page.click_tenzor()
        about_page.click_about()
        about_page.check_open_about()
        about_page.check_image_width()
        about_page.check_image_height()






