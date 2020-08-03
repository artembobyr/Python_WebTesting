import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
First
"""


def scroll():
    print("scroll")


def is_displayed():
    print("displayed")


# Get all items
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")
list_items = driver.find_elements(By.CLASS_NAME, "some")


def test_scroll_to_15_element():
    scroll_to_item(list_items[15])


def scroll_to_item(item):
    total_scroll_count = math.floor(len(list_items) / 10)
    # Go to page bottom
    for val in total_scroll_count:
        # Check for element is displayed
        if item.is_displayed():
            return True
        scroll()
    return False


"""
Second
"""


def get_product_by_id(id):
    print("get product name")


def get_extra_products(product_name):
    print("get list of extra products")


# Get list with product names
def get_product_name_list():
    product_name_list = []
    for index in range(10):
        product_name_list.append(get_product_by_id(index))
    return product_name_list


# Get list with all extra products
def get_all_extra_products():
    all_extra_products = []
    for index in get_product_name_list():
        all_extra_products.extend(get_extra_products(index))
    return all_extra_products


# Get elements frequency
def get_elements_frequency():
    # all_extra_products = ["Pita", "Salad", "Cheese", "Meat", "Ketchup", "Carrot", "Mustard", "Bread", "Meat", "Salad",
    #                       "Ketchup", "Cheese", "Bread", "Salad", "Meat"]
    frequency_products = dict()
    for item in get_all_extra_products():
        if not frequency_products.keys().__contains__(item):
            frequency_products[item] = 1
        else:
            frequency_products[item] = frequency_products.get(item) + 1

    for pair in frequency_products.items():
        print(pair)


get_elements_frequency()
