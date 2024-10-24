from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)

driver.find_element(By.PARTIAL_LINK_TEXT,"Free Access to InterviewQues").click()

#getting all the opened windows
openedWindows=driver.window_handles
#switchig to child window by actual is having expected url
for openedWindow in openedWindows:
    driver.switch_to.window(openedWindow)
    actualUrl=driver.current_url
    expectedUrl="https://rahulshettyacademy.com/documents-request"
    if actualUrl ==expectedUrl:
        break

#Performing action an child window
emailIdFromChildWindow=driver.find_element(By.CSS_SELECTOR,"p[class='im-para red'] a").text
#Verifying weather it grabbed correct text or not
assert "mentor@rahulshettyacademy.com" == emailIdFromChildWindow
#closing the child window which is opened
driver.close()

#switchig to parent window by actual is having expected url
for openedWindow in openedWindows:
    driver.switch_to.window(openedWindow)
    actualUrl=driver.current_url
    expectedUrl="https://www.rahulshettyacademy.com/loginpagePractise/"
    if actualUrl ==expectedUrl:
        break

#Performing action an parent window
driver.find_element(By.ID,"username").send_keys(emailIdFromChildWindow)
driver.find_element(By.ID,"password").send_keys("Password@123")
driver.find_element(By.ID,"signInBtn").click()

#error messaging coming late waiting explicitly
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

errorMessage=driver.find_element(By.CSS_SELECTOR,".alert-danger").text
assert "username/password." in errorMessage
#closing every thing
driver.close()