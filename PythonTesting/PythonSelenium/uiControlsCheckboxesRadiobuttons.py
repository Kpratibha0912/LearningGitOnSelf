import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()


checkBox = driver.find_element(By.XPATH,"//input[@id = 'checkBoxOption3']")
# radioButton = driver.find_element(By.XPATH,"//input[@value = 'radio2']")
checkBox.click()
# radioButton.click()
time.sleep(2)
assert checkBox.is_selected()
# assert radioButton.is_selected()

# With iteration
radioButtons = driver.find_elements(By.XPATH,"//input[@class = 'radioButton']")
print(len(radioButtons))

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        assert radioButton.is_selected()
        break


