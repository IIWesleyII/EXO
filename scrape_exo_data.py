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
    '''
    1. init lists to hold data for dataframe
    2. get max page
    3. set while loop to     while page <= max_page
    4. create web driver for each page , each time loading into dataframe
    '''
    planet_name = []
    dist_from_earth = []
    planet_mass = []
    stellar_magnitude = []
    discovery_date = []

    # max_pages is the number of pages in the table
    max_pages = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/div/span'))).text

    try:
       table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results')))
    except TimeoutException:
        print('web driver failure')
        driver.quit() 

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

