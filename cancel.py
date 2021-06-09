from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient
from capt import capt

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
c6 = db['cancelled']

def cancel(aid):
  st.header('Cancel')
  a = capt()
  st.image('capt.png')

  otp = st.text_input('Enter the CAPTCHA')
  b = st.button('cancel')
  if b:
    if otp and otp == a:
      data={'aid':aid}
      r = c4.find(data)
      for i in r:
        c6.insert_one(i)
      c4.delete_one(data)
      st.success('your appionment for the id '+aid+' is cancelled')

    
    else:
      st.error('Wrong captcha')
