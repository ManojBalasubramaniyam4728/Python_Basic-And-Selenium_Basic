import time
from os import times

from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

#Chrome driver
driver = webdriver.Chrome(options=chrome_options)

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Impilicit wait(This will wait globally until element is loaded in web page(DOM)
driver.implicitly_wait(10)
time.sleep(2)
#best site to know about option class parameters
#https://www.guru99.com/chrome-options-desiredcapabilities.html#:~:text=The%20Chromeoptions%20Class%20is%20a,for%20customizing%20Chrome%20driver%20sessions.
