from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    _search_field = (By.NAME, "q")  # строка ввода текста
    _picture_link = (By.CSS_SELECTOR, "[data-hveid=\"CAIQBQ\"]")  # Картинки
    _tools_button = (By.CSS_SELECTOR, "[jsname=\"I4bIT\"]")  # Инструменты
    _picture_size_dropdown = (By.CSS_SELECTOR, "[jsname=\"wLFV5d\"][aria-label=\"Размер\"]")  # Размер
    _big_pictures_option = (By.CSS_SELECTOR, "a.MfLWbb[aria-label=\"Большой\"]")  # Большие (картинки)
    _next_page_button = (By.ID, "pnnext")  # Большие (картинки)
    _picture_url = (
        By.CSS_SELECTOR, ".fxgdke")  # текст (URL) под картинкой (второй текст, там где пишется урезанный href)
    _link_on_search_page = (By.CSS_SELECTOR, "a[data-ved]")  # получаем ссылки на странице гугла
    _link_shortcut_block = (By.CSS_SELECTOR, "div.fG8Fp.uo4vr")  # получаем ссылки на странице гугла
    _link_shortcut_rating = (By.CSS_SELECTOR, "g-review-stars > span")  # получаем ссылки на странице гугла

    _url_block = (By.CLASS_NAME, "g")

    def enter_text(self, text):
        search_field = self.find_element(self._search_field)
        search_field.click()
        search_field.send_keys(text)

    def submit_search(self):
        search_field = self.find_element(self._search_field)
        search_field.send_keys(Keys.ENTER)

    def click_on_pictures_link(self):
        pictures_link = self.find_element(self._picture_link)
        pictures_link.click()

    def select_big_pictures(self):
        tools_button = self.find_element(self._tools_button)
        tools_button.click()

        sleep(0.2)  # не знаю как обойти. нужно для того, чтобы успело отрисоваться меню

        picture_size_dropdown = self.find_element(self._picture_size_dropdown)
        picture_size_dropdown.click()

        big_pictures_option = self.find_element(self._big_pictures_option)
        big_pictures_option.click()

    def get_amount_of_matching_pictures_urls(self, name_to_match: str):
        """
        Возвращаем число совпавших адресов у картинок по имени
        :param name_to_match:
        :return:
        """
        pictures_urls = self.find_elements(self._picture_url)
        matched_amount = 0
        for item in pictures_urls:
            if name_to_match in item.text:
                matched_amount += 1
        return matched_amount

    def go_to_next_page(self):
        next_page_button = self.find_element(self._next_page_button)
        next_page_button.click()

    def get_href_of_matching_text_url(self, sought_url):
        """
        Получаем текст параметра href

        :param sought_url:
        :return:
        """
        links = self.find_elements(self._link_on_search_page)

        for link in links:
            href = link.get_attribute("href")
            if href and sought_url in href:
                return href

    def get_app_rating_for_url(self, sought_url):
        # получаем все блоки с классом .g
        url_block = self.find_elements(self._url_block)
        for item in url_block:
            if item is not None:
                text = item.text
                if sought_url in text:
                    # делаем список
                    new_text = text.strip().splitlines()
                    # получаем последнюю строку
                    rating = new_text[-1].split(" ·")
                    # получаем рейтинг
                    rating_num = rating[0].replace("Рейтинг: ", "").replace(",", ".")
                    return float(rating_num)
