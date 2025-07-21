from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up ChromeDriver service
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
time.sleep(2)

# Step 1: Open SauceDemo site
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

# Step 2: Enter valid username and password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)

# Step 3: Click login button
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 4: Verify successful login by checking URL or page content
if "inventory" in driver.current_url:
    print("✅ SC1 Passed: Login successful and Inventory page loaded.")
else:
    print("❌ SC1 Failed: Inventory page not loaded.")

# Step 5: Close the browser
driver.quit()
