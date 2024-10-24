import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome Option class for setting the headless and certificate etc
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

#Chrome driver this time chrome will not i mean it will be in headless mode
driver = webdriver.Chrome(options=chrome_options)

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(10)

driver.find_element(By.ID,"checkBoxOption1").click()
time.sleep(2)