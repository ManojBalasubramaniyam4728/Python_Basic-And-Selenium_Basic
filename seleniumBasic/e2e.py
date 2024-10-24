import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()
expectedProductName="Blackberry"

#navigate to the url
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(2)

driver.find_element(By.PARTIAL_LINK_TEXT,"Shop").click()
productListPages=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for productListPage in productListPages:
    actualProductName= productListPage.find_element(By.XPATH,"div/h4/a").text
    if actualProductName == expectedProductName:
        productListPage.find_element(By.XPATH, "div/button[@class='btn btn-info']").click()

action=ActionChains(driver)
action.scroll_to_element(driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")).perform()
driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='btn btn-success']")))
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='country']").click()
driver.find_element(By.CSS_SELECTOR,"input[id='country']").send_keys("Ind")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//input[@id='checkbox2']/..//label").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
alertMessage=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank" in alertMessage

driver.close()

