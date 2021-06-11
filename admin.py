import streamlit as st
from pymongo import MongoClient, collection
from dashboard import dashboard 
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


def edit_centers():
    #print("Enter A for add and R for remove")
    selection=st.selectbox('Power of Admin',['Choose an option','Add centers','Remove centers'])
    #s = input("Enter:").strip()
    if selection == "Add centers":
        a = c1.find()
        #cid= a[c1.count_documents({})-1]['_id']+1

        cname = st.text_input("Enter name of hospital:")
        region = st.text_input("Enter the region:")
        pincode = st.text_input("Enter the pincode:")
        staffname=st.text_input("Enter the staff name for incharge")
        password=st.text_input("Enter the password")
        #tid=int(input("Enter center:"))
        add=st.button("ADD CENTER")
        if add==True:
            data={"cname":cname,"region":region,"Pincode":pincode,"staff":staffname,"password":password}
            c1.insert_one(data)
            st.success("center added to the list {}".format(cname))

        
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
        st.title("Welcome to admin portal\n")
    #admin_id=input("Adminname : ")
    #pwd=input("Password : ")
        admin_user=st.sidebar.text_input("Admin Name")
        admin_pswd=st.sidebar.text_input("Admin Password",type='password')
        choice=st.sidebar.checkbox("Login")
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

        if choice==True:
            if admin_user  and admin_user in a1:
                if admin_pswd and admin_pswd in p1:
                    edit_centers()




    
def main():
        menu=['Pick your choice','Admin','Dashboard']
        mc=st.sidebar.selectbox("Menus",menu)
        if mc=='Pick your choice':
            st.title("Admin And Dashboard page process")
            st.success("WELCOME TO COVAC -> AN APPOINTMENT BOOKING PORTAL")
        if mc=='Admin':
            admin_login()
        #edit_centers()
        
        if mc=='Dashboard':
            dashboard()



             
if __name__ == "__main__":
        main()
       
