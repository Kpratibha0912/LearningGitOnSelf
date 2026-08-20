from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver
        self.countryInput = (By.XPATH, "//input[@id = 'country']")
        self.termsAndConditionsCheckbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']/label")
        self.purchaseButton = (By.XPATH, "//input[@value = 'Purchase']")
        self.alertMessage = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']")


    def add_address(self, input, expectedCountry):
        self.driver.find_element(*self.countryInput).send_keys(input)
        wait = WebDriverWait(self.driver, 10)
        countrySuggestions = self.driver.find_elements(By.XPATH, "//div[@class = 'suggestions']//a")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'suggestions']//a")))
        for suggestion in countrySuggestions:
            if suggestion.text == expectedCountry:
                suggestion.click()
                break


    def accept_terms_and_conditions(self):
        self.driver.find_element(*self.termsAndConditionsCheckbox).click()

    def click_on_purchase_button(self):
        self.driver.find_element(*self.purchaseButton).click()

    def validate_order(self):
        successMessage = self.driver.find_element(*self.alertMessage).text
        assert "Thank you!" in successMessage