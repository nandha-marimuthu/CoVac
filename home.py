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
c1 = db['patient']
c1 = db['appoinment']
c1 = db['vaccinated']

option = st.sidebar.selectbox('Menu',['Home','Appoinment','Staff','Admin','Dashboard'])

if option == 'Home':
  st.title('Covid Vaccination Portal')