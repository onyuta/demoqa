from pages.radio_button import RadioButton
import pytest


#Декоратор позволяет пропускать тест-кейс исходя из условия (True, reason)
@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_2(browser):
    radio = RadioButton(browser)

    radio.visit()
    radio.yes_radio.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.impressive_radio.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio.no_radio.get_dom_attribute('class')


