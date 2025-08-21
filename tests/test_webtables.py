from pages.web_tables import WebTables
import time

def test_web_tables(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    assert not web_tables_page.no_data.exist()

    while web_tables_page.btn_delete_row.exist():
        web_tables_page.btn_delete_row.click()

    time.sleep(2)
    assert web_tables_page.no_data.exist()