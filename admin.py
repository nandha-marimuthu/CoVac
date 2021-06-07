import streamlit as st
from pymongo import MongoClient, collection
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['Covac']
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']

def admin_login():
    st.title("Welcome to admin portal\n")
    #admin_id=input("Adminname : ")
    #pwd=input("Password : ")
    admin_user=st.text_input("Admin Name")
    admin_pswd=st.text_input("Admin Password",type='password')
    choice=st.button("Login")
    f=0
    a1 = c2.find({'name':admin_user})
    p1=c2.find({'password':admin_pswd})
    c = 0
    for i in a1:
      for j in p1:
        f=1
   
    if f==1:
        if choice==True:
             st.success("Welcome back {}".format(admin_user))
    
    if choice == True:
        if f==0:
            st.error("Invalid admin member '{}'".format(admin_user))

    selection=st.selectbox('Power of Admin',['Add centers','Remove centers','Review staff'])
    if selection=='Add centers':
        st.header("This help you to add some centers")

    
        

    

          
if __name__ == "__main__":
        admin_login()
