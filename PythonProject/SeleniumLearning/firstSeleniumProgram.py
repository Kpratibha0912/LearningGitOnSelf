import time
from ssl import Options

from selenium import webdriver

print("The execution starts")

# invokes the web browser
driver = webdriver.Chrome()

# Opens the link entered in the braces in the browser
driver.get("https://www.google.com")

# gets the title of the web page
print(driver.title)

# waits on the web page for 5 seconds and then the browser is closed
time.sleep(5)
