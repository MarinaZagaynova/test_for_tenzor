import pytest
from selenium import webdriver

import data
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage


@pytest.fixture(params=['chrome'])
def webpage(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    url = data.DataUrl.URL
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def contacts_page(webpage):
    contacts_page = ContactsPage(webpage)
    return contacts_page

@pytest.fixture(scope='function')
def about_page(webpage):
    about_page = AboutPage(webpage)
    return about_page

