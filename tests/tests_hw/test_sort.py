from pages.web_tables import WebTables
import time

def test_sort_columns(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    assert web_tables_page.header_1.exist()
    web_tables_page.header_1.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_1.get_dom_attribute('class')

    assert web_tables_page.header_2.exist()
    web_tables_page.header_2.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_2.get_dom_attribute('class')

    assert web_tables_page.header_3.exist()
    web_tables_page.header_3.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_3.get_dom_attribute('class')

    assert web_tables_page.header_4.exist()
    web_tables_page.header_4.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_4.get_dom_attribute('class')

    assert web_tables_page.header_5.exist()
    web_tables_page.header_5.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_5.get_dom_attribute('class')

    assert web_tables_page.header_6.exist()
    web_tables_page.header_6.click()
    time.sleep(2)
    assert '-sort-asc' in web_tables_page.header_6.get_dom_attribute('class')






