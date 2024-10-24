import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()
name ="manoj"

#navigate to the url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

#alert popup
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)

#Switching to only ok alert popup
driver.find_element(By.ID,"alertbtn").click()
alertPopupWindow=driver.switch_to.alert
alertMessage=alertPopupWindow.text
assert name in alertMessage
#click on ok button using selenium api
alertPopupWindow.accept()

time.sleep(2)

#switching to cancel and ok alert popup
driver.find_element(By.ID,"confirmbtn").click()
alertPopupWindow=driver.switch_to.alert
alertMessage=alertPopupWindow.text
assert "Hello , Are you sure you want to confirm?" in alertMessage
#click on cancel button using selenium api
alertPopupWindow.dismiss()

time.sleep(2)
driver.close()



