import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsList = driver.window_handles
driver.switch_to.window(windowsList[1])
print(driver.find_element(By.XPATH, "//h3").text)
driver.close()
driver.switch_to.window(windowsList[0])
print(driver.find_element(By.XPATH, "//h3").text)
