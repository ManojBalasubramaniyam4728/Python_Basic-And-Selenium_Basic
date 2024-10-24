import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service("C:/Users/manoj.b/PycharmProjects/Python Basic/drivers/msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://github.com/manojbalasubramaniyam4728")
driver.maximize_window()











time.sleep(2)