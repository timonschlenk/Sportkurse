#import Selenium Libaries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Import the Chrome WebDriver
service = Service(executable_path='./chromedriver.exe')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get('https://www.google.com')

# Wait for the page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS, 'gLFyf'))
)

# Find the input element using its name attribute value
input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')

# Type 'Selenium' into the input element
input_element.clear()  # Clear the input field if needed
input_element.send_keys('Selenium' + Keys.ENTER)

# Print the title of the page  
print(driver.title)

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()