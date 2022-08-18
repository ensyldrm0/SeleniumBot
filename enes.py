from selenium import webdriver
import time

driver = webdriver.Chrome()

url="http://twitter.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("e.png")

url="http:/github.com"
driver.get(url)
time.sleep(2)
driver.back
driver.maximize_window()
time.sleep(2)
driver.close()