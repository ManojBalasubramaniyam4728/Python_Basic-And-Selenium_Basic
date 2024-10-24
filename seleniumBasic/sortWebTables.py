import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(10)

#Click on browser sort element
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# storing webElements in list
time.sleep(2)
veggieWebElement=driver.find_elements(By.XPATH,"//tr/td[1]")
veggieList=[]
for ele in veggieWebElement:
    veggieList.append(ele.text)

#getting copy of the list for compair
#again you can copy by two-way in list copy(), slice()
originalVeggieList=veggieList.copy()

#sort vegglist in python
veggieList.sort()

#comparing two list in assert
assert originalVeggieList == veggieList


