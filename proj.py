from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import MySQLdb


def ok():
    unname=e1.get()
    password=e2.get()

    if(unname == "" and password == "") :
        messagebox.showinfo("","Blank not found")
    
    elif(unname=="Team" and password=="Project"): 
        root =tk.Tk()  
        root.geometry("800x400")
        root.title("Dashboard")
        # Data base for Number of patient
        try:
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
            cur=mycon.cursor() 
            query="select * from patientd"
            cur.execute(query)
            mr=cur.fetchall() 

        except:
            print("Error Occurred When Fetching Your Data!!!!!!!!!!!!!!!!")
           # label of Dashboard
        Label(root,text="  Welcome to DashBoard  ",font=('Arial Rounded MT Bold',20)).place(x=230,y=8)
           # label of Dashboard Register
        Label(root,text="Total Patient Register",font=('Cambria',14)).place(x=70,y=70)
        Label(root,text=len(mr),font=('Segoe UI',20),width=10,height=1).place(x=80,y=95)
       
        # Appointements
        try:
    
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
            query="SELECT * FROM appoin"
            cur=mycon.cursor()
            cur.execute(query)
            ss=cur.fetchall()
        except:
            print("Error while fetching the Data! ")
            print("Try Again!!!!!!!")
        Label(root,text="Appointements",font=('Cambria',14)).place(x=325,y=200)
        Label(root,text=len(ss),font=('Segoe UI',20),width=10,height=1).place(x=320,y=225)

         # label of dashboard bill
        try:

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
            query="SELECT * FROM pdata"
            cur=mycon.cursor()
            cur.execute(query)
            rw=cur.fetchall()
        except:
            print("Error while fetching value")
        Label(root,text="Bill Genrated",font=('Cambria',14)).place(x=560,y=70)
        Label(root,text=len(rw),font=('Segoe UI',20),width=10,height=1).place(x=550,y=95)
         # refresh Button
        def h1():

            try:

                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                cur=mycon.cursor() 
                query="select * from patientd"
                cur.execute(query)
                pr=0
                tdata=cur.fetchall()
                # label of Dashboard
                Label(root,text="  Welcome to DashBoard  ",font=('Arial Rounded MT Bold',20)).place(x=230,y=8)
                # label of Dashboard Register
                Label(root,text="Total Patient Register",font=('Cambria',14)).place(x=70,y=70)
                Label(root,text=len(tdata),font=('Segoe UI',20),width=10,height=1).place(x=80,y=95)
                # label of dashboard bill
                Label(root,text="Bill Genrated",font=('Cambria',14)).place(x=560,y=70)
                Label(root,text=len(tdata),font=('Segoe UI',20),width=10,height=1).place(x=550,y=95)
                try:
                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                    query="SELECT * FROM appoin"
                    cur=mycon.cursor()
                    cur.execute(query)
                    ss=cur.fetchall()
                    Label(root,text="Appointements",font=('Cambria',14)).place(x=325,y=200)
                    Label(root,text=len(ss),font=('Segoe UI',20),width=10,height=1).place(x=320,y=225)
        
                except:
                    print("Error while fetching the Data! ")
                    print("Try Again!!!!!!!")
                
                try:

                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                    query="SELECT * FROM pdata"
                    cur=mycon.cursor()
                    cur.execute(query)
                    rw=cur.fetchall()
                except:
                    print("Error while fetching value")
                Label(root,text="Bill Genrated",font=('Cambria',14)).place(x=560,y=70)
                Label(root,text=len(rw),font=('Segoe UI',20),width=10,height=1).place(x=550,y=95)

            except:
                print("Error Occurred When Fetching Your Data!!!!!!!!!!!!!!!!")

        Button(root,text="Refresh",height=1,width=15,bg="skyblue",command=h1,font=('Arial',14)).place(x=310,y=360)

        def dataget():
            top=tk.Tk()
            top.geometry("800x400")
        # Add patient Data
            Label(top,text="Add Patient",font=('Arial Rounded MT Bold',20)).place(x=280,y=8)
            # lable name
            Label(top,text="Name",font=('Cambria',20)).place(x=30,y=40)
            g1=Entry(top)
            g1.place(x=120,y=50)
            Label(top,text="Age",font=('Cambria',20)).place(x=450,y=40)
            g2=Entry(top)
            g2.place(x=520,y=50)
            
            Label(top,text="Gender",font=('Cambria',20)).place(x=25,y=100)
            g3=Entry(top)
            g3.place(x=120,y=110)

            Label(top,text="Mobile",font=('Cambria',20)).place(x=430,y=100)
            g4=Entry(top)
            g4.place(x=520,y=110)

            Label(top,text="Address",font=('Cambria',20)).place(x=25,y=200)
            g5=Entry(top)
            g5.place(x=140,y=215,width=600)

            Button(top,text="Back",font=('Cambria',20),command=top.destroy,bg="skyblue").place(x=280,y=360)
            def hero():
                try:
                    name=g1.get()
                    age=g2.get()
                    gen=g3.get()
                    mobo=g4.get()
                    add=g5.get() 
                
                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                   # print("ok1")
                    query="""insert into patientd (name,age,gen,mobile,address) VALUES ('{}','{}','{}','{}','{}');""".format(name,age,gen,mobo,add)
                    #print("ok2")
                    cur=mycon.cursor()
                   # print("ok3")
                    cur.execute(query)
                    mycon.commit()
                    cur.close()
                    messagebox.showinfo("","Deatils Saved Successfully!!!!!!!!!!!!")
                except:
                    print("not working DataBase")
            Button(top,text="Save",font=('Cambria',20),command=hero,bg="skyblue").place(x=650,y=360)
            
            
             
            top.mainloop()

        def rete():

            show=tk.Tk()
            show.geometry("890x490")
            try:

                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                query="SELECT * FROM patientd"
                cur=mycon.cursor()
                cur.execute(query)
                tdata=cur.fetchall()
                num=2
                Label(show,text="Patient Registered",font=('Arial Rounded MT Bold',20)).grid(row=0,column=2)
                Label(show,text="Name",font=('Arial',14)).grid(row=1,column=0)
                Label(show,text="Age",font=('Arial',14)).grid(row=1,column=1)
                Label(show,text="Gender",font=('Arial',14)).grid(row=1,column=2)
                Label(show,text="Mobile",font=('Arial',14)).grid(row=1,column=3)
                Label(show,text="Address",font=('Arial',14)).grid(row=1,column=4)
                for i in tdata:
                    p=Label(show,text=i[0])
                    p.grid(row=num,column=0,padx=40,pady=20)

                    v=Label(show,text=i[1])
                    v.grid(row=num,column=1,padx=40,pady=10)
                    
                    g=Label(show,text=i[2])
                    g.grid(row=num,column=2,padx=40,pady=10)

                    m=Label(show,text=i[3])
                    m.grid(row=num,column=3,padx=40,pady=10)

                    ad=Label(show,text=i[4])
                    ad.grid(row=num,column=4,padx=40,pady=10)
                    num=num+2
                    
            except:

                print("Error while fetching the Data! ")
                print("Try Again!!!!!!!")
            show.mainloop()
                   
            
        def pet():
            win=tk.Tk()  
            win.geometry("800x400")
                # register Patient
            Label(win,text="  Welcome to Nersing Home  ",font=('Arial Rounded MT Bold',20)).place(x=230,y=8)
            b2=Button(win,text="Register Patient",command=dataget,font=('Cambria',14),bg="teal").place(x=70,y=100)

            b3=Button(win,text="List of Patient",command=rete,font=('Cambria',14),bg="teal").place(x=580,y=100)
           # Label(win,text="Instructions To Follow : ",font=('Calibri',12)).place(x=70,y=150)
            # Label(win,text="क्लिनिकमध्ये सामाजिक अंतर ठेवा ",font=('Calibri',12)).place(x=130,y=190)

            b1=Button(win,text="Back",command=win.destroy,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=310,y=360)
            win.mainloop()

               
        def my():
            Gui=tk.Tk()
            Gui.geometry("840x420")
            Label(Gui,text="  Select Your Appointments   ",font=('Arial Rounded MT Bold',20)).place(x=230,y=8)
            ttk.Label(Gui, text = "Select Patient :",font = ("Times New Roman", 10)).place(x=10,y=60)
            n = tk.StringVar()
            monthchoosen = ttk.Combobox(Gui, width = 27, textvariable = n)
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
            query="SELECT * FROM patientd"
            cur=mycon.cursor()
            cur.execute(query)
            tdata=cur.fetchall()
            namelist=[]
            for a in tdata:
                data=(a[0])
                namelist.append(data)
            # Adding combobox drop down list
            monthchoosen['values']=(namelist)

            monthchoosen.place(x=100,y=60)
            def call():

                try:
                    u1=k4.get()
                    val=monthchoosen.get()
                    val1=k.get()
                    val2=k1.get() 
                
                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                   
                    query="""insert into appoin(pname,adate,session,opd) VALUES ('{}','{}','{}','{}');""".format(val,u1,val1,val2)
                    #print("ok2")
                    cur=mycon.cursor()
                   # print("ok3")
                    cur.execute(query)
                    mycon.commit()
                    cur.close()
                    messagebox.showinfo("","Deatils Saved Successfully!!!!!!!!!!!!")
                except:
                    print("not working DataBase")

            

            Label(Gui, text = "Appointment Date:",font = ("Times New Roman", 10)).place(x=500,y=60)
            n3 = tk.StringVar()
            k4 = ttk.Combobox(Gui, width = 27, textvariable = n3)

            # Adding combobox drop down list
            k4['values'] = ('10/01/2022','11/01/2022','12/01/2022','13/01/2022','14/01/2022')
            k4.place(x=610,y=60)
            

            Label(Gui, text = "Appointment Session:",font = ("Times New Roman", 10)).place(x=10,y=160)
            n1 = tk.StringVar()
            k = ttk.Combobox(Gui, width = 27, textvariable = n1)

            # Adding combobox drop down list
            k['values'] = ('Moring','Afternoon','Evening')
            k.place(x=140,y=160)


            Label(Gui, text = "Appointment For OPD:",font = ("Times New Roman", 10)).place(x=500,y=160)
            n2 = tk.StringVar()
            k1= ttk.Combobox(Gui, width = 27, textvariable = n2)

            # Adding combobox drop down list
            k1['values'] = ('Orthopedic','Gynecologist')
            k1.place(x=640,y=160)
            
            Button(Gui,text="Back",command=Gui.destroy,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=80,y=360)
            Button(Gui,text="Submit",command=call,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=310,y=360)
            def we():
                know=tk.Tk()
                know.geometry("800x400")
                try:

                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                    query="SELECT * FROM appoin"
                    cur=mycon.cursor()
                    cur.execute(query)
                    tdata=cur.fetchall()
                    num=2
                    Label(know,text="Todays Appointment",font=('Arial Rounded MT Bold',20)).grid(row=0,column=2)
                    Label(know,text="Name",font=('Arial',14)).grid(row=1,column=0)
                    Label(know,text="Date",font=('Arial',14)).grid(row=1,column=1)
                    Label(know,text="Session",font=('Arial',14)).grid(row=1,column=2)
                    Label(know,text="OPD",font=('Arial',14)).grid(row=1,column=3)
                    

                   
                    for i in tdata:
                        p=Label(know,text=i[0])
                        p.grid(row=num,column=0,padx=40,pady=20)

                        v=Label(know,text=(i[1]))
                        v.grid(row=num,column=1,padx=40,pady=10)
                    
                        g=Label(know,text=i[2])
                        g.grid(row=num,column=2,padx=40,pady=10)

                        m=Label(know,text=i[3])
                        m.grid(row=num,column=3,padx=40,pady=10)

                        num=num+2
                    
                except:

                    print("Error while fetching the Data! ")
                    print("Try Again!!!!!!!")
                Button(know,text="Back",font=('Cambria',20),command=know.destroy,bg="skyblue").place(x=350,y=360)
                know.mainloop()
            Button(Gui,text="See Appointment List",command=we,height=1,width=25,bg="skyblue",font=('Arial',14)).place(x=550,y=360)
            monthchoosen.current()
            Gui.mainloop()
        def bill():
            way=tk.Tk()
            way.geometry("800x400")
            Label(way,text=" Bill ",font=('Arial Rounded MT Bold',20)).place(x=300,y=8)
            Label(way, text = "Bill No:",font = ("Times New Roman", 10)).place(x=10,y=60)
            v1=Entry(way)
            v1.place(x=60,y=60)

            Label(way, text = "Date:",font = ("Times New Roman", 10)).place(x=500,y=60)
            n6 = tk.StringVar()
            k10 = ttk.Combobox(way, width = 27, textvariable = n6)

            # Adding combobox drop down list
            k10['values'] = ('10/01/2022','11/01/2022','12/01/2022','13/01/2022','14/01/2022')
            k10.place(x=540,y=60)
            
            ttk.Label(way, text = "Select Patient :",font = ("Times New Roman", 10)).place(x=10,y=160)
            n7 = tk.StringVar()
            monthchoosen = ttk.Combobox(way, width = 27, textvariable = n7)
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
            query="SELECT * FROM patientd"
            cur=mycon.cursor()
            cur.execute(query)
            tdata=cur.fetchall()
            namelist=[]
            for a in tdata:
                data=(a[0])
                namelist.append(data)
            # Adding combobox drop down list
            monthchoosen['values']=(namelist)

            monthchoosen.place(x=100,y=160)
        
            Label(way, text = "Select OPD:",font = ("Times New Roman", 10)).place(x=500,y=160)
            n8 = tk.StringVar()
            k11= ttk.Combobox(way, width = 27, textvariable = n8)

            # Adding combobox drop down list
            k11['values'] = ('Orthopedic','Gynecologist')
            k11.place(x=580,y=160)
            Label(way, text = "Note:",font = ("Times New Roman", 10)).place(x=10,y=250)
            Label(way, text = "Orthopedic=500 Rs:",font = ("Times New Roman", 10)).place(x=70,y=250)
            Label(way, text = "Gynecologist=600 Rs:",font = ("Times New Roman", 10)).place(x=70,y=270)
            
            def pre():
                q1=v1.get()
                q2=k10.get()
                q3=monthchoosen.get()
                q4=k11.get()


                if k11.get()=='Orthopedic':
                    value10=500
                    print(value10)
                else:
                    value10=600
                    print(value10)
                try:

                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                   
                    query="""insert into pdata(bill,adate,ptname,opd,tbill) VALUES ('{}','{}','{}','{}','{}');""".format(q1,q2,q3,q4,value10)
                    cur=mycon.cursor()

                    cur.execute(query)
                    mycon.commit()
                    cur.close()
                    messagebox.showinfo("","Deatils Saved Successfully!!!!!!!!!!!!")
                except:
                    print("not working DataBase")
                
            def Coll():
                way1=tk.Tk()
                way1.geometry("800x400")
                try:

                    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="Patient")
                    query="SELECT * FROM pdata"
                    cur=mycon.cursor()
                    cur.execute(query)
                    tdata=cur.fetchall()
                    num=2
                    Label(way1,text="Total Bill Genrated",font=('Arial Rounded MT Bold',20)).grid(row=0,column=2)
                    Label(way1,text="Bill No",font=('Arial',14)).grid(row=1,column=0)
                    Label(way1,text="Date",font=('Arial',14)).grid(row=1,column=1)
                    Label(way1,text="Patient Name",font=('Arial',14)).grid(row=1,column=2)
                    Label(way1,text="OPD",font=('Arial',14)).grid(row=1,column=3)
                    Label(way1,text="Total Bill",font=('Arial',14)).grid(row=1,column=4)
                    
                    num=2
                   
                    for i in tdata:
                        p=Label(way1,text=i[0])
                        p.grid(row=num,column=0,padx=40,pady=20)

                        v=Label(way1,text=(i[1]))
                        v.grid(row=num,column=1,padx=40,pady=10)
                    
                        g=Label(way1,text=i[2])
                        g.grid(row=num,column=2,padx=40,pady=10)

                        m=Label(way1,text=i[3])
                        m.grid(row=num,column=3,padx=40,pady=10)

                        d=Label(way1,text=(i[4]))
                        d.grid(row=num,column=4,padx=40,pady=10)

                        num=num+2
                    
                except:

                    print("Error while fetching the Data! ")
                    print("Try Again!!!!!!!")
                Button(way1,text="Back",command=way1.destroy,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=270,y=360)
                way1.mainloop()
            Button(way,text="View Total Bill Genrated",command=Coll,height=1,width=25,bg="skyblue",font=('Arial',14)).place(x=500,y=360)   
            Button(way,text="submit",command=pre,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=265,y=360)
            Button(way,text="Back",command=way.destroy,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=60,y=360)

                


    
            way.mainloop()
        menubar = Menu(root)
       # menubar.add_command(label="DashBoard     ",font=('Arial',26))

        menubar.add_command(label="Patient          ", command=pet)

        menubar.add_command(label="Appointments          ", command=my)

        menubar.add_command(label="Genrate Bill          ", command=bill)


        menubar.add_command(label="Logout->          ", command=root.quit)
        root.config(menu=menubar)

        
        root.mainloop() 
    
    else:
        messagebox.showinfo("","Incorrect Username or Password")

root=tk.Tk()
root.title("Login")
root.geometry("400x400")
#photo=PhotoImage(file="img1.png")
a=tk.Label(root)
a.pack()
global e1
global e2

Label(root,text="Username",font=('Arial',14)).place(x=30,y=100)
Label(root,text="Password",font=('Arial',14)).place(x=30,y=150)
Label(root,text="Sign in to start your session",font=('Segoe UI',14)).place(x=70,y=10)
e1=Entry(root,bg="gray")
e1.place(x=190,y=110)
e2=Entry(root,bg="gray")
e2.place(x=190,y=160)



Button(root,text="Login",command=ok,height=1,width=15,bg="skyblue",font=('Arial',14)).place(x=100,y=360)

root.mainloop()

