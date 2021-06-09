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
  d1 = st.date_input('Date', tomorrow)
  d = str(d1)

  if d == today:
    'Please enter a valid date'
  slot = st.select_slider('Time Slot',['10AM','1PM','4PM'])
  z = c4.find({'center':center,'date':d,'slot':slot}).count()
  st.write(str(20-z)+' slots are left')
  if z>=20:
    st.warning('Choose other Hospital')

  if z<20 and st.button('Book Appoinment'):
    num = 4
    aid = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    st.success('Your Appoinment is Booked & Appoinment Id is '+aid)
    cont = "Don't forget to vaccinate !"
    pd = {'name':name,'aadhar':aadhar,'age':age,'region':region,'gender':gender,'email':email}
    ap = {'aid':aid,'name':name,'aadhar':aadhar,'age':age,'center':center,'date':d,'slot':slot,'status':'processing'}
    from pdfemail import pdf_mail
    pdf_mail(ap,cont)
    c4.insert_one(ap)
    print(ap)
    c3.insert_one(pd)
    
    
    
    st.success('Vaccination details is sent to your registered mailid')


def login():
  st.title('Appoinment')
  name = st.text_input('Name')
  aadhar = st.text_input('Aadhar No')
  a = st.checkbox('procced')
  a1 = c4.find()
  a2 = c5.find()
  c = 0
  for i in a1:
    if i['name'] == name:
      if i['aadhar'] == aadhar:
        c+=1
  for i in a2:
    if i['name'] == name:
      if i['aadhar'] == aadhar:
        c+=1
  if a:
    if (c==0):
      
      appoinment(name,aadhar)
    else:
      st.error('Already Booked')
 


  







