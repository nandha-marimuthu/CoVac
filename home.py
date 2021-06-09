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





option = st.sidebar.selectbox('Menu',['Home','Appoinment','Cancel/Reshedule','Staff','Admin','Dashboard','About'])

if option == 'Home':
  st.title('Covid Vaccination Portal')
  from covid import Covid

  from covid_india import states
  a = states.getdata()
  states = ['Tamil Nadu']
  for i in a:
    states.append(i)
  sta = st.selectbox('statewiese data',states)
  for i in a[sta]:
    st.write(i," : ",a[sta][i])
  st.title('FAQ')
  from homepage import homepage
  homepage()


if option == 'Appoinment':
  from appoinment import login
  login()
if option == 'Cancel/Reshedule':
  from recan import recan
  recan()

  



  

  
