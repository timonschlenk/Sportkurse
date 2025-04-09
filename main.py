#import Selenium Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import other libraries
import time
import json
from concurrent.futures import ThreadPoolExecutor

def inscribe(data):
    # Setup Chrome options and service
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Assign variables from JSON
        LINK = data["LINK"]
        KURSNUMMER = data["KURSNUMMER"]
        VORNAME = data["VORNAME"]
        NAME = data["NAME"]
        STRASSE = data["STRASSE"]
        ORT = data["ORT"]
        GEBURTSDATUM = data["GEBURTSDATUM"]
        STATUS = data["STATUS"]
        MATNR = data["MATNR"]
        EMAIL = data["EMAIL"]

        # Open the page and check for the "Buchen" button
        driver.get(LINK)
        while True:
            try:
                # Check if the "Buchen" button is available
                link_to_inscription = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, f"//td[a[@id='K{KURSNUMMER}']]/input"))
                )
                # If found, break the loop
                break
            except:
                # If not found, reload the page
                print("Buchen button not available, reloading the page...")
                driver.refresh()

        # Click the "Buchen" button
        link_to_inscription.click()

        driver.switch_to.window(driver.window_handles[1])

        # Fill out the form
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
        status.send_keys(STATUS[0] + Keys.ENTER)  # Select the first letter of the status and press Enter
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

        # Wait for 5000 seconds
        time.sleep(10)

    finally:
        # Close the browser
        driver.quit()

# Load data from data.json
with open('data.json', 'r') as file:
    all_data = json.load(file)

# Run inscriptions simultaneously using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    executor.map(inscribe, all_data)