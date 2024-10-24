import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/angularpractice/")

#If user see the select tage element then go for Select options
dropDown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropDown.select_by_index(1)
dropDown.select_by_visible_text("Male")












time.sleep(4)
