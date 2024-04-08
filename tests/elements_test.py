import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://www.google.com/')
    time.sleep(5)

    page.open()
    time.sleep(5)

