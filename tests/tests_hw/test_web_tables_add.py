from pages.web_tables import WebTables
import time

def test_web_tables(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    assert web_tables_page.btn_add.exist()
    web_tables_page.btn_add.click()
    time.sleep(2)
    assert web_tables_page.registration_form.exist()
    time.sleep(2)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    assert web_tables_page.registration_form.exist()
    web_tables_page.first_name.send_keys('Testina')
    web_tables_page.last_name.send_keys('Testova')
    web_tables_page.user_email.send_keys('tttttttt@tttttt.tt')
    web_tables_page.age.send_keys('18')
    web_tables_page.salary.send_keys('1000000')
    web_tables_page.department.send_keys('Testers')
    time.sleep(2)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    assert not web_tables_page.registration_form.exist()






