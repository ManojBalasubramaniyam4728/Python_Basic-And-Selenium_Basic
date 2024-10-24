import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

assert driver.find_element(By.CSS_SELECTOR,".displayed-class").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()

#negation in assertion
assert not driver.find_element(By.CSS_SELECTOR,".displayed-class").is_displayed()

time.sleep(2)

driver.close()