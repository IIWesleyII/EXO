from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException




def get_title(driver):
    return driver.title

def get_table(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results')))
    except TimeoutException:
        print('web driver failure')
        driver.quit() 

    table = driver.find_element("id", "results")
    print(table.text)

x=Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=x)

#url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
driver.get('https://exoplanets.nasa.gov/discovery/exoplanet-catalog/')

# get title
print(get_title(driver))

# get exoplanet table
print(get_table(driver))











# To keep the browser open fo 50 seconds
time.sleep(50)
driver.quit() 

