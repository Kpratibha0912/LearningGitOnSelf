import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()


# finding elements by locators
driver.find_element(By.NAME, "name").send_keys("TestPerson")
driver.find_element(By.NAME, "email").send_keys("testperson@nomail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@1234!")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//select[@id = 'exampleFormControlSelect1']/option[2]").click()
# Select the radio button Student
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()

driver.find_element(By.XPATH, "//input[@value = 'Submit']").click()

message = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
print(message)
assert "Success" in message
time.sleep(5)
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("abc")




