from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Step 1: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 2: Add first two items to cart
driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()  # First item
driver.find_elements(By.CLASS_NAME, "btn_inventory")[1].click()  # Second item

# Step 3: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Step 4: Proceed to checkout
driver.find_element(By.ID, "checkout").click()

# Step 5: Enter checkout info
driver.find_element(By.ID, "first-name").send_keys("Shreeya")
driver.find_element(By.ID, "last-name").send_keys("S")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# Step 6: Capture item prices and compute expected total
item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
total = sum([float(price.text.replace("$", "")) for price in item_prices])
total = round(total, 2)

# Step 7: Get displayed total
summary_total_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
displayed_total = float(summary_total_text.replace("Item total: $", "").strip())

# Step 8: Assert
if total == displayed_total:
    print(f"✅ SC2 Passed: Total ${total} matches expected.")
else:
    print(f"❌ SC2 Failed: Expected ${total}, but got ${displayed_total}.")

# Close browser
driver.quit()
