from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WikiPage(BasePage):
    _body_content = (By.ID, "bodyContent")
    _infobox = (By.CSS_SELECTOR, "table.infobox")
    _links = (By.TAG_NAME, "a")

    def get_body(self):
        return self.find_element(self._body_content)

    def get_infobox(self):
        return self.find_element(self._infobox)

    def get_body_links_as_list(self):
        list = []
        body = self.get_body()
        found_items_by_locator = body.find_elements(By.CSS_SELECTOR, 'a')
        for item in found_items_by_locator:
            if item:
                list.append(item.get_attribute("href"))
        return list
