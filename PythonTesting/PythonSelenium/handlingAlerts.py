import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

input = "TestData"

driver.find_element(By.XPATH,"//input[@id= 'name']").send_keys(input)
driver.find_element(By.XPATH,"//input[@id= 'alertbtn']").click()

time.sleep(2)

alert = driver.switch_to.alert
alertText = alert.text

print(alertText)

assert input in alertText
alert.accept()


