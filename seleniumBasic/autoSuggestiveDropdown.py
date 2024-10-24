import time
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://www.makemytrip.com/")
time.sleep(2)

#Auto suggestive dropdown
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"label[for='fromCity']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("Bangluru")
time.sleep(2)
places=driver.find_elements(By.CSS_SELECTOR,"li[role='option'] p:first-child")
print(len(places))
time.sleep(1)
for place in places:
    time.sleep(1)
    if place.text == "Bengaluru":
        place.click()
        break


time.sleep(3)

assert driver.find_element(By.CSS_SELECTOR,"label[for='fromCity']").get_attribute("value") == "Bengaluru"

time.sleep(3)
driver.close()




