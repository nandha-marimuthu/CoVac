from pymongo import MongoClient
import numpy as np
import pandas as pd
import streamlit as st
import time
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')
db = client['Covac']

c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']

def staff():
    

    