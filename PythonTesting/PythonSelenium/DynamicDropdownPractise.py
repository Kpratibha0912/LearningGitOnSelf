import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id = 'autosuggest']").send_keys("Ind")
time.sleep(2)
listOfCountries = driver.find_elements(By.XPATH,"//li[@class = 'ui-menu-item']/a")
print(len(listOfCountries))

for country in listOfCountries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.XPATH,"//input[@id = 'autosuggest']").get_attribute("value"))

# assertion
assert driver.find_element(By.XPATH,"//input[@id = 'autosuggest']").get_attribute("value") == "India"

