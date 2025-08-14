from components.components import WebElement
from pages.base_page import BasePage

class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.section_one_content_first = WebElement(driver, '#section1Content > p')
        self.section_heading_first = WebElement(driver, '#section1Heading')
        self.section_two_content_first = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_two_content_second = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_three_content_first = WebElement(driver, '#section3Content > p')


