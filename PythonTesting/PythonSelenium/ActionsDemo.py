import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.XPATH, "//button[@id = 'mousehover']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//a[text() = 'Top']")).click().perform()
time.sleep(2)

print(driver.find_element(By.XPATH, "//a[@class = 'blinkingText']").is_displayed())