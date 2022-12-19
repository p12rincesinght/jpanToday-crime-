from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
import pymongo
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://japantoday.com/category/crime")




data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
Link=[]
Para=[]
Date=[]
Head=[]
content2=soup.find_all("h3")
content1=soup.find_all("time")
content3=soup.find_all('p',class_='text-small mt-5 mb-5')


for i in range(len(content1)-10):

    f=str(content1[i].text) 
    Date.append(f)
    
    
#print(Date)
for i in range(len(content3)):
    Para.append(content3[i].text)
    
print(Para)


for i in range(len(content2)-12):
    Head.append(content2[i].text)
    content1[i]
print(Head)


cont=soup.find_all('a', href=True)
for link in range(22,len(cont)-22):
    Link.append(cont[link]['href'])


print(len(Date))
print(len(Head))
print(len(Link))
print('hey')
client =pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db = client['TIMES1fgfg2']
collection =db ['project12rhj']
for i in range(8):
    dictionary = {"HEAD":Head[i],'Paraw':Para[i],'DATE':Date[i]}
    collection.insert_one(dictionary)
one=collection.find()
for i in one:
    print(i)
