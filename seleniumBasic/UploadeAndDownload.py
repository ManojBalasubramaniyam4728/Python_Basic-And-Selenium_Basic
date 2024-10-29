from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from seleniumBasic.excelUtilit import excelUtilit

#Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.implicitly_wait(5)
excelPath="C:/Users/manoj.b/Downloads/download.xlsx"
fruitName="Apple"
driver.find_element(By.ID,"downloadButton").click()

#Befoure Adding Fruit Price
indexOfThePrice=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actualPriceTextInUI=driver.find_element(By.XPATH,"//div[text()='"+fruitName+"']/parent::div/parent::div//div[@id='cell-"+indexOfThePrice+"-undefined']/child::div").text
print(actualPriceTextInUI)
#editing data in Excel
excelUtilit.writeDataInExpectedCell(excelPath,"Price","Apple","450")

driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(excelPath)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")))
successMessageFromUI=driver.find_element(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)").text
assert "Updated Excel Data Successfully." == successMessageFromUI

#affter Adding Fruit Price
indexOfThePrice=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
expectedPriceTextInUI=driver.find_element(By.XPATH,"//div[text()='"+fruitName+"']/parent::div/parent::div//div[@id='cell-"+indexOfThePrice+"-undefined']/child::div").text
print(expectedPriceTextInUI)
assert actualPriceTextInUI != expectedPriceTextInUI








