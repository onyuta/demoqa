from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)

        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_delete_row = WebElement(driver, "span[title='Delete']")
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.registration_form = WebElement(driver, 'modal-content', 'class')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_edit_4 = WebElement(driver, '#edit-record-4 > svg')
        self.field_first_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]', 'xpath')
        self.btn_delete_row_4 = WebElement(driver, '#delete-record-4 > svg > path')
        #self.headers = WebElement(driver,'rt-resizable-header -cursor-pointer', 'class')
        self.header_1 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.header_2 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]','xpath')
        self.header_3 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]','xpath')
        self.header_4 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]','xpath')
        self.header_5 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]','xpath')
        self.header_6 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[6]','xpath')



