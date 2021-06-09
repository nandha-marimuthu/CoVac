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
c6 = db["kee's roughwork"]


# abcd = pd.DataFrame(list(c2.find()))
# st.table(abcd)
# from reportlab.pdfgen import canvas
# from reportlab.pdfgen import canvas 
# pdf = canvas.Canvas(fileName)
# pdf.setTitle(documentTitle)

# from fpdf import FPDF
# #obj
# mypdf= FPDF()
# #create
# mypdf.add_page()
# #font
# mypdf.set_font("Arial",size=18)
# mypdf.cell(200,10,txt="Magic",align="C")
# mypdf.output("keerthu.pdf")


