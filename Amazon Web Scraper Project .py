#!/usr/bin/env python
# coding: utf-8

# In[258]:


# import libraries 
from bs4 import BeautifulSoup
import requests
import time 
import datetime

import smtplib


# In[ ]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/Data-Analyst-Sleeve-T-Shirt-Husband/dp/B09ZF1J1XG/ref=sr_1_5?crid=27454M50F5US0&keywords=data%2Banalyst%2Btshirt&qid=1692466263&sprefix=data%2Banalyst%2Btshirt%2Caps%2C586&sr=8-5&th=1&psc=1'



# In[ ]:


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


# In[ ]:


page = requests.get(URL,headers=headers)


# In[ ]:


soup1 = BeautifulSoup(page.content,"html.parser")


# In[ ]:


soup2 = BeautifulSoup(soup1.prettify(),"html.parser")


# In[ ]:


title = soup2.find(id="productTitle").get_text().strip()


# In[ ]:


price = soup2.find(class_="a-offscreen").get_text().strip()[1:]


# In[ ]:


print(title)
print(price)


# In[ ]:


import datetime

today = datetime.date.today()

print(today)


# In[ ]:


# create CSV to inset the data 

import csv

header = ['Title', 'Price', 'Date']
data = [title,price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:


import pandas as pd 
df = pd.read_csv(r'C:\Users\Lenovo\AmazonWebScraperDataset.csv')
print(df)


# In[ ]:


# Now we are appending data to the csv()

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    URL = 'https://www.amazon.com/Data-Analyst-Sleeve-T-Shirt-Husband/dp/B09ZF1J1XG/ref=sr_1_5?crid=27454M50F5US0&keywords=data%2Banalyst%2Btshirt&qid=1692466263&sprefix=data%2Banalyst%2Btshirt%2Caps%2C586&sr=8-5&th=1&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    title = soup2.find(id="productTitle")
    price = soup2.find(class_="a-offscreen")
    import datetime

    today = datetime.date.today()

    print(today)
    
    import csv

    header = ['Title', 'Price', 'Date']
    data = [title,price, today]
    with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
    if(price < 14):
        send_mail()


# In[ ]:


while(True):
    check_price()
    time.sleep(80)


# In[ ]:


import pandas as pd 
df = pd.read_csv(r'C:\Users\Lenovo\AmazonWebScraperDataset.csv')
print(df)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('AlexTheAnalyst95@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'AlexTheAnalyst95@gmail.com',
        msg
     
    )


# In[ ]:




