from pymongo import MongoClient
import numpy as np
import pandas as pd
import streamlit as st
import smtplib
import datetime
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')
db = client['Covac']
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

def staff():
    st.markdown("""# CovaC Staff Portal""")
    n = st.sidebar.text_input('staffname')
    p = st.sidebar.text_input('password',type="password")
    v1=c1.find({'staff':n,'password':p})
    c=0
    for i in v1:
        c2=i['cname']
        region=i['region']
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
                    dat=j['date']
                    slot1=j['slot']
                    age=j['age']
                    xyz+=1
                

                    if xyz==1:
                        st.write(n1,"has been vaccinated")
                        dict1={'name':n1,'aadhar':a1,'centre':c2,'region':region,'age':age,'staff':n,'date':dat,'slot':slot1,'status':'vaccinated','aid':aid}
                        abc=c5.insert_one(dict1)                       
                        today = datetime.date.today()
                        tomorrow = today + datetime.timedelta(days=42)
                        cont="You have been vaccinated "+"\nDon't forget to take your second dose on "+str(tomorrow)
                        del1=c4.delete_one({'aadhar':a1})
                        from pdfemail import pdf_mail
                        pdf_mail(dict1,cont)

                    else:
                        "Invalid name or aadhar number"

    elif n=="" or  p=="":"Please login to continue"
    else:"Invalid credentials"  



