from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME,"q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
# print(result)
result = driver.find_elements(By.CSS_SELECTOR,".repo-list-item .d-flex .f4.text-normal a")

for element in result:
    print(element.text)

driver.close()
