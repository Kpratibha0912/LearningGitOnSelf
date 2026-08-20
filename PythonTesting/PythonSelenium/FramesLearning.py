import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH, "//fieldset/legend[text() = 'iFrame Example']")).perform()

driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.XPATH, "//li[text()=' contact@rahulshettyacademy.com']").text)
actions.move_to_element(driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES")).perform()
driver.switch_to.default_content()
actions.move_to_element(driver.find_element(By.XPATH, "//h1")).perform()
time.sleep(2)