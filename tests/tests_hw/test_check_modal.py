from pages.modal_dialogs import ModalDialogs
import time

def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.small_modal_btn.exist()
    modal_dialogs.small_modal_btn.click()
    time.sleep(2)
    assert modal_dialogs.modal.exist()
    assert modal_dialogs.small_close_btn.exist()
    modal_dialogs.small_close_btn.click()
    time.sleep(2)
    assert not modal_dialogs.modal.exist()

    assert modal_dialogs.large_modal_btn.exist()
    modal_dialogs.large_modal_btn.click()
    time.sleep(2)
    assert modal_dialogs.modal.exist()
    assert modal_dialogs.large_close_btn.exist()
    modal_dialogs.large_close_btn.click()
    time.sleep(2)
    assert not modal_dialogs.modal.exist()


