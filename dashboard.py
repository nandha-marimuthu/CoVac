import streamlit as st
import pandas as pd
from pymongo import MongoClient, collection
import plotly.graph_objects as go

client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['Covac']
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']
c6 = db['cancelled']


def dup(x):
    z=[]
    for i in x:
        if i not in z:
            z.append(i)
    return z

def dashboard():
    #st.title("Welcome to Covac Dashboard")
    des="Welcome to CovaC Dashboard"
    st.title(des)
    vis=True
    region=[]
    name=[]
    cname=[]
    age=[]
    gender=[]
    region1=[]
    t1=c1.find()
    for i in t1:
        region.append(i['region'])
        cname.append(i['cname'])
                
    t2=c5.find()
    for i in t2:
        name.append(i['name'])
        age.append(i['age'])
        region1.append(i['region'])
        


    if vis ==True:
        choice=st.selectbox('Pick your view',['choose one from the dropdown','Table','Display count','Bar Chart','Pie Chart'])
        if choice=='Table':
            df=pd.DataFrame({'Center Name':cname,'Region':region})
            st.header("Vaccination centers in various Region")
            st.dataframe(df)
            st.header("People Vaccinated")
            df1=pd.DataFrame({'Name':name,'Age':age,'location':region1})
            st.dataframe(df1)
            
        if choice=='Display count':
            select=st.selectbox('Classification',['select one from the below options','Count of people Vaccinated','Rate of appointment booking'])
            if select=='Count of people Vaccinated':
               ch=st.selectbox('Types of Classification',['region based','center based','gender based'])
               region=dup(region)
                
               if ch=='region based':
                    option1=st.radio('Regions',region)
                    count1=0
                    count1= c5.find({'region':option1}).count()
                    st.success("People Vaccinated in {} are {}".format(option1,count1))

               if ch=='center based':
                    option1=st.radio('Centers',dup(cname))
                    count1=0
                    count1=c5.find({'centre':option1}).count()
                    st.success("People Vacinated in {} are {}".format(option1,count1))

               if ch=='gender based':
                option1=st.radio('Gender',dup(gender))
                count1=0
                count1=c3.find({'gender':option1}).count()
                st.success("No. of {} vaccinated {}".format(option1,count1))


            if select=='Rate of appointment booking':
                option2=st.radio('Status of Appointments',['Booked appointments','cancelled appointments','rescheduled appointments'])
                if option2=='Booked appointments':
                    count2=c4.find({'status':'processing'}).count()
                    st.success("Total appointments booked {}".format(count2))
                
                if option2=='cancelled appointments':
                    count2=c6.find({'status':'processing'}).count()
                    st.success("Total appointments cancelled {}".format(count2))

                if option2=='rescheduled appointments':
                    count2=c6.find({'status':'resheduled'}).count()
                    st.success("Total appointments rescheduled {}".format(count2))

                  

        if choice=='Bar Chart':
            select=st.selectbox('Classification',['select one from the below options','Count of people Vaccinated','Rate of appointment booking'])
            if select=='Count of people Vaccinated':
                ch=st.radio('Classification',['Date wise','Region wise','Center wise','Age wise'])
                if ch=='Date wise':
                  a = c5.find()
                  dat=[]
                  vac=[]
                  for i in a:
                      dat.append(i['date'])
                  dat=dup(dat)
            
                  for i in dat:
                      vac.append(c5.find({'date':i}).count())


                  df = pd.DataFrame({'date': dat,'Vaccinated': vac})

                  df = df.rename(columns={'date':'index'}).set_index('index')
                  st.bar_chart(df)

                if ch=='Region wise':
                    a=c5.find()
                    reg=[]
                    vac=[]
                    for i in a:
                        reg.append(i['region'])
                    reg=dup(reg)

                    for i in reg:
                        vac.append(c5.find({'region':i}).count())
                    df=pd.DataFrame({'Region':reg,'Vaccinated':vac})
                    df = df.rename(columns={'Region':'index'}).set_index('index')
                    st.bar_chart(df)

                
                if ch=='Center wise':
                    a=c5.find()
                    cen=[]
                    vac=[]
                    for i in a:
                        cen.append(i['centre'])
                    cen=dup(cen)

                    for i in cen:
                        vac.append(c5.find({'centre':i}).count())
                    df=pd.DataFrame({'Centers':cen,'Vaccinated':vac})
                    df = df.rename(columns={'Centers':'index'}).set_index('index')
                    st.bar_chart(df)

                if ch=='Age wise':
                    a=c5.find()
                    age=[]
                    vac=[]
                    for i in a:
                        age.append(i['age'])
                    age=dup(age)

                    for i in age:
                        vac.append(c5.find({'age':i}).count())
                    df=pd.DataFrame({'Age':age,'Vaccinated':vac})
                    df = df.rename(columns={'Age':'index'}).set_index('index')
                    st.bar_chart(df)


            if select=='Rate of appointment booking':
                count1=c4.find({'status':'processing'}).count()
                count2=c6.find({'status':'processing'}).count()
                count3=c6.find({'status':'resheduled'}).count()

                df=pd.DataFrame({'Rate':['Booking','cancelled','Rescheduled'],'Count':[count1,count2,count3]})
                df = df.rename(columns={'Rate':'index'}).set_index('index')
                st.bar_chart(df)

        if choice=='Pie Chart':

            select=st.selectbox('Classification',['select one from the below options','Count of people Vaccinated','Rate of appointment booking'])
            if select=='Count of people Vaccinated':
                ch=st.radio('Classification',['Region wise','Center wise','Age wise'])
                if ch=='Region wise':
                    a=c5.find()
                    reg=[]
                    vac=[]
                    for i in a:
                        reg.append(i['region'])
                    reg=dup(reg)

                    for i in reg:
                        vac.append(c5.find({'region':i}).count())
                    
                    fig = go.Figure(data=[go.Pie(labels=reg, values=vac)])
                    st.plotly_chart(fig)
                
                if ch=='Center wise':
                    a=c5.find()
                    cen=[]
                    vac=[]
                    for i in a:
                        cen.append(i['centre'])
                    cen=dup(cen)

                    for i in cen:
                        vac.append(c5.find({'centre':i}).count())


                    fig = go.Figure(data=[go.Pie(labels=cen, values=vac)])
                    st.plotly_chart(fig)

                if ch=='Age wise':
                    a=c5.find()
                    age=[]
                    vac1=[]
                    vac2=[]
                    vac3=[]
                    for i in a:
                        a1=i['age']
                        age.append(i['age'])
                    age=dup(age)

                    for i in age:
                        if a1>=18 and a1<=45:
                            vac1.append(c5.find({'age':i}).count())
                        if a1>45 and a1<=60:
                            vac2.append(c5.find({'age':i}).count())
                        if a1>60:
                            vac3.append(c5.find({'age':i}).count())
                    vac=[]
                    vac.extend(vac1)
                    vac.extend(vac2)
                    vac.extend(vac3)




                    fig = go.Figure(data=[go.Pie(labels=['Between 18-45','Between 45-60','greater than 60'], values=vac)])
                    st.plotly_chart(fig)



            
            if select=='Rate of appointment booking':
                Rate=['Booking','cancelled','Rescheduled']
                count1=c4.find({'status':'processing'}).count()
                count2=c6.find({'status':'processing'}).count()
                count3=c6.find({'status':'resheduled'}).count()
                Count=[count1,count2,count3]

                fig = go.Figure(data=[go.Pie(labels=Rate, values=Count)])
                st.plotly_chart(fig)
            #df = pd.DataFrame({'Count':[count1,count2,count3]},index=['Booking','cancelled','Rescheduled'])
            #plot = df.plot.pie(y='Count', figsize=(5, 5))
            #st.image(plot,width=100)




            


                

            



                  

            