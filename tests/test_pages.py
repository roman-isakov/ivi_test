from selenium.common.exceptions import NoSuchElementException

from pages.google import GoogleSearchPage
from pages.play_google import GooglePlayPage
from pages.wiki import WikiPage


def test_amount_of_urls_in_pictures_tab(browser):
    google_page = GoogleSearchPage(browser)
    google_page.go_to_site()
    google_page.enter_text("ivi")
    google_page.submit_search()
    google_page.click_on_pictures_link()
    google_page.select_big_pictures()

    amount_of_matched_urls = google_page.get_amount_of_matching_pictures_urls("ivi.ru")

    assert amount_of_matched_urls >= 3


def test_ivi_wiki_page_has_ivi_link(browser):
    google_page = GoogleSearchPage(browser)
    google_page.go_to_site()
    google_page.enter_text("ivi")
    google_page.submit_search()

    for page in range(5):
        url = google_page.get_href_of_matching_text_url("https://ru.wikipedia.org/wiki/Ivi.ru")
        if url:
            browser.get(url)
            break
        else:
            if page == 5:
                raise NoSuchElementException
            else:
                google_page.go_to_next_page()

    wiki_page = WikiPage(browser)

    body_list_of_links = wiki_page.get_body_links_as_list()
    assert "https://www.ivi.ru/" in body_list_of_links


def test_google_play_mark(browser):
    google_page = GoogleSearchPage(browser)
    google_page.go_to_site()
    google_page.enter_text("ivi")
    google_page.submit_search()
    rating = 0
    for page in range(5):
        url = google_page.get_href_of_matching_text_url("https://play.google.com/")
        if url:
            rating = google_page.get_app_rating_for_url(sought_url="play.google.com")
            browser.get(url)
            break
        else:
            if page == 5:
                raise NoSuchElementException
            else:
                google_page.go_to_next_page()
    google_play_page = GooglePlayPage(browser)
    assert rating == google_play_page.get_app_raiting()
