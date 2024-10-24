import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#Action Chaining
action=ActionChains(driver)

#mouse action to the element
action.scroll_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()

#Lot of things can be done in action chins
#action.context_click() [ #Right click on element]
#action.double_click() [ #double click on element]
#action.drag_and_drop_by_offset() [#draging from element to to element]
#action.click_and_hold() [#holding element for few second]
#action.send_keys() [#entering input]
#action.pause(3) [#pause for few seconds]
#action.key_down(Keys.CONTROL).send_keys("S").key_up(Keys.CONTROL).perform() [#pressing two keys and releasing]

