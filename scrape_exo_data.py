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

# returns the generated data frame
def generate_exoplanet_df(driver):
    planet_name = []
    dist_from_earth = []
    planet_mass = []
    stellar_magnitude = []
    discovery_date = []

    # max_pages is the number of pages in the table
    max_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/div/span'))).text
    page = 1

    while page <= int(max_page):
        driver.refresh()
        
        try:
            table = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((
                By.CLASS_NAME, "exoplanet")))
        except TimeoutException:
            print('WEB DRIVER FAILURE')
            driver.quit() 
           
        for row in table:
            planet_name.append(row.find_element(By.CLASS_NAME, "display_name").text)
            dist_from_earth.append(row.find_element(By.CLASS_NAME, "st_dist").text)
            planet_mass.append(row.find_element(By.CLASS_NAME, "mass_display").text)
            stellar_magnitude.append(row.find_element(By.CLASS_NAME, "st_optmag").text)
            discovery_date.append(row.find_element(By.CLASS_NAME, "discovery_date").text)

        
        next_page = WebDriverWait(driver,10).until(EC.element_to_be_clickable((
            By.XPATH, "//*[@id='primary_column']/footer/div/div/div/nav/span[2]/a")))

        page += 1



    df = pd.DataFrame({"Planet Name" : planet_name, "Distance From Earth" : dist_from_earth, "Planet Mass" : planet_mass,
    "Stellar Magnitude" : stellar_magnitude, "Discovery Date" : discovery_date})

    return df

x=Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=x)

#url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
driver.get('https://exoplanets.nasa.gov/discovery/exoplanet-catalog/')

# get title
#print(get_title(driver))

# generate exoplanet dataframe
print(generate_exoplanet_df(driver))


# To keep the browser open fo 50 seconds
time.sleep(50)
driver.quit() 

