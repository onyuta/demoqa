from pages.alerts import Alerts
import time

def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.alert_5_sec_btn.exist()
    start_time = time.time()
    alert_page.alert_5_sec_btn.click()
    time.sleep(6)
    end_time = time.time()
    time_check = end_time - start_time
    assert 4.5 <= time_check <= 7
    alert_page.alert().accept()



