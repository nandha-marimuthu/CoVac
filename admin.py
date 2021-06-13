import streamlit as st
from pymongo import MongoClient, collection
from dashboard import dashboard 
client = MongoClient('mongodb+srv://dbuser2:covac@eshop.m8tu7.mongodb.net/test')

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


def edit_centers():
    #print("Enter A for add and R for remove")
    selection=st.selectbox('Power of Admin',['Choose an option','Add centers','Remove centers'])
    #s = input("Enter:").strip()
    if selection == "Add centers":
        a = c1.find()
        #cid= a[c1.count_documents({})-1]['_id']+1

        cname = st.text_input("Hospital name")
        region = st.text_input("Region")
        pincode = st.text_input("Pincode")
        staffname=st.text_input("Staffname")
        password=st.text_input("password")
        #tid=int(input("Enter center:"))
        add=st.button("ADD CENTER")
        if add==True:
            data={"cname":cname,"region":region,"pincode":int(pincode),"staff":staffname,"password":password}
            c1.insert_one(data)
            st.success("center added Sucessfully")

        
    elif selection=="Remove centers":
        #t=int(input("Enter center id:"))
        reg=c1.find()
        x=[]
        for i in reg:
            x.append(i['region'])
        region=dup(x)

        sreg=st.selectbox("Center situated regions",region)
        b = c1.find({'region':sreg})
        y = []
        for i in b:
            y.append(i['cname'])
        shosp=st.selectbox("Avaialable centers",y)
        dcenter=st.button("Remove Center")
        if dcenter==True:
            c1.delete_one({"cname":shosp})
            st.success("Center removed Successfully")


def admin_login():
    admin_user=st.sidebar.text_input("Admin Name")
    admin_pswd=st.sidebar.text_input("Admin Password",type='password')
    check=st.sidebar.checkbox("Login")
    f=0
    if check:
        a1 = c2.find({'name':admin_user})
        p1=c2.find({'password':admin_pswd})
        for i in a1:
            for j in p1:
                f=1
            if f==1:
                st.success("Welcome back {}".format(admin_user))
                edit_centers()
            elif admin_user=="" or  admin_pswd=="":"Please login to continue"
            else:st.error("Invalid admin credentials")
