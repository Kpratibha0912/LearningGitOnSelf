import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.maximize_window()
driver.implicitly_wait(5)
fruit = "Mango"

# Click on 'download button'
driver.find_element(By.XPATH, "//button[@id = 'downloadButton']").click()

# Uploading the file
filePath = "C:\\Users\\Pratibha.PRATIBHA-VARUN\\Downloads\\download.xlsx"
driver.find_element(By.XPATH, "//input[@id= 'fileinput']").send_keys(filePath)

# Put explicit wait so that the element is captured for the success message

# successful upload toast message
toastMessage = driver.find_element(By.XPATH, "//div[text() = 'Updated Excel Data Successfully.']")

waitObj = WebDriverWait(driver, 5)
waitObj.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text() = 'Updated Excel Data Successfully.']")))
print(toastMessage.text)

# Finding the smart XPATH by traversing back from child to parent and then to the sibling. This is the scenario where you want to traverse to a column through another one.

# Generalize this statement, since this can be dynamic thing, so let's make it dynamic and not hard coding

# time.sleep(2)
priceColumn = driver.find_element(By.XPATH, "//div[text() = 'Price']").get_attribute("data-column-id")
seasonColumn = driver.find_element(By.XPATH, "//div[text() = 'Season']").get_attribute("data-column-id")
priceOfFruit = driver.find_element(By.XPATH, f"//div[text() = '{fruit}']/parent::div/parent::div/div[@data-column-id = '{priceColumn}']").text
seasonOfFruit = driver.find_element(By.XPATH, f"//div[text() = '{fruit}']/parent::div/parent::div/div[@data-column-id = '{seasonColumn}']").text

print(priceOfFruit)
print(seasonOfFruit)