from pages.demoqa import DemoQa
import time
import pytest

#Декоратор для пропуска тестовой функции (reason необязательно)
@pytest.mark.skip
def test_decor(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    time.sleep(2)
    assert demo_qa_page.cards.check_count_elements(6)
    for element in demo_qa_page.cards.find_elements():
        assert element.text != ''