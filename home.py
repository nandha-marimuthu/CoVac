from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient

#connecting with the mongodb cluster using the connection token
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

#declaring the database
db = client['Covac']

#declaring the collections
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']

def dup(x):
  z=[]
  for i in x:
    if i not in z:
      z.append(i)
  return z
a = c1.find()
x=[]
for i in a:

  x.append(i['region'])
x = dup(x)


option = st.sidebar.selectbox('Menu',['Home','Appoinment','Staff','Admin','Dashboard','About'])

if option == 'Home':
  st.title('Covid Vaccination Portal')
  
if option == 'Appoinment':
  st.title('Appoinment')
  st.header('Hospitals')
  option1 = st.selectbox('Regions',x)
  b = c1.find({'region':option1})
  y = []
  for i in b:
    y.append(i['cname'])
  option2 = st.selectbox('Hospitals',y)

  
