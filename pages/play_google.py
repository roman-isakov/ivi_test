from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GooglePlayPage(BasePage):
    _rating_locator = (By.CSS_SELECTOR, 'div.BHMmbe')

    def get_app_rating(self):
        return float(self.find_element(self._rating_locator).text)
