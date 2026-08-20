import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

waitObject = WebDriverWait(driver, 10)

shop = driver.find_element(By.XPATH, "//a[text() = 'Shop']")
shop.click()

products = driver.find_elements(By.XPATH, "//div[@class = 'col-lg-9']/app-card-list/app-card/div/div/h4/a")
listOfProducts = driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")
goToCart = driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']")
# iPhoneX = driver.find_element(By.XPATH, "//a[text() = 'iphone X']").text

# try using the chaining xpath logic to click on the add button


selectedPhone = "iphone X"
for product in listOfProducts:
    if product.find_element(By.XPATH, "./div/h4").text == selectedPhone:
        product.find_element(By.XPATH, "./div/button").click()
        break

print(goToCart.text)
goToCart.click()

# assert selectedPhone == iPhoneX

checkOutFromCart = driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']")
checkOutFromCart.click()

# Enter the country, mark terms and conditions checkbox as true and then click on Purchase button
countryLocator = driver.find_element(By.XPATH, "//input[@id = 'country']")

def purchasePage(country, expectedCountry):
    countryLocator.send_keys(country)
    countrySuggestions = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']//a")
    waitObject.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'suggestions']//a")))
    for suggestion in countrySuggestions:
        if suggestion.text == expectedCountry:
            suggestion.click()
            break

purchasePage("in", "India")
driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']/label").click()
driver.find_element(By.XPATH, "//input[@type= 'submit']").click()
time.sleep(2)
successMessage = driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
print(successMessage)
assert "Thank you!" in successMessage


