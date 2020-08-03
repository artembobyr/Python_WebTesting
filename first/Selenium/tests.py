from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_url = "https://google.com"

# def find_element(self, locator, time=10):
#     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
#                                                   message=f"Can't find element by locator {locator}")
#
# def find_elements(self, locator, time=10):
#     return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
#                                                   message=f"Can't find elements by locator {locator}")

# def test_input_selenium():
#     search_input = driver.find_element_by_name('q')
#     search_input.send_keys('Selenium')
#     search_input.submit()
#     # return self.driver.get(self.base_url)


# class TestResource:
# def test_that_depends_on_resource(driver):
#     search_input = driver.find_element_by_name('q')
#     search_input.send_keys('Selenium')
#     search_input.submit()
