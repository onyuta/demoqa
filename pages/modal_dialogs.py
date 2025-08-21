from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.submenu_btns = WebElement(driver,'div:nth-child(3) > div > ul > li')
        self.icon_demoqa = WebElement(driver, '#app > header > a > img')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.small_close_btn = WebElement(driver,'#closeSmallModal')
        self.large_close_btn = WebElement(driver, '#closeLargeModal')







