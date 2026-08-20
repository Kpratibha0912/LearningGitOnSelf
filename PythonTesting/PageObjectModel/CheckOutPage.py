from selenium.webdriver.common.by import By

from PageObjectModel.PurchasePage import PurchasePage

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.continueShoppingButton = (By.XPATH, "//button[@class = 'btn btn-default']")
        self.checkoutButton = (By.XPATH, "//button[@class = 'btn btn-success']")

    # def continue_shopping(self):
    #     self.driver.find_element(*self.continueShoppingButton).click()
    #     return ShopPage(self.driver)

    def checkout_shopping(self):
        self.driver.find_element(*self.checkoutButton).click()
        return PurchasePage(self.driver)
