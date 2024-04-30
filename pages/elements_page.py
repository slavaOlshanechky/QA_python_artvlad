import time

from locators.element_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Piter Jackson')
        self.element_is_visible(self.locators.EMAIL).send_keys('piters@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('sdfsdf')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('cvxcv')
        self.element_is_visible(self.locators.SUBMIT).click()


time.sleep(5)
