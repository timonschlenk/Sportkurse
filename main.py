#import Selenium Libaries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import other libraries
import time
import json

# Setup Chrome options and service
service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Load data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)

# Assign variables from JSON
LINK = data["LINK"]
VORNAME = data["VORNAME"]
NAME = data["NAME"]
STRASSE = data["STRASSE"]
ORT = data["ORT"]
GEBURTSDATUM = data["GEBURTSDATUM"]
STATUS = data["STATUS"]
MATNR = data["MATNR"]
EMAIL = data["EMAIL"]

driver.get(LINK) # Open the Doppelkopf page

link_to_inscription = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'bs_btn_buchen')) # ID of the link
)
link_to_inscription.click()

driver.switch_to.window(driver.window_handles[1])

checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@value="M"]'))
)
vorname = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="vorname"]'))
)
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="name"]'))
)
strasse = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="strasse"]'))
)
ort = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="ort"]'))
)
geburtsdatum = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="geburtsdatum"]'))
)
status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//select[@name="statusorig"]'))
)
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
)
tnbed = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="tnbed"]'))
)

checkbox.click()
vorname.send_keys(VORNAME)
name.send_keys(NAME)
strasse.send_keys(STRASSE)
ort.send_keys(ORT)
geburtsdatum.send_keys(GEBURTSDATUM)
status.send_keys(STATUS[0]+Keys.ENTER) # Select the first letter of the status and press Enter
matnr = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="matnr"]'))
)
matnr.send_keys(MATNR)
email.send_keys(EMAIL)
tnbed.click()

submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'bs_submit'))
)
submit.click()

# Wait for 5 seconds
time.sleep(50)

# Close the browser
driver.quit()