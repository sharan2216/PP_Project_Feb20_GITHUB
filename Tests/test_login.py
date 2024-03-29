import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def test_login_with_valid_credentials():
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-email").send_keys("sksharan666@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//a[text()='Edit your account information']").text
    expected_text = "Edit your account information"
    assert actual_text.__eq__(expected_text)



def test_login_with_invalid_email_and_valid_password():
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-email").send_keys("XXXXsksharan@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    actual_warning_message = driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
    assert expected_warning_message.__contains__(actual_warning_message)


