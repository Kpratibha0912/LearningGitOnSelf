from selenium.webdriver.common.by import By

from PageObjectModel.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.shopMenuLink = (By.XPATH, "//a[text() = 'Shop']")

    def clickOnShopMenu(self):
        self.driver.find_element(*self.shopMenuLink).click()
        shop_page = ShopPage(self.driver)
        return shop_page


