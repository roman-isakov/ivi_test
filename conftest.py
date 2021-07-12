import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0, print_first_line=False).install())
    yield driver
    driver.quit()
