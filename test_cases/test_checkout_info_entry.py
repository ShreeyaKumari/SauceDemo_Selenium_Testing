import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Add specific product to cart
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    print("✅ Product added to cart")
except:
    print("❌ Failed to add product to cart")
    driver.quit()
    exit()

time.sleep(2)

# Go to cart
try:
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("🛒 Navigated to cart")
except:
    print("❌ Failed to go to cart")
    driver.quit()
    exit()

time.sleep(2)

# Click Checkout
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()
    print("➡️ Clicked checkout")
except:
    print("❌ Failed to find/click checkout button")
    driver.quit()
    exit()

time.sleep(2)

# Fill checkout info slowly
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Shreeya")
    time.sleep(2)
    driver.find_element(By.ID, "last-name").send_keys("S")
    time.sleep(2)
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    time.sleep(2)
    driver.find_element(By.ID, "continue").click()
except:
    print("❌ Failed during checkout info entry")
    driver.quit()
    exit()

time.sleep(2)

# Verify overview page
if "checkout-step-two" in driver.current_url:
    print("✅ SC7 Passed: Checkout info entry successful and navigated to overview.")
else:
    print("❌ SC7 Failed: Did not reach checkout overview.")

driver.quit()
