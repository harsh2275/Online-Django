from asyncio.windows_events import NULL
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from .temp import *
from datetime import datetime
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserChangeForm
import mysql.connector as sql
fn=""
ln=""
s=""
em=""
pwd=""
ph_num=""
email=""
passwd=""
# Create your views here.


def home(request):
    return render(request, 'booking/home.html') 

def signin(request):
    global email,passwd
    if request.method=="POST":
        m=sql.connect(host = "localhost" , user="root" , passwd= "855fc1@NOV25" , database = "techfest")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                passwd=value 
            
        c="select * from users where email='{}' and password='{}'".format(email,passwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        #print(t)
        if t==():
            return render(request,'booking/error.html')
        else:
            return HttpResponseRedirect('ticket%20booking')
            return render(request,"booking/d_booking.html")
    
    """else :
        print("nope")"""

    return render(request, 'booking/signin.html')


def signup(request):
    global fn,ln,s,em,pwd,ph_num
    if request.method=="POST":
        m=sql.connect(host = "localhost" , user="root" , passwd= "855fc1@NOV25" , database = "techfest")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstName":
                fn=value
            if key=="lastName":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value 
            if key=="phone":
                ph_num=value
                ph_num=int(ph_num)
        
        c="select * from users where email='{}'".format(em)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        print(t)
        if t==():
            c="insert into users(first_name,last_name,sex,email,password,phone) Values('{}','{}','{}','{}','{}',{})".format(fn,ln,s,em,pwd,ph_num)
            cursor.execute(c)
            m.commit()
            return render(request, 'booking/welcome.html')
            
        else:
            return render(request,'booking/error.html')
        

    return render(request, 'booking/signup.html')
    #return render(request, 'booking/signin.html')


def fare_calculation(request):
    return render(request, 'booking/ticket.html')

def ticket_booking(request):
    lis=[]
    lis_nam=[]
    tic=[]
    print (email)
    if request.method=="POST":
        m=sql.connect(host = "localhost" , user="root" , passwd= "855fc1@NOV25" , database = "try")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if value=="":
                break
            else : 
                if key=="date":
                    date_t = value
                if key=="time":
                    time_t = value
                if key=="name1":
                    name1 = value
                    lis_nam.append(name1)
                if key=="age1":
                    age1 = value
                    txt1 = name1 + "_" + str(age1) + "_" + date_t + time_t + "_" + str(datetime.now()) +"_"+ email
                    tic.append("1")
                    lis.append(txt1)
                if key=="yes1":
                    yes1 = value
                if key=="gender1" :
                    gender1 = value
                
                if key=="name2" and value!="":
                    name2 = value
                    lis_nam.append(name2)
                if key=="age2" and value!="":
                    age2 = value
                    txt2 = name2 + "_" + str(age2) + "_" + date_t + time_t + "_" + str(datetime.now()) +"_"+ email
                    tic.append("2")
                    lis.append(txt2)
                if key=="yes2":
                    print("hoo4")
                    yes2 = value
                if key=="gender2" : 
                    print("hoo5") 
                    gender2 = value

                if key=="name3" and value!="":
                    name3 = value
                    lis_nam.append(name3)
                if key=="name3" and value!="":
                    name3 = value
                if key=="age3" and value!="":
                    age3 = value
                    txt3 = name3 + "_" + str(age3) + "_" + date_t + time_t + "_" + str(datetime.now()) +"_"+ email
                    tic.append("3")
                    lis.append(txt3)
                if key=="yes3":
                    yes3 = value
                if key=="gender3" : 
                    gender3 = value

                if key=="name4" and value!="":
                    name4 = value
                    lis_nam.append(name4)
                if key=="age4" and value!="":
                    age4 = value
                    txt4 = name4 + "_" + str(age4) + "_" + date_t + time_t + "_" + str(datetime.now()) +"_"+ email
                    tic.append("4")
                    lis.append(txt4)
                if key=="yes4":
                    yes4 = value
                if key=="gender4" : 
                    gender4 = value

                if key=="name5" and value!="":
                    name5 = value
                    lis_nam.append(name5)
                if key=="age5" and value!="":
                    age5 = value
                    txt5 = name5 + "_" + str(age5) + "_" + date_t + time_t + "_" + str(datetime.now()) +"_"+ email
                    tic.append("5")
                    lis.append(txt5)
                if key=="yes5":
                    yes5 = value
                if key=="gender5" : 
                    gender5 = value

        if "1" in tic:
            c="insert into main(Name,Age,Email,Date,Time,Disabality,Source,HashValue) Values('{}',{},'{}','{}','{}','{}','{}','{}')".format(name1,age1,email,date_t,time_t,yes1,gender1,txt1)
            cursor.execute(c)
            m.commit()
        
        if "2" in tic:
            c="insert into main(Name,Age,Email,Date,Time,Disabality,Source,HashValue) Values('{}',{},'{}','{}','{}','{}','{}','{}')".format(name2,age2,email,date_t,time_t,yes2,gender2,txt2)
            cursor.execute(c)
            m.commit()
        
        
        if "3" in tic:
            c="insert into main(Name,Age,Email,Date,Time,Disabality,Source,HashValue) Values('{}',{},'{}','{}','{}','{}','{}','{}')".format(name3,age3,email,date_t,time_t,yes3,gender3,txt3)
            cursor.execute(c)
            m.commit()

        
        if "4" in tic:
            c="insert into main(Name,Age,Email,Date,Time,Disabality,Source,HashValue) Values('{}',{},'{}','{}','{}','{}','{}','{}')".format(name4,age4,email,date_t,time_t,yes4,gender4,txt4)
            cursor.execute(c)
            m.commit()
        
        
        if "5" in tic:
            c="insert into main(Name,Age,Email,Date,Time,Disabality,Source,HashValue) Values('{}',{},'{}','{}','{}','{}','{}','{}')".format(name5,age5,email,date_t,time_t,yes5,gender5,txt5)
            cursor.execute(c)
            m.commit()
        func(email,lis,lis_nam)
        return render(request, 'booking/sucessful.html')
    return render(request, 'booking/d_booking.html')