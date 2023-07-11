from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def test_5_hw():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
        driver.find_element(By.CSS_SELECTOR, '#password')
        driver.find_element(By.CSS_SELECTOR, '#login-button')

    except NoSuchElementException:
        assert False
    assert True

    time.sleep(4)

    print('Все элементы найдены')

