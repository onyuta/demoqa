from pages.text_box import TextBox
import time


def test_filling_fields(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Edward C')
    text_box.c_address.send_keys('New York')
    text_box.sub_button.click_force()
    time.sleep(2)
    assert text_box.name_text.exist()
    assert text_box.address_text.exist()
    assert text_box.name_text.get_text() == 'Name:Edward C'
    assert text_box.address_text.get_text() == 'Current Address :New York'
