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

option = st.sidebar.selectbox('Menu',['Home','Appointment','Cancel/Reschedule','Staff','Admin','Dashboard','About'])

if option == 'Home':
  v=c5.count_documents({})
  ke="Don't forget to vaccinate ! Stay home stay safe !"+ " People vaccinated through CovaC : "+str(v)
  col1, col2, col3 = st.beta_columns([1,6,1])

  with col1:
    st.write("")

  with col2:
    st.image('vaccination.png',width=600)

  with col3:
    st.write("")
  
  col1, col2, col3 = st.beta_columns([1,8,1])

  with col1:
    st.write("")

  with col2:
    st.markdown(f"<marquee width='100%' direction='left' height='40px'>{ke}</marquee>",unsafe_allow_html=True)

  with col3:
    st.write("")
 
 
  # des1="CovaC - Vaccination Portal"
  # st.markdown(f"<h1 style='text-align: center; color: FireBrick;'>{des1}</h1>",unsafe_allow_html=True)
  
  print(v)
  from covid import Covid

  from covid_india import states
  a = states.getdata()
  states = []
  for i in a:
    states.append(i)
  st.title('Covid Information')
  sta = st.selectbox('statewiese data',states)
  ac,cu,de=a[sta]["Active"],a[sta]["Cured"],a[sta]["Death"]
  st.write('Total: ',ac+cu+de)
  st.write('Active: ',ac)
  st.write('Cured: ',cu)
  st.write('Death: ',de)
  st.title('FAQ')
  from faq import faq
  faq()

if option == 'Appointment':
  from appoinment import login
  login()
if option == 'Cancel/Reschedule':
  from recan import recan
  recan()
if option == 'Staff':
  from staff import staff
  staff()
if option == 'Admin':
  st.title("CovaC Admin Portal")
  from admin import admin_login
  admin_login()
if option == 'About':
  from about import about
  about()
if option == 'Dashboard':
  from dashboard import dashboard
  dashboard()

  





  



  

  
