import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://the-internet.herokuapp.com/iframe")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//div[@aria-label='Close']/./*").click()

#Switch to iframe by Element, Index,
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Rich Text Area']"))
#driver.switch_to.frame(0)

#performing action on iframe
messageInFrame=driver.find_element(By.XPATH,"//body[@id='tinymce']//p").text
assert "Your content goes here." ==messageInFrame

#switching to parent frame to perform action in parent frame
#by two wys you can switch parent_frame() or default_content
driver.switch_to.parent_frame()
#driver.switch_to.default_content()
text=driver.find_element(By.TAG_NAME,"h3").text

assert "An iFrame" in text