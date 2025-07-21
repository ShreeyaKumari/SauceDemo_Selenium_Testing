from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
