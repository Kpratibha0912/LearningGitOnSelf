import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# implicit wait gives the max timeout time. If the operation finishes in less than the limit provided, it will complete the operation and proceed and will not wait until the time limit is reached. For cases, where it takes time to load, it will wait max till the given limit and if it still does not load, it will timeout and give error on execution
driver.implicitly_wait(5)

# Get the locator for the search bar and enter "ber"
driver.find_element(By.XPATH, "//input[@type= 'search']").send_keys("ber")
time.sleep(2)

# Get all the products appearing with "ber" search
productList = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")

# addToCartButton = driver.find_elements(By.XPATH, "//div[@class = 'products']/div/div/button")

for products in productList:
    products.find_element(By.XPATH, "div/button").click()

# click on the cart
driver.find_element(By.XPATH, "//a[@class = 'cart-icon']").click()

# click on "Proceed to checkout" to go to the next page
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

# Enter the promocode and click on apply button
driver.find_element(By.XPATH, "//input[@class = 'promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text() = 'Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class = 'promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class = 'promoInfo']").text)


