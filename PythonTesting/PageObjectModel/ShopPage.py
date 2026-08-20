from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from PageObjectModel.CheckOutPage import CheckOutPage



class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.allProducts = (By.XPATH, "//div[@class = 'card h-100']")
        self.checkoutButton = driver.find_element(By.XPATH, "//a[@class = 'nav-link btn btn-primary']")


    def addProductToCart(self, expectedProduct):
        # wait = WebDriver.Wait(10)
        # wait.until(expected_conditions.presence_of_element_located((self.allProducts)))
        for product in self.driver.find_elements(*self.allProducts):
            productName = product.find_element(By.XPATH, "./div/h4").text
            if productName == expectedProduct:
                product.find_element(By.XPATH, "./div/button").click()
                break

    def clickOnCheckOutButton(self):
        self.checkoutButton.click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage


