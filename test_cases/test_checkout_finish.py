import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Toggle this to True to force an intentional failure
force_fail = False  # Change to True to make it fail intentionally

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

# Add item to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()
time.sleep(2)

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Proceed to checkout
try:
    if force_fail:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "checkot"))).click()  # wrong id
    else:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    time.sleep(2)
except:
    print("❌ SC8 Failed at Checkout Button: Button not found or not clickable.")
    driver.quit()
    exit()

# Fill in user details
try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Shreeya")
    time.sleep(2)
    driver.find_element(By.ID, "last-name").send_keys("S")
    time.sleep(2)
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    time.sleep(2)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
except:
    print("❌ SC8 Failed at Form Fill: One or more form fields not found.")
    driver.quit()
    exit()

# Click Finish
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    time.sleep(2)
except:
    print("❌ SC8 Failed: Finish button not found.")
    driver.quit()
    exit()

# Final Confirmation
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
