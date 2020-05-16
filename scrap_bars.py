from selenium import webdriver
import time
import requests
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome("/usr/bin/chromedriver")


#Here, Selenium accesses the Chrome browser driver in incognito mode and
#without actually opening a browser window(headless argument).


driver.get("https://www.tripadvisor.fr/Restaurant_Review-g187162-d3193015-Reviews-Comptoir_Saint_Michel-Nancy_Meurthe_et_Moselle_Grand_Est.html")

reviews = {}
elem = driver.find_element_by_css_selector('.ulBlueLinks')
time.sleep(2)
elem.click()
review_elem = driver.find_elements_by_css_selector('.partial_entry')
reviews['restau0'] = [p.text for p in review_elem]
start_URL = "https://www.tripadvisor.fr/Restaurant_Review-g187162-d3193015-Reviews-or"
end_URL = "-Comptoir_Saint_Michel-Nancy_Meurthe_et_Moselle_Grand_Est.html"
for page in range(10,110,10):
    try:
        driver.get(start_URL + str(page) + end_URL)
        elem = driver.find_element_by_css_selector('.ulBlueLinks')
        # element without a s cause we want to click and go next
        time.sleep(2)
        elem.click()
        review_elem = driver.find_elements_by_css_selector('.partial_entry')
        # element with a s cause we want to collect and go next
        reviews['restau'+str(page)] = [p.text for p in review_elem]
    except:
        pass

#html_source = driver.page_source
#driver.quit()


# Here, Selenium web driver traverses through the DOM of Trip Advisor review page and finds all “More” buttons. 
# Then it iterates through all “More” buttons and automates their clicking. 
# On the automated clicking of “More” buttons, the reviews which were partially available before becomes fully available.


# # Lire 
# with open('fichier.json', 'r', encoding='utf-8') as f:
#     data = json.loads(f.read()) 
# Ecrire 
with open('reviews.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(reviews))