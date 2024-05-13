from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def switch_to_page(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait(locator)
        redirected_url = self.driver.current_url
        return redirected_url

    def wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def get_width(self, locator):
        return self.driver.find_element(*locator).get_attribute("width")

    def get_height(self, locator):
        return self.driver.find_element(*locator).get_attribute("height")

    def get_title(self):
        return self.driver.title
