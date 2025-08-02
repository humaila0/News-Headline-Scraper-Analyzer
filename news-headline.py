from distributed.dashboard.scheduler import applications
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
import os
import sys

application_path= os.path.dirname(sys.executable)

now=datetime.now()
month_day_year=now.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\Dell\Downloads\chromedriver-win64\chromedriver.exe"

#headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(website)

time.sleep(5)  # Wait for the page to fully load

titles = []
subtitles = []
links = []

containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')

for container in containers:
    try:
        title = container.find_element(By.XPATH, './/a/span').text
    except:
        title = ''

    try:
        subtitle = container.find_element(By.XPATH, './/a/h3').text
    except:
        subtitle = ''

    try:
        link = container.find_element(By.XPATH, './/a').get_attribute('href')
    except:
        link = ''

    # Only save if at least one field is valid
    if title or subtitle or link:
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name=f'headlines_{month_day_year}.csv'
final_path=os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()
