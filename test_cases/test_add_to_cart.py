import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Add first product to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()

# Check if cart badge shows 1
try:
    cart_badge = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    if cart_badge.text == "1":
        print("✅ SC5 Passed: Item successfully added to cart.")
    else:
        print("❌ SC5 Failed: Cart count mismatch.")
except:
    print("❌ SC5 Failed: Cart badge not found.")

driver.quit()
