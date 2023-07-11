from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

#def test_site_visit():
#    driver = webdriver.Chrome()
#    driver.get('https://demoqa.com/')
#    time.sleep(1)

#    try:
#        driver.find_element(By.CSS_SELECTOR, 'header > a > img')
#    except NoSuchElementException:
#        assert False
#    assert True

#def test_site_task_2():
#    driver = webdriver.Chrome()
#    driver.get('https://demoqa.com/')
#    time.sleep(2)

#    try:
#        driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > a > img')
#    except NoSuchElementException:
#        assert False
#    assert True


def test_site_task_3():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')


    try:
        button = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.home-body > div > div:nth-child(1)')
    except NoSuchElementException:
        assert False
    assert True

    button.click()
    time.sleep(3)
    assert driver.current_url == 'https://demoqa.com/elements'

    driver.quit()