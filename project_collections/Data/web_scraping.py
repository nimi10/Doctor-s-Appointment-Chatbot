#Import Webscraping libraries
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver

#Import Data structure libraries
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

#Import libraries for controlling crawling rate
from time import sleep, time
from random import randint

from IPython.display import Image
import requests #to request html page code
import bs4 #to format html code
urls=[]
for i in range(1,40):
    urls.append(' https://www.practo.com/delhi/doctors?page={}'.format(i))
    
doctornames=[]
clinicnames=[]
locality=[]
for url in urls:
    practo=requests.get(url)
    soup=bs4.BeautifulSoup(practo.text,'lxml')
    
    
    alldoctornames=soup.select('.doctor-name')
    for doctor in alldoctornames:
        doctornames.append(doctor.getText())
        
   
    allclinicdump=soup.select('.u-c-pointer.u-t-hover-underline')
    clinicnamestemp=[]
    for data in allclinicdump:
        clinicnamestemp.append(data.getText()) #this gets some unwanted data, requires cleaning
    for clinic in clinicnamestemp[1:]:
        if 'more' not in clinic:
            clinicnames.append(clinic)
            
    
    alllocality=soup.select('.u-bold.u-d-inlineblock.u-valign--middle')
    for place in alllocality:
        locality.append(place.getText().split(',')[0])
    doctor_data=pd.DataFrame()
    doctor_data[:40]
    doctor_data[:40].to_excel('doctor_dataset.xlsx',sheet_name='doctor_dataset',index=False)
