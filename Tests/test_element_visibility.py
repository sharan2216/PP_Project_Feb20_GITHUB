
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_element_visibility():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(3)
    try:
        button = driver.find_element(By.ID, "but2")
        assert button.is_displayed()
        if True:
            print("button is Visible and present in the Page")
    except Exception as e:
        print(e)


