from pymongo import MongoClient
import numpy as np
import pandas as pd
import streamlit as st
import time

client = MongoClient('mongodb+srv://dbuser2:covac@eshop.m8tu7.mongodb.net/test')
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
# mypdf= FPDF()
# mypdf.add_page()
# mypdf.set_font("Arial",size=18)
# mypdf.cell(200,10,txt="Wingardium leviosa",ln=1,align="C")
# mypdf.output("keerthu.pdf")

# from covid import Covid
# from covid_india import states
# a = states.getdata()
# states = ['Tamil Nadu']
# for i in a:
#     states.append(i)
# sta = st.selectbox('statewiese data',states)

# for j in a[sta]:
#     print(j)
#     print(a[sta][j])
#     #st.write(i," : ",a[sta][j])
    
# #print(states.getdata('Total'))
# ke="This is a sample scrolling text that has scrolls in the upper direction."
# st.markdown(f"<marquee width='60%' direction='right' height='100px'>{ke}</marquee>",unsafe_allow_html=True)
# ke=st.image("test.jpg")
# st.markdown(f"<marquee width='60%' direction='right' height='100px'>{ke}</marquee>",unsafe_allow_html=True)

# "<style>
# '.parallax{("background-image: url("test.jpg") min-height: "500px" background-attachment: "fixed" background-position: "center" background-repeat: "no-repeat" background-size: "cover" )"
# }'
# </style>"

# <!-- Container element -->
# <div class="parallax"></div>",unsafe_allow_html=True)