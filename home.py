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





option = st.sidebar.selectbox('Menu',['Home','Appoinment','Staff','Admin','Dashboard','About'])

if option == 'Home':
  st.title('Covid Vaccination Portal')

if option == 'Appoinment':
  st.title('Appoinment')
  name = st.text_input('Name')
  aadhar = st.text_input('Aadhar No')
  a = st.checkbox('procced')
  a1 = c4.find()
  c = 0
  for i in a1:
    if i['name'] == name:
      if i['aadhar'] == aadhar:
        c+=1
  if a and (c==0):
    from appoinment import appoinment
    appoinment(name,aadhar)
      



  

  
