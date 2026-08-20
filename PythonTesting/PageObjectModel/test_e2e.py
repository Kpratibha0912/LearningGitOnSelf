import json

import pytest
from selenium.webdriver.support import expected_conditions

from PageObjectModel.HomePage import HomePage
from PageObjectModel.ShopPage import ShopPage
from PageObjectModel.PurchasePage import PurchasePage
from PageObjectModel.CheckOutPage import CheckOutPage

# read data from the json file, for that use the below logic
test_data_path = "./data/test_e2e.json"
with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]

# With line 13, the json file was converted to a python object. To read data from this object, we need to pass this as fixture

@pytest.mark.parametrize("test_data_items", test_list)
def test_e2e(browserInstance, test_data_items):
    driver = browserInstance
    driver.get(test_data_items["url"])
    home_page = HomePage(driver)
    shop_page = home_page.clickOnShopMenu()
    shop_page.addProductToCart(test_data_items["product"])
    checkoutPage = shop_page.clickOnCheckOutButton()
    purchase_page = checkoutPage.checkout_shopping()
    purchase_page.add_address("ind", "India")
    purchase_page.accept_terms_and_conditions()
    purchase_page.click_on_purchase_button()
    purchase_page.validate_order()
