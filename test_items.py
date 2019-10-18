import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_if_add_to_bag_exists(browser):
    browser.get(link)
    time.sleep(10)
    try:
        button = browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        assert False, "No such element"
