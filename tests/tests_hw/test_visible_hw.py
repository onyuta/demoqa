from pages.accordian_page import AccordianPage
import time

def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.section_one_content_first.visible()
    accordian_page.section_heading_first.click()
    time.sleep(2)
    assert not accordian_page.section_one_content_first.visible()

def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert not accordian_page.section_two_content_first.visible()
    assert not accordian_page.section_two_content_second.visible()
    assert not accordian_page.section_three_content_first.visible()




