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

def faq():
    option = st.selectbox('Frequently asked questions',['Select your questions','About the vaccine','Who can get vaccinated ?','After vaccination','Register for vaccination'])
    
    if option=="About the vaccine":
        e1 = st.beta_expander("Which COVID-19 vaccines are licensed in India?")
        e1.write("Two vaccines were granted emergency use authorization by the Central Drugs Standard Control Organization (CDSCO) in India, Covishield® (AstraZeneca's vaccine manufactured by Serum Institute of India) and Covaxin® (manufactured by Bharat Biotech Limited). Sputnik - V has been granted EUA in the month of April 2021.")
        e2 = st.beta_expander("What technology has been used in development of the currently available two vaccines in India?")
        e2.write("Covishield® vaccine, manufactured by the Serum Institute of India, is a Viral Vector-based Technology which is also used to manufacture Ebola vaccine.")
        e2.write("Covaxin® vaccine, manufactured by the Bharat Biotech, is a Whole-virion Inactivated Coronavirus Vaccine which is also used to manufacture vaccines like Influenza, Rabies and Hepatitis- A.")
        e3 = st.beta_expander("What is the dose schedule of both the vaccines?")
        e3.write("The time interval between two doses of the Covishield vaccine has been extended from four-eight weeks to 12-16 weeks. The second dose of Covaxin can be taken four to six weeks after the first.")
    if option=="Who can get vaccinated ?":
        e1 = st.beta_expander("Can a person presently having COVID-19 (confirmed or suspected) infection be vaccinated?")
        e1.write("Person with confirmed or suspected COVID-19 infection may increase the risk of spreading the same to others at vaccination site. For this reason, infected individuals should defer vaccination for 14 days after symptoms resolution.")
        e2=st.beta_expander("What are the constrains for getting vaccinated?")
        e2.write("People with allergies But people with a severe allergic reaction (anaphylaxis) to any component of the COVID-19 vaccine or injectable (intramuscular or intravenous) medication should NOT receive the vaccine.")
        e2.write("Pregnant & Lactating women have not been part of any COVID-19 vaccine clinical trial so far. Therefore, women who are pregnant or not sure of their pregnancy; and lactating women should not receive COVID-19 vaccine at this time")
        e3=st.beta_expander("What is the age limit for vaccination in India ?")
        e3.write("In India, the age limit to get covid vaccination is 18")
    if option=="After vaccination":
        e1 = st.beta_expander("Do I need to use the mask/other COVID-19 appropriate precautions after receiving the vaccine?")
        e1.write("Yes, it is absolutely necessary that everyone who has received the COVID-19 vaccine should continue to follow the COVID-19 appropriate behaviour and hand sanitization to protect themselves and those around from spreading the infection.")
        e2 = st.beta_expander("What precautions I need to take after receiving the vaccine?")
        e2.write("Both the vaccines are safe but in case of any discomfort or complaint, ask the beneficiary to visit the nearest health facility and/or call the health worker whose phone number is given in the Co-WIN SMS received after vaccination.")
        e3=st.beta_expander("In how many days will the vaccination create an adequate immune response and protection?")
        e3.write("Adequate immune response takes 2-3 weeks after completion of entire vaccination schedule i.e., after the second dose of COVISHIELD® and COVAXIN®.")
    if option=="Register for vaccination":
        st.write("Please go through the guidelines and click agree for registration")
        a=st.checkbox("agree")
        if a:
            latest_iteration = st.empty()
            bar = st.progress(0)
            for i in range(100):
                latest_iteration.text('Redirecting to registration portal....')
                bar.progress(i + 1)
                time.sleep(0.01)
            st.success("Select Appoinment from Menu to book an appoinment now")
