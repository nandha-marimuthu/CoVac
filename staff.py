from pymongo import MongoClient
import numpy as np
import pandas as pd
import streamlit as st
import smtplib
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')
db = client['Covac']
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']
c6 = db["kee's roughwork"]
def staff():
    st.markdown("""# Covac Staff Portal""")
    n = st.sidebar.text_input('staffname')
    p = st.sidebar.text_input('passowrd',type="password")
    v1=c1.find({'staff':n,'password':p})
    c=0
    for i in v1:
        c2=i['cname']
        if n==i['staff']:
            if p==i['password']:
                c+=1
    if c==1:
        dict1={}
        c2,"STAFF PORTAL"
        "Welcome back",n,"!"
        option = st.selectbox('Menu',['Select','Appoinments','Vaccination Entry'])
        if option=='Appoinments':
            s=st.radio("Bookings",("Select","Overall","Datewise"))
            if s=="Overall":
                abcd = c4.find({'center':c2})
                n,slot,age,date1=[],[],[],[]
                for i in abcd:
                    n.append(i['name'])
                    slot.append(i['slot'])
                    age.append(i['age'])
                    date1.append(i['date'])
                table=pd.DataFrame({'name':n,'age':age,'slot':slot,'date':date1})
                st.table(table)
            elif s=="Datewise":
                mydate=st.text_input("dd-mm-yyyy")
                view=st.checkbox("View")
                if view:
                    abcd = c4.find({'center':c2,'date':mydate})
                    n,slot,age,date1=[],[],[],[]
                    for i in abcd:
                        n.append(i['name'])
                        slot.append(i['slot'])
                        age.append(i['age'])
                        date1.append(i['date'])
                    table=pd.DataFrame({'name':n,'age':age,'slot':slot,'date':date1})
                    st.table(table)
        elif option=='Vaccination Entry':
            n1=st.text_input("Name")
            a1=st.text_input("Aadhar")
            aid=st.text_input("Appoinment ID")
            v2=c4.find({'name':n1,'aadhar':a1})
            check=st.checkbox("Check")
            if check:
                xyz=0
                for j in v2:

                    xyz+=1
                    if xyz==1:
                        st.write(n1,"has been vaccinated")
                        dict1={'name':n1,'aadhar':a1,'centre':c2,'staff':n,'status':'vaccinated','aid':aid}
                        abc=c5.insert_one(dict1)
                        #mail(name,mailid)
                        del1=c4.delete_one({'aadhar':a1})
                        sender = 'tnvaccinationportal@gmail.com'
                        rec = 'keerthanav3103@gmail.com'
                        password = 'vaccine123'
                        msg=n1+" has been vaccinated"
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(sender, password)
                        server.sendmail(sender, rec, msg)

                    else:
                        "Invalid name or aadhar number"

    elif n=="" or  p=="":"Please login to continue"
    else:"Invalid credentials"  

