import allure


@allure.suite('Проверка страницы Контакты')
class TestContactsPage:
    @allure.title('Проверка перехода к странице Тензор из вкладки Контакты и наличия блока "Сила в людях"')
    def test_open_tenzor(self, contacts_page):
        contacts_page.click_contacts()
        contacts_page.click_tenzor()
        contacts_page.check_open_tenzor()
        contacts_page.check_block_force()

    @allure.title('Проверка автоматического определения региона')
    def test_region(self, contacts_page):
        contacts_page.click_contacts()
        contacts_page.check_region()

    @allure.title('Проверка наличия партнеров')
    def test_partners(self, contacts_page):
        contacts_page.click_contacts()
        contacts_page.check_partners()

    @allure.title('Проверка смены региона')
    def test_change_region(self, contacts_page):
        contacts_page.click_contacts()
        contacts_page.click_change_region()
        contacts_page.check_change_partners()
        contacts_page.check_change_url()
        contacts_page.check_change_title()
