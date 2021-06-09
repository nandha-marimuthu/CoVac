from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient
import random
import datetime

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

def reshedule(aid):
  st.title('Reshedule')
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(days=2)
  d1 = st.date_input('Date', tomorrow)
  d = str(d1)
  slot = st.select_slider('Time Slot',['10AM','1PM','4PM'])
  data = {'aid':aid}
  a = st.button('Reshedule')
  if a:
    # c4.update_one(data,{"$set":{}})
    c4.update_one(data,{"$set":{"status":'resheduled',"date":d,'slot':slot}})
    st.success('Your vaccination appoinment reshduled at '+d+' at '+slot+' slot')