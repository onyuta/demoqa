from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver,self.base_url)

        self.name = WebElement(driver, '#userName')
        self.c_address = WebElement(driver,'#currentAddress')
        self.sub_button = WebElement(driver, '#submit')
        self.name_text = WebElement(driver, '#name')
        self.address_text = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[2]', locator_type='xpath')



