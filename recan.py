from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient
import random
import datetime

#connecting with the mongodb cluster using the connection token
client = MongoClient('mongodb+srv://dbuser2:covac@eshop.m8tu7.mongodb.net/test')

#declaring the database
db = client['Covac']

#declaring the collections
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']

def recan():
  st.title('Reschedule/Cancel')
  aid = st.text_input("Appoinment Id ")
  name = st.text_input("Name ")
  r1 = c4.find()
  c = 0
  for i in r1:
    if i['aid'] == aid:
      if i['name'] == name:
        c+=1
  a1 = st.checkbox('proceed')
  

  if a1:
    if(c==1):
      r = st.selectbox('Select any one',['select','Reshedule','Cancel'])
      if r =='Reshedule':
        from reshedule import reshedule
        reshedule(aid)
      if r =='Cancel':
        from cancel import cancel
        cancel(aid)
    else:
      st.error('Invalid Appoinmnet id or name')
