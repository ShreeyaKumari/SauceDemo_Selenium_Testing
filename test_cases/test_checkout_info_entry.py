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

# Add to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()

# Go to cart and proceed to checkout
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# Enter user info
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Shreeya")
driver.find_element(By.ID, "last-name").send_keys("S")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()

# Verify overview page
if "checkout-step-two" in driver.current_url:
    print("✅ SC7 Passed: Checkout info entry successful and navigated to overview.")
else:
    print("❌ SC7 Failed: Did not reach checkout overview.")

driver.quit()
