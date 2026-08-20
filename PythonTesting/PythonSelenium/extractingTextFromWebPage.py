import time
from operator import eq

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client")
# actualUrl = driver.current_url
driver.maximize_window()


# Aim is to click on forgot password link, enter the registered email "demo@gmail.com", enter the new password, confirm password and then click on save password button

# xpath for forgot password link
driver.find_element(By.XPATH, "//a[@class = 'forgot-password-link']").click()
# forgotPasswordUrl = driver.current_url
# print(forgotPasswordUrl)

# You are now navigated to the forgot Password page.
driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//input[@id= 'userPassword']").send_keys("demo@1234")
driver.find_element(By.XPATH, "//input[@id= 'confirmPassword']").send_keys("demo@1234")
driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
# driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()

# assert eq(driver.current_url, "https://www.rahulshettyacademy.com/client")
time.sleep(2)