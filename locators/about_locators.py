from selenium.webdriver.common.by import By


class AboutLocators:
    more = [By.XPATH, "//a[@href='/about']"]
    image_one = [By.XPATH, "//*[@id='container']/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img"]
    image_two = [By.XPATH, "//*[@id='container']/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img"]
    image_three = [By.XPATH, "//*[@id='container']/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img"]
    image_four = [By.XPATH, "//*[@id='container']/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img"]
