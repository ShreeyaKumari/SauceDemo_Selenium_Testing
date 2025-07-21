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

# Add an item to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Click checkout
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    if "checkout-step-one" in driver.current_url:
        print("✅ SC6 Passed: Navigated to Checkout Step One.")
    else:
        print("❌ SC6 Failed: Did not reach Checkout page.")
except:
    print("❌ SC6 Failed: Checkout button not found or not clickable.")

driver.quit()
