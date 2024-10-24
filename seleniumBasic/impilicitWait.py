import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

#Note:- Implicit will wait till element action and result of it
# But find_elements will return list if element is not present it will
# return 0 list so it should be handel with sleep.
time.sleep(2)

results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count > 0
for result in results:
    #element chaining
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
promoApplyedText=driver.find_element(By.CLASS_NAME,"promoInfo").text
assert "Code applied ..!" in promoApplyedText
