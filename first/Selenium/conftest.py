from time import sleep
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://google.com")
    yield driver
    driver.quit()


def test_that_depends_on_resource(browser):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys('Selenium')
    search_input.submit()
    sleep(2)


phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
del(phonebook["John"])
print(phonebook)
