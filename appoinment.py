from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient
import datetime
import random
import secrets
import string

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

def appoinment(name,aadhar):

  a = c1.find()
  x=[]
  for i in a:
    x.append(i['region'])
  x = dup(x)
  

  age = st.slider('How old are you?', 18, 60, 18)
  gender = st.radio("Select Gender: ", ('Male', 'Female','Transgender'))
  email = st.text_input('Email')
  region = st.selectbox('Select Any Region',x)

  b = c1.find({'region':region})
  y = []
  for i in b:
    y.append(i['cname'])

  center = st.selectbox('Hospitals',y)
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(days=2)
  d = st.date_input('Date', tomorrow)

  if d == today:
    'Please enter a valid date'
  slot = st.select_slider('Time Slot',['10AM','1PM','4PM'])
  d

  if st.button('Book Appoinment'):
    num = 4
    aid = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
    st.success('Your Appoinment is Booked & Appoinment Id is '+aid)
    
  


  







# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# start_date = st.date_input('Start date', today)
# end_date = st.date_input('End date', tomorrow)
# if start_date < end_date:
#     st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
# else:
#     st.error('Error: End date must fall after start date.')