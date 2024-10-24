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

radioButtons =driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
radioButtons[1].click()
assert  radioButtons[1].is_selected()

driver.close()
