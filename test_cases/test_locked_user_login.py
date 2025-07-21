from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Step 1: Try login with locked-out user
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 2: Capture error message
error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
error_text = error_element.text

# Step 3: Verify message content
expected_message = "Epic sadface: Sorry, this user has been locked out."

if expected_message in error_text:
    print("✅ SC4 Passed: Correct error shown for locked-out user.")
else:
    print(f"❌ SC4 Failed: Unexpected error message -> {error_text}")

driver.quit()
