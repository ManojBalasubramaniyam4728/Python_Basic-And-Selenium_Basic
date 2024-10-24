import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)

#Verify List of Product in Actual v/s expected
expectedProductNameList=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

productNames=driver.find_elements(By.CSS_SELECTOR,"h4[class=product-name]")
actualProductNameList=[]
for productName in productNames:
    actualProductNameList.append(productName.text)

print(expectedProductNameList)
print(actualProductNameList)
assert expectedProductNameList == actualProductNameList

results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
print(count)
assert count > 0
for result in results:
    #element chaining
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"promoInfo")))

promoApplyedText=driver.find_element(By.CLASS_NAME,"promoInfo").text
assert "Code applied ..!" in promoApplyedText

#Verify Total amount from price in table
time.sleep(2)
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")

sum=0
for price in prices:
   sum=sum+ int(price.text)

totalPrice=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(sum)
print(totalPrice)
assert  sum==totalPrice

#verify total amount and total after discount amount
totalAfterDiscount=float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
print(totalAfterDiscount)
assert totalPrice > totalAfterDiscount


