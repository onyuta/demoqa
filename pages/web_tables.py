from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)

        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_delete_row = WebElement(driver, '#delete-record-1 > svg > path')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.registration_form = WebElement(driver, 'modal-content', 'class')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')


