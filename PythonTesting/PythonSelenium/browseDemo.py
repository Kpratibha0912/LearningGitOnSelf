import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com")

#maximizes the window after launch
driver.maximize_window()

#fetches the title of the page
print(driver.title)

#There are cases where the page gets redirected to another url after launch, so with this statement, you receive the current url of the page
print(driver.current_url)
time.sleep(2)