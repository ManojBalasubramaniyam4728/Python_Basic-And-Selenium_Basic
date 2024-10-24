import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Id, Xpath, CSSSector, ClassName, name, linkText

#Name
driver.find_element(By.NAME, "name").send_keys("Rahul")

#Id
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Rahul@123")

#Xpath--> //TagName[@attributeName="ValueOfTheAttribute"]
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

#Xpath Traversing
driver.find_element(By.XPATH,"//label[text()='Employment Status: ']/..//div[1]/input").click()

#Css Traversing
driver.find_element(By.CSS_SELECTOR,".form-group div:nth-child(3) input").click()

#CSSSelector--> TagName[attributeName="ValueOfTheAttribute"]
driver.find_element(By.CSS_SELECTOR,"input[value='Submit']").click()

#Class
#message=driver.find_element(By.CLASS_NAME,"alert alert-success alert-dismissible").text
#assert "Success! The Form has been submitted successfully!." in message

#If Text is present in dom use xpath
driver.find_element(By.XPATH,"//Strong[text()='Success!']").is_displayed()

#linkText
driver.find_element(By.LINK_TEXT,"Shop").click()

#navigate Back
driver.back()

#PartialLinkText
driver.find_element(By.PARTIAL_LINK_TEXT,"Sh").click()

#close
driver.close()

time.sleep(5)


