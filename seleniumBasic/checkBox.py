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

checkboxs =driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(2)
        assert  checkbox.is_selected()

driver.close()
