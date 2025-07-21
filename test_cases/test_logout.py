from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Open burger menu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()

# Wait for logout to be visible and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

# Verify logout worked
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))

if "login" in driver.page_source.lower():
    print("✅ SC3 Passed: Logout redirected to login page.")
else:
    print("❌ SC3 Failed: Logout redirection failed.")

driver.quit()
