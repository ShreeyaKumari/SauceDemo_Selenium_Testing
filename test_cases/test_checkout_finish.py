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

# Add item to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()

# Go to cart and checkout
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# Enter user info
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Shreeya")
driver.find_element(By.ID, "last-name").send_keys("S")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()

# Finish the checkout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "finish"))).click()

# Check for order confirmation
try:
    confirmation = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    if "THANK YOU" in confirmation.text.upper():
        print("✅ SC8 Passed: Order completed successfully.")
    else:
        print("❌ SC8 Failed: Confirmation message not as expected.")
except:
    print("❌ SC8 Failed: Confirmation message not found.")

driver.quit()
