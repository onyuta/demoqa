import time

from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa

def test_check_icon(browser):
    # browser.get('https://demoqa.com/')
    #
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Не найден')
    # else:
    #     print('Найден')

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()



