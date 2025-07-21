import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print("🌐 Opened SauceDemo login page")
time.sleep(2)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
print("🧑 Entered username")
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("secret_sauce")
print("🔐 Entered password")
time.sleep(2)

driver.find_element(By.ID, "login-button").click()
print("🔓 Clicked login button")
time.sleep(2)

# Add an item to cart
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()
    print("🛒 Added product to cart")
    time.sleep(2)
except:
    print("❌ Failed to add item to cart.")
    driver.quit()
    exit()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("📦 Navigated to cart page")
time.sleep(2)

# Click checkout
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    print("➡️ Clicked Checkout button")
    time.sleep(2)

    if "checkout-step-one" in driver.current_url:
        print("✅ SC6 Passed: Navigated to Checkout Step One.")
    else:
        print("❌ SC6 Failed: Did not reach Checkout Step One page.")
except:
    print("❌ SC6 Failed: Checkout button not found or not clickable.")
    driver.quit()
    exit()

# Optional: Stop here or continue with next steps (fill details, etc.)

driver.quit()
