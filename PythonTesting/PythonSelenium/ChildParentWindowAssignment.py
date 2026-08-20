import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

# find the link and then click on it
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
winList = driver.window_handles
driver.switch_to.window(winList[1])
time.sleep(2)

# get the email id on the page and store it in a variable username
username = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(username)

# come back to the parent window
driver.switch_to.window(winList[0])
driver.find_element(By.XPATH, "//input[@id ='username']").send_keys(username)
driver.find_element(By.XPATH, "//input[@id ='password']").send_keys("P@ssw0rd!")
driver.find_element(By.XPATH, "//input[@id ='signInBtn']").click()
time.sleep(2)
print(driver.find_element(By.XPATH, "//div[@class = 'alert alert-danger col-md-12']").text)