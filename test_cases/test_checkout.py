from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
time.sleep(2)

driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()

# Step 1: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 2: Add first two items to cart
driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()  # First item
time.sleep(2)
driver.find_elements(By.CLASS_NAME, "btn_inventory")[1].click()  # Second item
time.sleep(2)

# Step 3: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Step 4: Proceed to checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# Step 5: Enter checkout info
driver.find_element(By.ID, "first-name").send_keys("Shreeya")
time.sleep(2)
driver.find_element(By.ID, "last-name").send_keys("S")
time.sleep(2)
driver.find_element(By.ID, "postal-code").send_keys("560001")
time.sleep(2)
driver.find_element(By.ID, "continue").click()
time.sleep(2)
time.sleep(2)

# Step 6: Capture item prices and compute expected total
item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
time.sleep(2)
total = sum([float(price.text.replace("$", "")) for price in item_prices])
total = round(total, 2)

# Step 7: Get displayed total
summary_total_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
time.sleep(2)
displayed_total = float(summary_total_text.replace("Item total: $", "").strip())
time.sleep(2)

# Step 8: Assert
if total == displayed_total:
    print(f"✅ SC2 Passed: Total ${total} matches expected.")
else:
    print(f"❌ SC2 Failed: Expected ${total}, but got ${displayed_total}.")

# Close browser
driver.quit()
