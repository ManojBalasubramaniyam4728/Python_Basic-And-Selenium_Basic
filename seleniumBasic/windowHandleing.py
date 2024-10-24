import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#window Handling
driver.find_element(By.ID,"openwindow").click()
openedWindows=driver.window_handles

#switchig to child window
for openedWindow in openedWindows:
    driver.switch_to.window(openedWindow)
    actualUrl=driver.current_url
    expectedUrl="https://www.qaclickacademy.com/"
    if actualUrl ==expectedUrl:
        driver.maximize_window()
        break

#performing action in child window
driver.find_element(By.LINK_TEXT,"Access all our Courses").click()
text=driver.find_element(By.CLASS_NAME,"ud-heading-serif-xxxl").text
#verifying the text in child window
assert "QA Click Academy" == text
driver.close()

#switching to parent window back
for openedWindow in openedWindows:
    driver.switch_to.window(openedWindow)
    actualUrl=driver.current_url
    expectedUrl="https://rahulshettyacademy.com/AutomationPractice/"
    if actualUrl ==expectedUrl:
        break

#verifying the text in parent window
textInParentWindow=driver.find_element(By.ID,"openwindow").text
assert "Open Window" == textInParentWindow