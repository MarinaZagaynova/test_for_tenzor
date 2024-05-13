from selenium.webdriver.common.by import By


class ContactsLocators:
    contacts = [By.XPATH, "//div[@class='sbisru-Header']/div[2]/ul//a[@href='/contacts']"]
    logo_tenzor = [By.XPATH, "//a[@title='tensor.ru']/img[@alt='Разработчик системы СБИС — компания «Тензор»']"]
    force = [By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']"]
    force_text = [By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']/p[@class='tensor_ru-Index__card-title tensor_ru-pb-16']"]
    region = [By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"]
    partners = [By.XPATH, "//div[@title='СБИС - Самара']"]
    region_kamchatka = [By.XPATH, "//span[@title='Камчатский край']/span[.='41 Камчатский край']"]
    partners_kamchatka = [By.XPATH, "//div[@title='СБИС - Камчатка']"]