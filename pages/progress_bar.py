from components.components import WebElement
from pages.base_page import BasePage

class ProgressBar(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar/'
        super().__init__(driver,self.base_url)

        self.start_stop_btn = WebElement(driver, '#startStopButton')
        self.progress_bar = WebElement(driver, '#progressBar')