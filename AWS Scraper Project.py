#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[10]:


# Connect to website

URL = 'https://www.amazon.com/-/es/Michio-Kaku/dp/0385477813/ref=sr_1_1?__mk_es_US=ÅMÅŽÕÑ&crid=1VI7JVBS1OXT6&keywords=beyond%2Beinstein%2Bby%2Bmichio%2Bkaku&qid=1680828552&sprefix=beyond%2Beinstein%2Bby%2Bmichio%2Bkaku%2Caps%2C177&sr=8-1&language=en_US'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()
review = soup2.find(id='acrCustomerReviewText').get_text()

print(title)
print(review)


# In[11]:


title = title.strip()
review = review.strip()[:3]

print(title)
print(review)


# In[23]:


# Getting the time

from datetime import datetime
import pytz

hawaiizone = pytz.timezone('Pacific/Honolulu')
timehawaii = datetime.now (hawaiizone)
hour = timehawaii.strftime('%H:%M:%S')

print(hour)


# In[24]:


# Create .csv document and write headers and data into the file

import csv 

header = ['Title', 'Review', 'Date']
data = [title, review, hour]

with open('AWSDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[25]:


# Funtion to check the rating
def check_rating():
    URL = 'https://www.amazon.com/-/es/Michio-Kaku/dp/0385477813/ref=sr_1_1?__mk_es_US=ÅMÅŽÕÑ&crid=1VI7JVBS1OXT6&keywords=beyond%2Beinstein%2Bby%2Bmichio%2Bkaku&qid=1680828552&sprefix=beyond%2Beinstein%2Bby%2Bmichio%2Bkaku%2Caps%2C177&sr=8-1&language=en_US'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    review = soup2.find(id='acrCustomerReviewText').get_text()
    
    title = title.strip()
    review = review.strip()[:3]

    from datetime import datetime
    import pytz

    hawaiizone = pytz.timezone('Pacific/Honolulu')
    timehawaii = datetime.now (hawaiizone)
    hour = timehawaii.strftime('%H:%M:%S')

    import csv 

    header = ['Title', 'Review', 'Date']
    data = [title, review, hour]
    
    with open('AWSDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


# Check the rating every hour
while(True):
    check_rating()
    time.sleep(3600)


# In[ ]:


import pandas as pd

df = pd.read_cvs(http://localhost:8888/edit/AWSDataset.csv)
print(df)


# In[ ]:




