import pytest
from selenium import webdriver

# registering the option before using
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser name"
    )

@pytest.fixture
def browserInstance(request ):
    browserName = request.config.getoption("--browser_name")
    if browserName == "chrome":
        driver = webdriver.Chrome()
    elif browserName == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()