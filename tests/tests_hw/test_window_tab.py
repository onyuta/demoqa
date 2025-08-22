from pages.links import Links
import time

def test_link_and_tab(browser):
    links_page = Links(browser)

    links_page.visit()
    assert links_page.home_link.exist()
    time.sleep(1)
    assert links_page.home_link.get_text() == 'Home'
    time.sleep(1)
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    time.sleep(1)
    assert len(browser.window_handles) == 1
    links_page.home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
