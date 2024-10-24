import time
from io import BytesIO

from selenium import webdriver


#Chrome driver
driver = webdriver.Chrome()

#maximize the window
driver.maximize_window()

#navigate to the url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

#scroll till bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#scroll till height
#driver.execute_script(0,500)

#getting screenshot of the page by javaScript executor
driver.get_screenshot_as_file("screen.png")