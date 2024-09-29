from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import csv,os,random,datetime

######################################################################
######################################################################

def About_Us_Func():
    def Home_Page_Back_Func():
        window.destroy()
        Home_Page_Func()

    window = Tk()
    window.title("ABOUT HILLTOP HEAVEN RESORTS")
    window.geometry("1000x700")

    bg = PhotoImage(file="bg image 10.png")
    label1 = Label( window, image = bg)
    label1.place(x = 0, y = 0)
    btn32 = Button(window,text="BACK",font=("Cambria",16),bg="forest green",fg="blanched almond",width=8, command=Home_Page_Back_Func)
    btn32.place(x=10, y= 10)

    lbl36=Label(window,text="HILLTOP HEAVEN RESORTS",fg="forest green",font=("Cambria",28,"bold"),width=25)
    lbl36.place(x=240,y=80)

    T = Text(window, height = 16,fg="forest green", width = 55)
    Fact = """We are a resort that is a self-contained commercial establishment and try to provide most of a vacationer's wants, such as food, drink, \nlodging, sports, entertainment, and shopping, on the premises.We \nprovide an array of amenities, typically including entertainment and \nrecreational activities. \n\nWe have:
                     o A multi-cuisine restaurant,
                     o Spa,
                     o Indoor Games,
                     o Outdoor Games,
                     o Car rentals,
                     o Rooms with heaters, air coolers
                     o Excellent laundry services and dry cleaning
                     o A large gymnasiumbackbac
                     o Postal Services
                     o Swimming pools
	  for a very comfortable and a memorable experience.
             
            """

    T.config(font =("Cambria", 18))
    T.place(x=140, y=190)
    T.insert(END, Fact)
    T.config(state="disabled")

    window.mainloop()

######################################################################
######################################################################

def Admin_Signup():
    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
    cur=mydb.cursor()
    
        
    def back_func():
        window.destroy()
        Admin_Signin_Func()

    def callback(eventObject):
        global gender
        if ("Male" ==eventObject.widget.get()): gender = 'M'
        else: gender = 'F'    
           
           
    def Ok():
        if ent31.get() and ent32.get() and ent33.get() and ent331.get() and ent41.get() and ent34.get() and ent35.get() and ent36.get() and address.get("1.0","end-1c"):
            userid=""
            username = ent31.get()
            name = ent33.get()
            passwd = ent32.get()
            idproof = ent331.get()
            phno = ent34.get()
            email=ent35.get()
            addr=address.get("1.0","end-1c")

            if len(name) > 30:
                messagebox.showinfo('error','Length of name should not exceed 30')
                return
            if not any(char.isalpha() for char in name):
                messagebox.showerror('error','Invalid Name !')
                return
                            
            SpecialSym =['$', '@', '#', '%','!']
           
            if len(username) < 4:
                messagebox.showerror('error','Username should have atleast 4 characters')
                return
            if len(username) > 15:
                messagebox.showerror('error','Length of username should not exceed 15')
                return
            if len(passwd) < 6:
                messagebox.showerror('error','Password should have atleast 6 characters')
                return             
            if len(passwd) > 20:
                messagebox.showerror('error','Length of password should not exceed 20')
                return              
            if not any(char.isdigit() for char in passwd):
                messagebox.showerror('error','Password should have atleast one numeral')
                return            
            if not any(char.isupper() for char in passwd):
                messagebox.showerror('error','Password should have atleast one uppercase letter')
                return              
            if not any(char.islower() for char in passwd):
                messagebox.showerror('error','Password should have atleast one lowercase letter')
                return
            if not any(char in SpecialSym for char in passwd):
                messagebox.showerror('error','Password should have atleast special character')
                return
            if (not str(phno).isdigit()) or len(str(phno))!=10:
                messagebox.showerror('error','Invalid Phone Number !')
                return
            if '@' not in email:
                messagebox.showerror('error','Invalid Email-Id !')
                return

                        
            while True:
                c="A"
                n1=random.randint(1000,9999)
                a=str(c)+str(n1)
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                cur=mydb.cursor()
                cur.execute("select ID from user_admin where ID='"+a+"'")
                userid = a
                if len(cur.fetchall())==0: break

            mycursor=mydb.cursor()

            if ent36.get()=='ad123':
             
                try:
                    sql = "INSERT INTO user_admin(id, name,gender,idproof,phoneno,email,address,username,pswd)\
                                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (userid, name, gender, idproof, phno, email, addr, username, passwd)
                    mycursor.execute(sql, val)
                    mydb.commit()

                except Exception as e:
                    mydb.rollback()
                    mydb.close()

                messagebox.showinfo("Admin", "ACCOUNT CREATED SUCCESSFULLY!!")
            else:
                messagebox.showerror("Admin", "Wrong Admin Password!!")

    window = Tk()
    window.title("SIGN UP")
    window.geometry("1000x700")
    bg = PhotoImage(file="bg image 3.png")
    label1 = Label( window, image = bg)
    label1.place(x=0,y=0)
    btn32 = Button(window,text="BACK",bg="forest green",fg="white",font=("Cambria",16), width=8, command=back_func)
    btn32.place(x=10, y= 10)
    lbl36=Label(window,text="CREATE ACCOUNT",font=("Cambria",36,"bold"),fg="forest green", width=17)
    lbl36.place(x=275,y=70)

    lbl37=Label(window,text="USER NAME",fg="forest green",font=("Cambria",16, "bold"))
    lbl37.place(x=180,y=160)
    ent31=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent31.place(x=370, y=160)

    lbl38=Label(window,text="PASSWORD",fg="forest green",font=("Cambria",16, "bold"))
    lbl38.place(x=180,y=210)
    ent32=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent32.place(x=370, y=210)

    lbl39=Label(window,text="NAME",fg="forest green",font=("Cambria",16, "bold"))
    lbl39.place(x=180,y=260)
    ent33=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent33.place(x=370, y=260)

    lbl391=Label(window,text="ID PROOF",fg="forest green",font=("Cambria",16, "bold"))
    lbl391.place(x=180,y=310)
    ent331=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent331.place(x=370, y=310)

    lbl41=Label(window,text="GENDER",fg="forest green",font=("Cambria",16, "bold"))
    lbl41.place(x=750,y=310)
    ent441 = StringVar()
    data=("M", "F")
    ent41=ttk.Combobox(window, textvariable=ent441,width=2,font=("Californian F8",16))
    ent41['values']=data
    ent41.place(x=840, y=310)
    ent41.bind("<<ComboboxSelected>>", callback)

    lbl40=Label(window,text="PHONE NUMBER",fg="forest green",font=("Cambria",16, "bold"))
    lbl40.place(x=180,y=360)
    ent34=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent34.place(x=370, y=360)

    lbl41=Label(window,text="EMAIL",fg="forest green", font=("Cambria",16, "bold"))
    lbl41.place(x=180,y=410)
    ent35=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent35.place(x=370, y=410)

    lbl42=Label(window,text="ADDRESS",fg="forest green", font=("Cambria",16, "bold"))
    lbl42.place(x=180,y=460)
    address = Text(window,width=37,height=8,bd=3)
    address.place(x=370,y=460)

    lbl43=Label(window,text="ADMIN PWD",fg="forest green", font=("Cambria",16, "bold"))
    lbl43.place(x=180,y=620)
    ent36=Entry(window,font=("Californian F8", 16),bd=3,width=25,show='*')
    ent36.place(x=370, y=620)

    btn34 = Button(window,text="CREATE ACCOUNT",bg="forest green",fg="white",font=("Cambria",16),    width=16, command=Ok)
    btn34.place(x=750, y= 590)
    window.mainloop()

######################################################################
######################################################################

                def Room_Type_Func():

                    def sign_out_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        Home_Page_Func()
                    
                    def admin_ui_back_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        admin_home_page_func()
                    
                    window = Tk()
                    window.title('room_type page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    columns = ('TYPE_ID','NAME','NOP','AC_NONAC','COST')
                    wth=[50,160,50,70,50]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=6)
                    for i in range(len(columns)):
                        tree.heading(columns[i],text=columns[i])
                        tree.column(columns[i],width=wth[i])
                        
                    def Show_all():
                        tree.delete(*tree.get_children())
                        cur.execute('SELECT * FROM Room_Type')
                        types=cur.fetchall()
                        for Type in types:
                            tree.insert('',END,values=Type)    
                        tree.place(x=100,y=360)

                    Show_all()

                    def Show_entry(x):
                        values=tree.item(tree.focus())['values']

                        ti_entry.config(state='normal')
                        name_entry.config(state='normal')
                        nop_spin.config(state='normal')
                        ac_combo.config(state='normal')

                        ti_entry.delete(0,END)
                        name_entry.delete(0,END)
                        nop_spin.delete(0,END)
                        ac_combo.delete(0,END)
                        cost_entry.delete(0,END)
                        
                        ti_entry.insert(0,values[0])
                        name_entry.insert(0,values[1])
                        nop_spin.insert(0,values[2])
                        ac_combo.insert(0,values[3])
                        cost_entry.insert(0,values[4])

                        ti_entry.config(state='readonly')
                        name_entry.config(state='readonly')
                        nop_spin.config(state='readonly')
                        ac_combo.config(state='readonly')
                        
                    tree.bind('<ButtonRelease>', Show_entry)

                    columns2 = ('HOTEL_ID','PLACE','ADDRESS')
                    wth2=[80,110,330]
                    tree2 = ttk.Treeview(window, columns=columns2, show='headings',height=6)
                    for i in range(len(columns2)):
                        tree2.heading(columns2[i],text=columns2[i])
                        tree2.column(columns2[i],width=wth2[i])
                    cur.execute('SELECT * FROM Branch')
                    records2=cur.fetchall()
                    for record in records2:
                        tree2.insert('',END,values=record)
                    tree2.place(x=240,y=110)

                    type_id=Label(window, text='Type Id :', font=("Cambria",14,'bold'),fg="forest green")
                    type_id.place(x=565,y=320)

                    ti_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    ti_entry.place(x=670,y=322)

                    name=Label(window, text='Name   :', font=("Cambria",14,'bold'),fg="forest green")
                    name.place(x=565,y=370)

                    name_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    name_entry.place(x=670,y=372)

                    nop=Label(window, text='NOP :', font=("Cambria",14,'bold'),fg="forest green")
                    nop.place(x=565,y=420)

                    nop_spin=Spinbox(window,from_=0, to=15,bd=3, font=("Californian FB",12),width=24,state='readonly')
                    nop_spin.place(x=670,y=422)

                    ac=Label(window, text='AC_nonAC :', font=("Cambria",14,'bold'),fg="forest green")
                    ac.place(x=565,y=470)

                    m=StringVar()
                    ac_combo=ttk.Combobox(window,width=20,textvariable=m,font=('Californian FB',12),state='readonly')
                    ac_combo['values']=('AC','nonAC')
                    ac_combo.place(x=700,y=472)

                    cost=Label(window, text='Cost     :', font=("Cambria",14,'bold'),fg="forest green")
                    cost.place(x=565,y=520)

                    cost_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    cost_entry.place(x=670,y=522)

                    def Update():
                        Values=tree.item(tree.focus())['values']
                        if len(Values)==5:
                            try :
                                float(cost_entry.get())
                                Values[2]=nop_spin.get()
                                Values[3]=ac_combo.get()
                                Values[4]=cost_entry.get()
                                tree.item(tree.selection()[0],values=Values)
                                with open('temp.csv', 'a', newline='') as f:
                                    a= csv.writer(f)
                                    a.writerow(Values)
                            except ValueError: messagebox.showerror('Error','Invalid Input')

                    def Save():
                        x=None
                        try:
                            with open('temp.csv') as f:
                                a=csv.reader(f)
                                for i in a:
                                    cur.execute('UPDATE room_type SET NOP='+i[2]+', AC_NONAC="'+i[3]+'", COST='+i[4]+' WHERE TYPE_ID="'+i[0]+'"')
                                    mydb.commit()
                                    x=True
                        except: pass
                        if x: messagebox.showinfo('info','Record(s) Updated Successfully')
                        with open('temp.csv','w') as f: pass

                    def Reset():
                        Show_all()
                            
                        with open('temp.csv','w') as f: pass

                        ti_entry.config(state='normal')
                        name_entry.config(state='normal')
                        nop_spin.config(state='normal')
                        ac_combo.config(state='normal')
                        
                        ti_entry.delete(0,END)
                        name_entry.delete(0,END)
                        nop_spin.delete(0,END)
                        ac_combo.delete(0,END)
                        cost_entry.delete(0,END)
                        
                        ti_entry.config(state='readonly')
                        name_entry.config(state='readonly')
                        nop_spin.config(state='readonly')
                        ac_combo.config(state='readonly')
                                
                    update=Button(window,text="UPDATE",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Update)
                    update.place(x=610,y=610)

                    save=Button(window,text="SAVE",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Save)
                    save.place(x=410,y=610)

                    reset=Button(window,text="RESET",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Reset)
                    reset.place(x=210,y=610)
                    
                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def Services_Func():

                    def sign_out_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        Home_Page_Func()

                    def admin_ui_back_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        admin_home_page_func()

                    def Search():
                        if sb_combo.get() and sb_entry.get():
                            tree.delete(*tree.get_children())
                            cur.execute('SELECT * FROM Services WHERE LOWER('+sb_combo.get()+') LIKE LOWER("%'+sb_entry.get()+'%")')
                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)
                        
                    def Show_all():
                        tree.delete(*tree.get_children())
                        cur.execute('SELECT * FROM Services')
                        records=cur.fetchall()
                        for record in records:
                            tree.insert('',END,values=record)    

                    window = Tk()
                    window.title('services page')
                    window.geometry('1000x700')
                    
                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    search_by=Label(window, text='SEARCH BY :', font=("Cambria",16,'bold'),fg="forest green")
                    search_by.place(x=75,y=101)

                    columns = ('SERVICE_ID','NAME','PRICE','UNITS')
                    wth=[70,160,50,113]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                    for i in range(len(columns)):
                        tree.heading(columns[i],text=columns[i])
                        tree.column(columns[i],width=wth[i])
                    tree.place(x=85,y=170)

                    Show_all()

                    def Show_entry(x):
                        values=tree.item(tree.focus())['values']

                        id_entry.config(state='normal')
                        name_entry.config(state='normal')

                        id_entry.delete(0,END)
                        name_entry.delete(0,END)
                        price_entry.delete(0,END)
                        u_entry.delete(0,END)
                        
                        id_entry.insert(0,values[0])
                        name_entry.insert(0,values[1])
                        price_entry.insert(0,values[2])
                        u_entry.insert(0,values[3])

                        id_entry.config(state='readonly')
                        name_entry.config(state='readonly')
                        
                    tree.bind('<ButtonRelease>', Show_entry)

                    n=StringVar()
                    sb_combo=ttk.Combobox(window, width=11, textvariable=n, font=(12),state='readonly')
                    sb_combo['values']=('SERVICE_ID','NAME','PRICE','UNITS')
                    sb_combo.place(x=215,y=105)

                    sb_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    sb_entry.place(x=365,y=105)

                    search=Button(window,text="SEARCH",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Search)
                    search.place(x=645,y=98)

                    show_all=Button(window,text="SHOW ALL",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Show_all)
                    show_all.place(x=805,y=98)

                    service_id=Label(window, text='Service Id :', font=("Cambria",16,'bold'),fg="forest green")
                    service_id.place(x=545,y=210)

                    id_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    id_entry.place(x=675,y=213)

                    name=Label(window, text='Name :', font=("Cambria",16,'bold'),fg="forest green")
                    name.place(x=545,y=280)

                    name_entry=Entry(window,font=("Californian FB",12),bd=3,width=29)
                    name_entry.place(x=638,y=282)

                    price=Label(window, text='Price :', font=("Cambria",16,'bold'),fg="forest green")
                    price.place(x=545,y=350)

                    price_entry=Entry(window,font=("Californian FB",12),bd=3,width=30)
                    price_entry.place(x=630,y=353)

                    units=Label(window, text='Units :', font=("Cambria",16,'bold'),fg="forest green")
                    units.place(x=545,y=420)

                    u_entry=Entry(window,font=("Californian FB",12),bd=3,width=30)
                    u_entry.place(x=630,y=422)

                    def Update():
                        Values=tree.item(tree.focus())['values']
                        if len(Values)==4:
                            try:
                                float(price_entry.get())
                                Values[2]=price_entry.get()
                                Values[3]=u_entry.get()
                                tree.item(tree.selection()[0],values=Values)
                                with open('temp.csv','a',newline='') as f:
                                    a=csv.writer(f)
                                    a.writerow(Values)
                            except ValueError: messagebox.showerror('Error','Invalid Input')

                    def Save():
                        x=None
                        with open('temp.csv') as f:
                            a=csv.reader(f)
                            for i in a:
                                cur.execute('UPDATE services SET PRICE='+i[2]+', UNITS="'+i[3]+'" WHERE SERVICE_ID="'+i[0]+'"')
                                mydb.commit()
                                x=True
                        if x: messagebox.showinfo('info','Record(s) Updated Successfully')
                        with open('temp.csv','w') as f: pass
                        
                    def Reset():
                        Show_all()
                            
                        with open('temp.csv','w') as f: pass

                        id_entry.config(state='normal')
                        name_entry.config(state='normal')
                        id_entry.delete(0,END)
                        name_entry.delete(0,END)
                        price_entry.delete(0,END)
                        u_entry.delete(0,END)
                        id_entry.config(state='readonly')
                        name_entry.config(state='readonly')
                        
                        
                    update=Button(window,text="UPDATE",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Update)
                    update.place(x=645,y=490)

                    save=Button(window,text="SAVE",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Save)
                    save.place(x=545,y=570)

                    reset=Button(window,text="RESET",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Reset)
                    reset.place(x=745,y=570)
                        
                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def Rooms_Func():

                    def sign_out_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        Home_Page_Func()

                    def admin_ui_back_func():
                        try: os.remove('temp.csv')
                        except: pass
                        window.destroy()
                        admin_home_page_func()

                    def search():
                        if sb_combo.get() and sb_entry.get():
                            tree.delete(*tree.get_children())
                            if sb_combo.get()=='TYPE_NAME': c='name'
                            elif sb_combo.get()=='PLACE': c='branch'
                            else: c=sb_combo.get()
                            cur.execute('SELECT * FROM ROOMS WHERE LOWER('+c+') LIKE LOWER("%'+sb_entry.get()+'%")')
                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)

                    def Show_all():
                        tree.delete(*tree.get_children())
                        cur.execute('SELECT * FROM ROOMS')
                        records=cur.fetchall()
                        for record in records:
                            tree.insert('',END,values=record)
                    
                    window = Tk()
                    window.title('rooms page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    search_by=Label(window, text='SEARCH BY :', font=("Cambria",16,'bold'),fg="forest green")
                    search_by.place(x=75,y=101)

                    columns = ('ROOM_NO','TYPE_ID','TYPE_NAME','HOTEL_ID','PLACE')
                    wth=[70,50,160,60,90]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                    for i in range(len(columns)):
                            tree.heading(columns[i],text=columns[i])
                            tree.column(columns[i],width=wth[i])
                    tree.place(x=75,y=170)

                    Show_all()

                    n=StringVar()
                    sb_combo=ttk.Combobox(window, width=11, textvariable=n, font=(12),state='readonly')
                    sb_combo['values']=('ROOM_NO','TYPE_ID','TYPE_NAME','HOTEL_ID','PLACE')
                    sb_combo.place(x=215,y=105)

                    sb_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    sb_entry.place(x=365,y=105)

                    search=Button(window,text="SEARCH",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=search)
                    search.place(x=645,y=98)

                    show_all=Button(window,text="SHOW ALL",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Show_all)
                    show_all.place(x=805,y=98)

                    room_no=Label(window, text='Room No. :', font=("Cambria",16,'bold'),fg="forest green")
                    room_no.place(x=545,y=180)

                    rn_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    rn_entry.place(x=675,y=183)

                    cur.execute('SELECT * FROM Room_Type')
                    records=cur.fetchall()
                    t_id,t_name=[],[]
                    for record in records:
                        t_id.append(record[0])
                        t_name.append(record[1])

                    def type_id_func(x):
                        y=int(ti_combo.get()[-1])-1
                        tn_combo.current(y)

                    def type_name_func(x):
                        z=['PRESIDENTIAL SUITE','ONE BEDROOM CHALET','INTERCONNECTING ROOMS','TWIN ROOM'].index(tn_combo.get())
                        ti_combo.current(z)

                    type_id=Label(window, text='Type Id :', font=("Cambria",16,'bold'),fg="forest green")
                    type_id.place(x=545,y=250)

                    m=StringVar()
                    ti_combo=ttk.Combobox(window, width=24, textvariable=m, font=("Californian FB",12),state='readonly')
                    ti_combo['values']=t_id
                    ti_combo.place(x=667,y=252)
                    ti_combo.bind('<<ComboboxSelected>>',type_id_func)
                   
                    tname=Label(window, text='Type Name :', font=("Cambria",16,'bold'),fg="forest green")
                    tname.place(x=545,y=320)

                    n=StringVar()
                    tn_combo=ttk.Combobox(window, width=22, textvariable=n, font=("Californian FB",12),state='readonly')
                    tn_combo['values']=t_name
                    tn_combo.place(x=688,y=323)
                    tn_combo.bind('<<ComboboxSelected>>',type_name_func)

                    cur.execute('SELECT * FROM Branch')
                    records=cur.fetchall()
                    h_id,place=[],[]
                    for record in records:
                        h_id.append(record[0])
                        place.append(record[1])

                    def hotel_id_func(x):
                        y=int(hi_combo.get()[-1])-1
                        hn_combo.current(y)

                    def hotel_name_func(x):
                        z=['COORG','KODAIKANAL','MUNNAR'].index(hn_combo.get())
                        hi_combo.current(z)

                    hotel_id=Label(window, text='Hotel Id :', font=("Cambria",16,'bold'),fg="forest green")
                    hotel_id.place(x=545,y=390)

                    o=StringVar()
                    hi_combo=ttk.Combobox(window, width=24, textvariable=o, font=("Californian FB",12),state='readonly')
                    hi_combo['values']=h_id
                    hi_combo.place(x=667,y=392)
                    hi_combo.bind('<<ComboboxSelected>>',hotel_id_func)

                    hname=Label(window, text='Place :', font=("Cambria",16,'bold'),fg="forest green")
                    hname.place(x=545,y=460)

                    p=StringVar()
                    hn_combo=ttk.Combobox(window, width=26, textvariable=p, font=("Californian FB",12),state='readonly')
                    hn_combo['values']=place
                    hn_combo.place(x=645,y=462)
                    hn_combo.bind('<<ComboboxSelected>>',hotel_name_func)

                    def Add():
                        if rn_entry.get() and ti_combo.get() and tn_combo.get() and hi_combo.get() and hn_combo.get():
                            if len(rn_entry.get())==4:
                                records=[]
                                for i in tree.get_children():
                                    Id=tree.item(i)['values']
                                    records.append(str(Id[0]))
                                
                                Values=[rn_entry.get(),ti_combo.get(),tn_combo.get(),hi_combo.get(),hn_combo.get()]
                                if Values[0] not in records:
                                    tree.insert('',END,values=Values)
                                    with open('temp.csv','a',newline='') as f:
                                        a=csv.writer(f)
                                        a.writerow(Values)
                                else: messagebox.showerror('error','Room already exists')

                            else: messagebox.showerror('error','Invalid Room_No')

                    def Save():
                        x=None
                        with open('temp.csv') as f:
                            a=csv.reader(f)
                            for i in a:
                                cur.execute('INSERT INTO rooms VALUES ( "'+i[0]+'","'+i[1]+'","'+i[2]+'","'+i[3]+'","'+i[4]+'")')
                                mydb.commit()
                                x=True
                        if x: messagebox.showinfo('info','Record(s) Added Successfully')
                        with open('temp.csv','w') as f: pass

                    def Reset():
                        Show_all()
                            
                        with open('temp.csv','w') as f: pass

                        ti_combo.config(state='normal')
                        tn_combo.config(state='normal')
                        hi_combo.config(state='normal')
                        hn_combo.config(state='normal')

                        rn_entry.delete(0,END)
                        ti_combo.delete(0,END)
                        tn_combo.delete(0,END)
                        hi_combo.delete(0,END)
                        hn_combo.delete(0,END)

                        ti_combo.config(state='readonly')
                        tn_combo.config(state='readonly')
                        hi_combo.config(state='readonly')
                        hn_combo.config(state='readonly')

                    add=Button(window,text="ADD",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Add)
                    add.place(x=645,y=520)

                    save=Button(window,text="SAVE",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Save)
                    save.place(x=545,y=600)

                    reset=Button(window,text="RESET",font=("Cambria",14),bg="forest green",width=15,fg='blanched almond',command=Reset)
                    reset.place(x=745,y=600)
                    
                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def Admin_User_Func():

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def admin_ui_back_func():
                        window.destroy()
                        admin_home_page_func()

                    def search():
                        if sb_combo.get() and sb_entry.get():
                            columns = ('ID','NAME','GENDER','IDPROOF','PHONENO','EMAIL','ADDRESS')
                            wth=[43,100,58,100,78,140,310]
                            tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                            for i in range(len(columns)):
                                tree.heading(columns[i],text=columns[i])
                                tree.column(columns[i],width=wth[i])
                            cur.execute('SELECT * FROM User_Admin WHERE LOWER('+sb_combo.get()+') LIKE LOWER("%'+sb_entry.get()+'%")')
                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)    
                            tree.place(x=85,y=170)

                    def Show_all():
                        global columns
                        columns = ('ID','NAME','GENDER','IDPROOF','PHONENO','EMAIL','ADDRESS')
                        wth=[43,100,58,100,78,140,310]
                        tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                        for i in range(len(columns)):
                            tree.heading(columns[i],text=columns[i])
                            tree.column(columns[i],width=wth[i])
                        cur.execute('SELECT * FROM User_Admin')
                        records=cur.fetchall()
                        for record in records:
                            tree.insert('',END,values=record)    
                        tree.place(x=85,y=170)
                    
                    window = Tk()
                    window.title('admin_user page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    search_by=Label(window, text='SEARCH BY :', font=("Cambria",16,'bold'),fg="forest green")
                    search_by.place(x=75,y=101)
                    
                    Show_all()

                    n=StringVar()
                    sb_combo=ttk.Combobox(window, width=11, textvariable=n, font=(12),state='readonly')
                    sb_combo['values']=columns
                    sb_combo.place(x=215,y=105)

                    sb_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    sb_entry.place(x=365,y=105)

                    search=Button(window,text="SEARCH",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=search)
                    search.place(x=645,y=98)

                    show_all=Button(window,text="SHOW ALL",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Show_all)
                    show_all.place(x=805,y=98)
                    
                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def Booking_Details_Func():

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def admin_ui_back_func():
                        window.destroy()
                        admin_home_page_func()

                    def search():
                        if sb_combo.get() and sb_entry.get():
                            columns = ('BOOKING_ID','ID','HOTEL_ID','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                            wth=[89,53,70,120,80,80,80,60,80]
                            tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                            for i in range(len(columns)):
                                tree.heading(columns[i],text=columns[i])
                                tree.column(columns[i],width=wth[i])
                            cur.execute('SELECT * FROM Booking_Details WHERE LOWER('+sb_combo.get()+') LIKE LOWER("%'+sb_entry.get()+'%")')
                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)    
                            tree.place(x=145,y=170)

                    def Show_all():
                        columns = ('BOOKING_ID','ID','HOTEL_ID','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                        wth=[89,53,70,120,80,80,80,60,80]
                        tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                        for i in range(len(columns)):
                            tree.heading(columns[i],text=columns[i])
                            tree.column(columns[i],width=wth[i])
                        cur.execute('SELECT * FROM Booking_Details')
                        records=cur.fetchall()
                        for record in records:
                            tree.insert('',END,values=record)    
                        tree.place(x=145,y=170)

                    window = Tk()
                    window.title('booking details page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    search_by=Label(window, text='SEARCH BY :', font=("Cambria",16,'bold'),fg="forest green")
                    search_by.place(x=75,y=101)

                    Show_all()

                    n=StringVar()
                    sb_combo=ttk.Combobox(window, width=11, textvariable=n, font=(12),state='readonly')
                    sb_combo['values']=('BOOKING_ID','ID','HOTEL_ID','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                    sb_combo.place(x=215,y=105)

                    sb_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    sb_entry.place(x=365,y=105)

                    search=Button(window,text="SEARCH",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=search)
                    search.place(x=645,y=98)

                    show_all=Button(window,text="SHOW ALL",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Show_all)
                    show_all.place(x=805,y=98)
                    
                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def User_Services_Func():

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def admin_ui_back_func():
                        window.destroy()
                        admin_home_page_func()

                    def search():
                        if sb_combo.get() and sb_entry.get():
                            columns = ('USERVICE_ID','BOOKING_ID','NAME','ROOM_NO','QUANTITY','COST','PAYMENT')
                            wth=[80,80,130,80,80,80,80]
                            tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                            for i in range(len(columns)):
                                tree.heading(columns[i],text=columns[i])
                                tree.column(columns[i],width=wth[i])
                            cur.execute('SELECT USERVICE_ID,BOOKING_ID,NAME,ROOM_NO,QTY,COST,PAYMENT FROM User_Services,services\
                                    WHERE User_Services.SERVICE_ID=services.SERVICE_ID AND\
                                    LOWER('+sb_combo.get()+') LIKE LOWER("%'+sb_entry.get()+'%")')

                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)    
                            tree.place(x=55,y=170)

                    def Show_all():
                        columns = ('USERVICE_ID','BOOKING_ID','NAME','ROOM_NO','QUANTITY','COST','PAYMENT')
                        wth=[80,80,130,80,80,80,80]
                        tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                        for i in range(len(columns)):
                            tree.heading(columns[i],text=columns[i])
                            tree.column(columns[i],width=wth[i])
                        cur.execute('SELECT USERVICE_ID,BOOKING_ID,NAME,ROOM_NO,QTY,COST,PAYMENT FROM User_Services,services\
                                    WHERE User_Services.SERVICE_ID=services.SERVICE_ID')
                        records=cur.fetchall()
                        for record in records:
                            tree.insert('',END,values=record)    
                        tree.place(x=55,y=170)
                    
                    window = Tk()
                    window.title('user_services page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='bg image 3.png')
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=admin_ui_back_func)
                    back.place(x=10,y=10)

                    search_by=Label(window, text='SEARCH BY :', font=("Cambria",16,'bold'),fg="forest green")
                    search_by.place(x=75,y=101)

                    Show_all()

                    n=StringVar()
                    sb_combo=ttk.Combobox(window, width=11, textvariable=n, font=(12),state='readonly')
                    sb_combo['values']=('USERVICE_ID','BOOKING_ID','SERVICE_ID','ROOM_NO','QUANTITY','COST','PAYMENT')
                    sb_combo.place(x=215,y=105)

                    sb_entry=Entry(window,font=("Californian FB",12),bd=3,width=25)
                    sb_entry.place(x=365,y=105)

                    search=Button(window,text="SEARCH",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=search)
                    search.place(x=645,y=98)

                    show_all=Button(window,text="SHOW ALL",font=("Cambria",14),bg="forest green",width=11,fg='blanched almond', command=Show_all)
                    show_all.place(x=805,y=98)
                    
                    window.mainloop()

                #####################################################################            #####################################################################
              
                def Edit_Profile_Func():
                    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                    cur=mydb.cursor()

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def back_func():
                        window.destroy()
                        admin_home_page_func()
                    
                    def GetDetails():
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM user_admin limit 0,10")
                        for user in mycursor:
                            if (userid == user[0]):
                               return user

                    def Ok():
                        if ent31.get() and ent32.get() and ent33.get() and ent41.get() and ent34.get() and ent35.get() and address.get("1.0","end-1c"):
                            username = ent31.get()
                            name = ent33.get()
                            gender = ent41.get()[0]
                            passwd = ent32.get()
                            phno = ent34.get()
                            email=ent35.get()
                            addr=address.get("1.0","end-1c")

                            if len(name) > 30:
                                messagebox.showinfo('error','Length of name should not exceed 30')
                                return
                            if not any(char.isalpha() for char in name):
                                messagebox.showerror('error','Invalid Name !')
                                return
                            
                            SpecialSym =['$', '@', '#', '%','!']
           
                            if len(username) < 4:
                                messagebox.showerror('error','Username should have atleast 4 characters')
                                return
                            if len(username) > 15:
                                messagebox.showerror('error','Length of username should not exceed 15')
                                return
                            if len(passwd) < 6:
                                messagebox.showerror('error','Password should have atleast 6 characters')
                                return             
                            if len(passwd) > 20:
                                messagebox.showerror('error','Length of password should not exceed 20')
                                return              
                            if not any(char.isdigit() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one numeral')
                                return            
                            if not any(char.isupper() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one uppercase letter')
                                return              
                            if not any(char.islower() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one lowercase letter')
                                return
                            if not any(char in SpecialSym for char in passwd):
                                messagebox.showerror('error','Password should have atleast special character')
                                return
                            if (not str(phno).isdigit()) or len(str(phno))!=10:
                                messagebox.showerror('error','Invalid Phone Number !')
                                return
                            if '@' not in email:
                                messagebox.showerror('error','Invalid Email-Id !')
                                return
                
                            mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                            mycursor=mydb.cursor()
                            mycursor.execute("SELECT * FROM user_admin limit 0,10")
                            i=0
                            found = 0
                            for user in mycursor:
                                if (userid == user[0]):
                                   idproof = user[3]
                                   data_update = (name,gender,idproof,int(phno),email,addr,username,passwd,user[0])
                                   found = 1
                                   break  
                            if (found == 1):
                                mydb1=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                                cur=mydb1.cursor()
                                sql="UPDATE user_admin set  name=%s,gender=%s,idproof=%s,phoneno=%s,email=%s,address=%s,username=%s,pswd=%s where ID=%s"
                                try:
                                   cur.execute(sql, data_update)
                                   mydb1.commit()
                                except Exception as e:
                                   mydb1.rollback()
                                   mydb1.close()
                            messagebox.showinfo("Admin", "CHANGES STORED SUCCESSFULLY!!")
               
                    window = Tk()
                    window.title("EDIT PROFILE")
                    window.geometry("1000x700")
                    window["bg"]="blanched almond"
                    bg = PhotoImage(file="bg image 3.png")
                    label1 = Label( window, image = bg)
                    label1.place(x = 0, y = 0)
                    data_display = GetDetails()

                    btn32 = Button(window,bg="forest green",fg="white",text="BACK",font=("Cambria",16),   width=8,command=back_func)
                    btn32.place(x=10, y= 10)
                    btn33 = Button(window,bg="forest green",fg="white",text="SIGNOUT",font=("Cambria",16),   width=8,command=sign_out_func)
                    btn33.place(x=870, y= 10)
                    lbl36=Label(window,text="EDIT PROFILE DETAILS",fg="forest green", font=("Cambria",36),   width=20)
                    lbl36.place(x=280,y=70)

                    lbl37=Label(window,text="USER NAME",fg="forest green", font=("Cambria",16, "bold"))
                    lbl37.place(x=180,y=180)
                    ent31=Entry(window)
                    ent31.config(font=("Californian F8", 16),bd=3,width=25)
                    ent31.delete(0, END)
                    ent31.insert(0, data_display[7])
                    ent31.place(x=370, y=180)

                    lbl38=Label(window,text="PASSWORD",fg="forest green",font=("Cambria",16, "bold"))
                    lbl38.place(x=180,y=230)
                    ent32=Entry(window)
                    ent32.config(font=("Californian F8", 16),bd=3,width=25)
                    ent32.delete(0, END)
                    ent32.insert(0, data_display[8])
                    ent32.place(x=370, y=230)

                    lbl39=Label(window,text="NAME",fg="forest green",font=("Cambria",16, "bold"))
                    lbl39.place(x=180,y=280)
                    ent33=Entry(window)
                    ent33.config(font=("Californian F8", 16),bd=3,width=25)
                    ent33.delete(0, END)
                    ent33.insert(0, data_display[1])
                    ent33.place(x=370, y=280)

                    lbl41=Label(window,text="GENDER",fg="forest green",font=("Cambria",16, "bold"))
                    lbl41.place(x=180,y=330)
                    ent441 = StringVar()
                    data=("Male", "Female")
                    ent41=ttk.Combobox(window, textvariable=ent441,font=("Californian F8",16),state="readonly")
                    ent41['values']=data
                    if (data_display == "M"):
                        ent41.current(0)
                    else:
                        ent41.current(1)
                    ent41.place(x=370, y=330)

                    lbl40=Label(window,text="PHONE NUMBER",fg="forest green",font=("Cambria",16, "bold"))
                    lbl40.place(x=180,y=380)
                    ent34=Entry(window)
                    ent34.config(font=("Californian F8", 16),bd=3,width=25)
                    ent34.delete(0, END)
                    ent34.insert(0, data_display[4])
                    ent34.place(x=370, y=380)

                    lbl41=Label(window,text="EMAIL",fg="forest green",font=("Cambria",16, "bold"))
                    lbl41.place(x=180,y=430)
                    ent35=Entry(window)
                    ent35.config(font=("Californian F8", 16),bd=3,width=25)
                    ent35.delete(0, END)
                    ent35.insert(0, data_display[5])
                    ent35.place(x=370, y=430)

                    lbl42=Label(window,text="ADDRESS",fg="forest green",font=("Cambria",16, "bold"))
                    lbl42.place(x=180,y=490)
                    address=Text(window)
                    address.config(font=("Californian F8", 16),bd=3,width=25,height=6)
                    Fact=data_display[6]
                    address.insert(END, Fact)
                    address.place(x=370,y=490)

                    btn34 = Button(window,bg="forest green",fg="white",text="SAVE",font=("Cambria",16),   width=8, command=Ok)
                    btn34.place(x=750, y= 590)

                    window.mainloop()

                #####################################################################                #####################################################################

                window=Tk()
                window.title("ADMIN HOME PAGE")
                window.geometry("1000x700")

                bgimage=PhotoImage(file='bg image 3.png')
                bg=Label(window,image=bgimage)
                bg.place(x=0,y=0)

                signout=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                signout.place(x=870,y=10)

                editprofile=Button(window,text='EDIT PROFILE',font=('Cambria',16),fg='blanched almond',bg='forest green',width=12,command=edit_profile_func)
                editprofile.place(x=700,y=10)

                room_type=Button(window,text='BRANCHES & ROOM TYPES',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=room_type_func)
                room_type.place(x=125,y=150)

                rooms=Button(window,text='ROOM DETAILS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=rooms_func)
                rooms.place(x=125,y=340)

                services=Button(window,text='RESTAURANT & OTHER SERVICES',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=services_func)
                services.place(x=125,y=530)

                user_admin=Button(window,text='USER / ADMIN DETAILS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=admin_user_func)
                user_admin.place(x=540,y=150)

                booking_details=Button(window,text='BOOKING DETAILS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=booking_details_func)
                booking_details.place(x=540,y=340)

                user_services=Button(window,text='ROOM SERVICE DETAILS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=user_services_func)
                user_services.place(x=540,y=530)

                window.mainloop()

                #####################################################################                #####################################################################
            
            db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
            cursor = db.cursor()
            query = "SELECT USERNAME,PSWD,ID FROM user_admin "
            cursor.execute(query)
            names = cursor.fetchall()
            a1=ent1.get()
            a2=ent2.get()               
                

            lst1=[]
            lst2=[]
            for name in names:
                lst1.append(name[0])
                lst2.append(name[1])
                

            for b in range (0,len(lst1)):
                if a1==lst1[b]:
                    c=b
                    break
                else: c=0
                    
            if (a2)==lst2[c] and names[c][2][0]=="A":
                userid=names[c][2]
                window.destroy()
                admin_home_page_func()
            elif a2!=lst2[c]:
                lbl3=Label(window,text="INCORRECT PASSWORD/USERNAME",fg="red",font=("Cambria",13))
                lbl3.place(x=355,y=480)

    def admin_signup():
        window.destroy()
        Admin_Signup()

    btn1=Button(window,text="SIGN IN",font=("Cambria",16),fg="blanched almond",bg="forest green",width=10,command=sql)
    btn1.place(x=450,y=410)

    lbl5=Label(window,text="New here??",fg="forest green",font=("Cambria",13))
    lbl5.place(x=355,y=550)
    btn3=Button(window,text="Create an account",font=("Cambria",13),fg="blanched almond",bg="forest green",width=22,command=admin_signup)
    btn3.place(x=455,y=550)

    window.mainloop()

######################################################################
######################################################################

def User_Signup():
    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
    cur=mydb.cursor()     

    def back_func():
        window.destroy()
        User_Signin_Func()

    def callback(eventObject):
        global gender
        if ("Male" ==eventObject.widget.get()): gender = 'M'
        else: gender = 'F'    
            
            
    def Ok():
        if ent31.get() and ent32.get() and ent33.get() and ent331.get() and ent41.get() and ent34.get() and ent35.get() and address.get("1.0","end-1c"):
            userid=""
            username = ent31.get()
            name = ent33.get()
            passwd = ent32.get()
            idproof = ent331.get()
            phno = ent34.get()
            email=ent35.get()
            addr=address.get("1.0","end-1c")

            if len(name) > 30:
                messagebox.showinfo('error','Length of name should not exceed 30')
                return
            if not any(char.isalpha() for char in name):
                messagebox.showerror('error','Invalid Name !')
                return
                            
            SpecialSym =['$', '@', '#', '%','!']
           
            if len(username) < 4:
                messagebox.showerror('error','Username should have atleast 4 characters')
                return
            if len(username) > 15:
                messagebox.showerror('error','Length of username should not exceed 15')
                return
            if len(passwd) < 6:
                messagebox.showerror('error','Password should have atleast 6 characters')
                return             
            if len(passwd) > 20:
                messagebox.showerror('error','Length of password should not exceed 20')
                return              
            if not any(char.isdigit() for char in passwd):
                messagebox.showerror('error','Password should have atleast one numeral')
                return            
            if not any(char.isupper() for char in passwd):
                messagebox.showerror('error','Password should have atleast one uppercase letter')
                return              
            if not any(char.islower() for char in passwd):
                messagebox.showerror('error','Password should have atleast one lowercase letter')
                return
            if not any(char in SpecialSym for char in passwd):
                messagebox.showerror('error','Password should have atleast special character')
                return
            if (not str(phno).isdigit()) or len(str(phno))!=10:
                messagebox.showerror('error','Invalid Phone Number !')
                return
            if '@' not in email:
                messagebox.showerror('error','Invalid Email-Id !')
                return

            while True:
                c="U"
                n1=random.randint(1000,9999)
                a=str(c)+str(n1)
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                cur=mydb.cursor()
                cur.execute("select ID from user_admin where ID='"+a+"'")
                userid = a
                if len(cur.fetchall())==0: break
    
            mycursor=mydb.cursor()
             
            try:
                sql = "INSERT INTO user_admin(id, name,gender,idproof,phoneno,email,address,username,pswd)\
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (userid, name, gender, idproof, phno, email, addr, username, passwd)
                mycursor.execute(sql, val)
                mydb.commit()

            except Exception as e:
                mydb.rollback()
                mydb.close()
            messagebox.showinfo("User", "ACCOUNT CREATED SUCCESSFULLY!!")
        
    window = Tk()
    window.title("SIGNUP")
    window.geometry("1000x700")
    window["bg"]="blanched almond"
    bg = PhotoImage(file="user images.png")
    label1 = Label( window, image = bg)
    label1.place(x=0,y=0)
    btn32 = Button(window,text="BACK",bg="forest green",fg="white",font=("Cambria",16), width=8, command=back_func)
    btn32.place(x=10, y= 10)
    lbl36=Label(window,text="CREATE ACCOUNT",font=("Cambria",36,"bold"),fg="forest green", width=17)
    lbl36.place(x=275,y=70)

    lbl37=Label(window,text="USER NAME",fg="forest green",font=("Cambria",16, "bold"))
    lbl37.place(x=180,y=180)
    ent31=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent31.place(x=370, y=180)

    lbl38=Label(window,text="PASSWORD",fg="forest green",font=("Cambria",16, "bold"))
    lbl38.place(x=180,y=230)
    ent32=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent32.place(x=370, y=230)

    lbl39=Label(window,text="NAME",fg="forest green",font=("Cambria",16, "bold"))
    lbl39.place(x=180,y=280)
    ent33=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent33.place(x=370, y=280)

    lbl391=Label(window,text="ID PROOF",fg="forest green",font=("Cambria",16, "bold"))
    lbl391.place(x=180,y=330)
    ent331=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent331.place(x=370, y=330)

    lbl41=Label(window,text="GENDER",fg="forest green",font=("Cambria",16, "bold"))
    lbl41.place(x=750,y=330)
    ent441 = StringVar()
    data=("M", "F")
    ent41=ttk.Combobox(window, textvariable=ent441,width=2,font=("Californian F8",16))
    ent41['values']=data
    ent41.place(x=840, y=330)
    ent41.bind("<<ComboboxSelected>>", callback)

    lbl40=Label(window,text="PHONE NUMBER",fg="forest green",font=("Cambria",16, "bold"))
    lbl40.place(x=180,y=380)
    ent34=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent34.place(x=370, y=380)

    lbl41=Label(window,text="EMAIL",fg="forest green", font=("Cambria",16, "bold"))
    lbl41.place(x=180,y=430)
    ent35=Entry(window,font=("Californian F8", 16),bd=3,width=25)
    ent35.place(x=370, y=430)

    lbl42=Label(window,text="ADDRESS",fg="forest green", font=("Cambria",16, "bold"))
    lbl42.place(x=180,y=480)
    address = Text(window,width=37,height=8,bd=3)
    address.place(x=370,y=480)

    btn34 = Button(window,text="CREATE ACCOUNT",bg="forest green",fg="white",font=("Cambria",16),    width=16, command=Ok)
    btn34.place(x=750, y= 590)
    window.mainloop()

######################################################################
######################################################################

def User_Signin_Func():
    def Home_Page_Back_Func():
        window.destroy()
        Home_Page_Func()

    def user_signup():
        window.destroy()
        User_Signup()

    window=Tk()
    window.title("USER LOGIN PAGE")
    window.geometry("1000x700")
    bg = PhotoImage(file = "user images.png")
    lbl8=Label(window,image=bg)
    lbl8.place(x=0,y=0)

    btn5=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=Home_Page_Back_Func)
    btn5.place(x=10,y=10)

    lbl6=Label(window,text="USER SIGN IN",fg="forest green",font=("Cambria",28,"bold"))
    lbl6.place(x=400,y=150)

    lbl1=Label(window,text="USERNAME",fg="forest green",font=("Cambria",16,"bold"))
    lbl1.place(x=280,y=250)
    ent1=Entry(window,font=("Californian FB",16),bd=3,width=25,textvariable=StringVar())
    ent1.place(x=430,y=250)

    lbl2=Label(window,text="PASSWORD",fg="forest green",font=("Cambria",16,"bold"))
    lbl2.place(x=280,y=330)
    ent2=Entry(window,font=("Californian FB",16),show="*",bd=3,width=25,textvariable=StringVar())
    ent2.place(x=430,y=330)

    def sql():
        if ent1.get() and ent2.get():
            def User_Home_Page_Func():

                def sign_out_func():
                    window.destroy()
                    Home_Page_Func()

                def edit_profile_func():
                    window.destroy()
                    Edit_Profile_Func()

                def booking_history_func():
                    window.destroy()
                    Booking_History_Func()

                def current_stay_func():
                    window.destroy()
                    open_bookings()

                def book_rooms_func():
                    window.destroy()
                    Book_Rooms_Func()

                def room_service_func():
                    window.destroy()
                    Room_Service_Func()

                def resort_amenities_func():
                    window.destroy()
                    Resort_Amenities_Func()

                #####################################################################               #####################################################################

                def Booking_History_Func():
                    
                    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hotel')
                    cur=mydb.cursor()
                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()
                    def user_home_page_back_func():
                        window.destroy()
                        User_Home_Page_Func()

                    window = Tk()
                    window.title('booking history page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='user images.png')   
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=user_home_page_back_func)
                    back.place(x=10,y=10)

                    label3=Label(window,text="PREVIOUS BOOKINGS",font=('Cambria',30,'bold'),fg='forest green',width=20)
                    label3.place(x=270,y=30)

                    columns = ('BOOKING_ID','ID','HOTEL_ID','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                    wth=[89,53,70,120,80,80,80,60,80]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=23)
                    for i in range(len(columns)):
                        tree.heading(columns[i],text=columns[i])
                        tree.column(columns[i],width=wth[i])
                    cur.execute('SELECT * FROM Booking_Details WHERE ID="'+userid+'" ')
                    records=cur.fetchall()
                    for record in records:
                        tree.insert('',END,values=record)    
                    tree.place(x=145,y=125)
                    
                    window.mainloop()

                #####################################################################                #####################################################################

                def Room_Service_Func():
                    

                        def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                        def user_home_page_back_func():
                                    window.destroy()
                                    User_Home_Page_Func()

                        def restaurant_func():
                                    window.destroy()
                                    Restaurant_Func()

                        def other_services_func():
                                    window.destroy()
                                    Other_Services_Func()

                        #################################################################                        #################################################################

                        def Restaurant_Func():
                            window=Tk()
                            window.title("FOOD COURT")
                            window.geometry("1000x700")
                            bg = PhotoImage(file = "restaurant bg.png")
                            lbl8=Label(window,image=bg)
                            lbl8.place(x=0,y=0)

                            def back():
                                window.destroy()
                                Room_Service_Func()

                            def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                            btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                            btn2.place(x=10,y=10)
                            btn7=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                            btn7.place(x=870,y=10)

                            lbl=Label(window,text="RESTAURANT",fg="forest green",font=("Cambria",36,"bold"),width=15)
                            lbl.place(x=290,y=30)

                            ################################################################                            ################################################################

                            def Lunch():
                                window.destroy()
                                lunch()
                            def lunch():
                                def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                                def back():
                                    window.destroy()
                                    Restaurant_Func()

                                window=Tk()
                                window.title("LUNCH")
                                window.geometry("1000x700")
                                bg = PhotoImage(file = "lunch bg.png")
                                lbl8=Label(window,image=bg)
                                lbl8.place(x=0,y=0)

                                lbl=Label(window,text="LUNCH",fg="forest green",font=("Cambria",36,"bold"),width=15)
                                lbl.place(x=290,y=30)
                                btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn4=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn4.place(x=870,y=10)

                                var1=IntVar()
                                var2=IntVar()
                                var3=IntVar()
                                var4=IntVar()
                                var5=IntVar()
                                var6=IntVar()
                                var7=IntVar()
                                var8=IntVar()
                                var9=IntVar()
                                var10=IntVar()
                                var11=IntVar()

                                specialmeals=Checkbutton(window,text='Special meals',variable=var1,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                specialmeals.place(x=130,y=130)
                                spin1=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin1.place(x=350,y=130)

                                limitedmeals=Checkbutton(window,text='Limited meals',variable=var2,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                limitedmeals.place(x=130,y=180)
                                spin2=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin2.place(x=350,y=180)

                                lemonrice=Checkbutton(window,text='Lemon rice',variable=var3,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                lemonrice.place(x=130,y=230)
                                spin3=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin3.place(x=350,y=230)

                                sambharrice=Checkbutton(window,text='Sambhar rice',variable=var4,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                sambharrice.place(x=130,y=280)
                                spin4=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin4.place(x=350,y=280)

                                curdrice=Checkbutton(window,text='Curd rice',variable=var5,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                curdrice.place(x=130,y=330)
                                spin5=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin5.place(x=350,y=330)

                                tomatorice=Checkbutton(window,text='Tomato rice',variable=var6,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                tomatorice.place(x=130,y=380)
                                spin6=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin6.place(x=350,y=380)

                                coconutrice=Checkbutton(window,text='Coconut rice',variable=var7,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                coconutrice.place(x=130,y=430)
                                spin7=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin7.place(x=350,y=430)

                                mintrice=Checkbutton(window,text='Mint rice',variable=var8,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                mintrice.place(x=130,y=480)
                                spin8=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin8.place(x=350,y=480)

                                vegfriedrice=Checkbutton(window,text='Veg fried rice',variable=var9,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                vegfriedrice.place(x=130,y=530)
                                spin9=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin9.place(x=350,y=530)

                                mushroombriyani=Checkbutton(window,text='Mushroom briyani',variable=var10,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                mushroombriyani.place(x=130,y=580)
                                spin10=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin10.place(x=350,y=580)

                                paneerfriedrice=Checkbutton(window,text='Paneer fried rice',variable=var11,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                paneerfriedrice.place(x=130,y=630)
                                spin11=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin11.place(x=350,y=630)


                                columns = ('NAME','PRICE')
                                wth=[160,50]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window, columns=columns, show='headings',height=13)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=585,y=160)
                                cur.execute('SELECT NAME,PRICE FROM Services WHERE service_id LIKE "RL%"')
                                records=cur.fetchall()
                                for record in records:
                                    tree.insert('',END,values=record)

                                lbl1=Label(window,text="FOOD'S COST",fg="forest green",font=("Cambria",16,"bold"),width=12)
                                lbl1.place(x=580,y=470)
                                
                                def get_price_of_service(service_id):
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                    t=cur.fetchall()
                                    lprice = int(t[0][1])
                                    return(lprice)

                                def insert_to_services_db(booking_id, service_id, room_no, qty):
                                    if (qty == 0):
                                        return
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select uservice_id from user_services")
                                    t=len(cur.fetchall())
                                    uservice_id = "U" + str(t+1)
                                    price = get_price_of_service(service_id)
                                    cost = qty * price
                                    try:
                                       sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                                  VALUES (%s, %s, %s, %s, %s, %s)"
                                       val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                       mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                       cur=mydb.cursor()
                                       cur.execute(sql, val)
                                       mydb.commit()

                                    except Exception as e:
                                       print(e)
                                       mydb.rollback()
                                       mydb.close()

                                def okbutton():
                                    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get() or var10.get() or var11.get()) and ent1.get():
                                        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                        cursor = db.cursor()
                                        query = "SELECT name,price FROM services"
                                        cursor.execute(query)
                                        names = cursor.fetchall()
                                        lst=[]
                                        lst1=[]
                                        lst2=[]
                                        for name in names:
                                            lst+=[name][0]
                                        for i in range(len(lst)):
                                            if i%2==0:
                                                lst1+=[lst[i]]
                                            else:
                                                lst2+=[lst[i]]
                                        
                                        totlunch=0
                                            
                                        if var1.get()==1:
                                            m1=lst1.index('SPECIAL MEALS')
                                            a1=lst2[m1]
                                            n1=spin1.get()
                                            cost1=a1*(float(n1))
                                            totlunch+=cost1
                                                
                                                    
                                        if var2.get()==1:
                                            m2=lst1.index('LIMITED MEALS')
                                            a2=lst2[m2]
                                            n2=spin2.get()
                                            cost2=a2*(float(n2))
                                            totlunch+=cost2
                                            
                                        if var3.get()==1:
                                            m3=lst1.index('LEMON RICE')
                                            a3=lst2[m3]
                                            n3=spin3.get()
                                            cost3=a3*(float(n3))
                                            totlunch+=cost3
                                            
                                        if var4.get()==1:
                                            m4=lst1.index('SAMBHAR RICE')
                                            a4=lst2[m4]
                                            n4=spin4.get()
                                            cost4=a4*(float(n4))
                                            totlunch+=cost4

                                        if var5.get()==1:
                                            m5=lst1.index('CURD RICE')
                                            a5=lst2[m5]
                                            n5=spin5.get()
                                            cost5=a5*(float(n5))
                                            totlunch+=cost5

                                            
                                        if var6.get()==1:
                                            m6=lst1.index('TOMATO RICE')
                                            a6=lst2[m6]
                                            n6=spin6.get()
                                            cost6=a6*(float(n6))
                                            totlunch+=cost6

                                        if var7.get()==1:
                                            m7=lst1.index('COCONUT RICE')
                                            a7=lst2[m7]
                                            n7=spin7.get()
                                            cost7=a7*(float(n7))
                                            totlunch+=cost7
                                            
                                        if var8.get()==1:
                                            m8=lst1.index('MINT RICE')
                                            a8=lst2[m8]
                                            n8=spin8.get()
                                            cost8=a8*(float(n8))
                                            totlunch+=cost8

                                        if var9.get()==1:
                                            m9=lst1.index('VEG FRIED RICE')
                                            a9=lst2[m9]
                                            n9=spin9.get()
                                            cost9=a9*(float(n9))
                                            totlunch+=cost9

                                        if var10.get()==1:
                                            m10=lst1.index('MUSHROOM BRIYANI')
                                            a10=lst2[m10]
                                            n10=spin10.get()
                                            cost10=a10*(float(n10))
                                            totlunch+=cost10
                                            
                                        if var11.get()==1:
                                            m11=lst1.index('PANEER FRIED RICE')
                                            a11=lst2[m11]
                                            n11=spin11.get()
                                            cost11=a11*(float(n11))
                                            totlunch+=cost11

                                        totcost=totlunch
                                        

                                        room_no = ent1.get()
                                        booking_id = value[lst0.index(room_no)][0]

                                        g1 = spin1.get()
                                        service_id="RL01"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g1))
                                
                                        g2 = spin2.get()
                                        service_id="RL02"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g2))

                                        g3 = spin3.get()
                                        service_id="RL03"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g3))
                                
                                        g4 = spin4.get()
                                        service_id="RL04"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g4))

                                        g5 = spin5.get()
                                        service_id="RL05"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g5))

                                        g6 = spin6.get()
                                        service_id="RL06"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g6))

                                        g7 = spin7.get()
                                        service_id="RL07"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g7))

                                        g8 = spin8.get()
                                        service_id="RL08"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g8))

                                        g9 = spin9.get()
                                        service_id="RL09"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g9))

                                        g10 = spin10.get()
                                        service_id="RL10"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g10))

                                        g11 = spin11.get()
                                        service_id="RL11"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g11))

                                        lbl2=Label(window,fg="forest green",text="Rs "+str(totlunch),font=("Cambria",16,"bold"),width=12)
                                        lbl2.place(x=750,y=470)

                                        messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                                     
                                btn6=Button(window,text="OK",font=("Cambria",14),fg="blanched almond",bg="forest green",width=6,command=okbutton)
                                btn6.place(x=500,y=620)

                                lbl20=Label(window,fg="forest green",text="ROOM NO.",font=("Cambria",16,"bold"),width=12)
                                lbl20.place(x=580,y=510)
                                s=StringVar()
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                                value=cur.fetchall()
                                lst0=[]
                                for i in value:
                                     lst0.append(i[1])
                                m=StringVar()
                                ent1=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                                ent1['values']=lst0
                                ent1.place(x=750,y=510)

                                window.mainloop()

                            ################################################################                          ################################################################

                            def Breakfast():
                                window.destroy()
                                breakfast()
                            def breakfast():
                                def sign_out_func():
                                    window1.destroy()
                                    Home_Page_Func()

                                def back():
                                    window1.destroy()
                                    Restaurant_Func()

                                window1=Tk()

                                window1.title("BREAKFAST")
                                window1.geometry("1000x700")
                                bg = PhotoImage(file = "breakfast1.png")
                                lbl8=Label(window1,image=bg)
                                lbl8.place(x=0,y=0)

                                lbl=Label(window1,text="BREAKFAST",fg="forest green",font=("Cambria",36,"bold"),width=15)
                                lbl.place(x=290,y=30)
                                btn2=Button(window1,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn4=Button(window1,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn4.place(x=870,y=10)

                                var1=IntVar()
                                var2=IntVar()
                                var3=IntVar()
                                var4=IntVar()
                                var5=IntVar()
                                var6=IntVar()
                                var7=IntVar()
                                var8=IntVar()
                                var9=IntVar()
                                var10=IntVar()
                                var11=IntVar()

                                idli=Checkbutton(window1,text='Idli',variable=var1,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                idli.place(x=130,y=130)
                                spin1=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin1.place(x=300,y=130)

                                gheeroast=Checkbutton(window1,text='Ghee roast',variable=var2,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                gheeroast.place(x=130,y=180)
                                spin2=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin2.place(x=300,y=180)

                                masaladosa=Checkbutton(window1,text='Masaladosa',variable=var3,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                masaladosa.place(x=130,y=230)
                                spin3=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin3.place(x=300,y=230)

                                goliidli=Checkbutton(window1,text='Goli idli',variable=var4,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                goliidli.place(x=130,y=280)
                                spin4=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin4.place(x=300,y=280)

                                appam=Checkbutton(window1,text='Appam',variable=var5,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                appam.place(x=130,y=330)
                                spin5=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin5.place(x=300,y=330)

                                uttappam=Checkbutton(window1,text='Uttappam',variable=var6,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                uttappam.place(x=130,y=380)
                                spin6=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin6.place(x=300,y=380)

                                pongal=Checkbutton(window1,text='Pongal',variable=var7,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                pongal.place(x=130,y=430)
                                spin7=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin7.place(x=300,y=430)

                                cholebatura=Checkbutton(window1,text='Chole batura',variable=var8,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                cholebatura.place(x=130,y=480)
                                spin8=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin8.place(x=300,y=480)

                                akkiroti=Checkbutton(window1,text='Akki roti',variable=var9,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                akkiroti.place(x=130,y=530)
                                spin9=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin9.place(x=300,y=530)

                                minitiffin=Checkbutton(window1,text='Mini tiffin',variable=var10,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                minitiffin.place(x=130,y=580)
                                spin10=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin10.place(x=300,y=580)

                                meduvada=Checkbutton(window1,text='Medu vada',variable=var11,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                meduvada.place(x=130,y=630)
                                spin11=Spinbox(window1,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin11.place(x=300,y=630)


                               

                                columns = ('NAME','PRICE')
                                wth=[160,50]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window1, columns=columns, show='headings',height=13)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=585,y=160)
                                cur.execute('SELECT NAME,PRICE FROM Services WHERE service_id LIKE "RB__"')
                                records=cur.fetchall()
                                for record in records:
                                    tree.insert('',END,values=record)

                                def get_price_of_service(service_id):
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                    t=cur.fetchall()
                                    lprice = int(t[0][1])
                                    return(lprice)

                                def insert_to_services_db(booking_id, service_id, room_no, qty):
                                    if (qty == 0):
                                        return
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select uservice_id from user_services")
                                    t=len(cur.fetchall())
                                    uservice_id = "U" + str(t+1)
                                    price = get_price_of_service(service_id)
                                    cost = qty * price
                                    try:
                                       sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                                  VALUES (%s, %s, %s, %s, %s, %s)"
                                       val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                       mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                       cur=mydb.cursor()
                                       cur.execute(sql, val)
                                       mydb.commit()

                                    except Exception as e:
                                       print(e)
                                       mydb.rollback()
                                       mydb.close()

                                def okbutton():
                                    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get() or var10.get() or var11.get())  and ent1.get():
                                        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                        cursor = db.cursor()
                                        query = "SELECT name,price FROM services"
                                        cursor.execute(query)
                                        names = cursor.fetchall()
                                        lst=[]
                                        lst1=[]
                                        lst2=[]
                                        for name in names:
                                            lst+=[name][0]
                                        for i in range(len(lst)):
                                            if i%2==0:
                                                lst1+=[lst[i]]
                                            else:
                                                lst2+=[lst[i]]
                                        
                                        totlunch=0
                                            
                                        if var1.get()==1:
                                            m1=lst1.index('IDLI')
                                            a1=lst2[m1]
                                            n1=spin1.get()
                                            cost1=a1*(float(n1))
                                            totlunch+=cost1
                                                
                                                    
                                        if var2.get()==1:
                                            m2=lst1.index('GHEE ROAST')
                                            a2=lst2[m2]
                                            n2=spin2.get()
                                            cost2=a2*(float(n2))
                                            totlunch+=cost2
                                            
                                        if var3.get()==1:
                                            m3=lst1.index('MASALA DOSA')
                                            a3=lst2[m3]
                                            n3=spin3.get()
                                            cost3=a3*(float(n3))
                                            totlunch+=cost3
                                            
                                        if var4.get()==1:
                                            m4=lst1.index('GOLI IDLI')
                                            a4=lst2[m4]
                                            n4=spin4.get()
                                            cost4=a4*(float(n4))
                                            totlunch+=cost4

                                        if var5.get()==1:
                                            m5=lst1.index('APPAM')
                                            a5=lst2[m5]
                                            n5=spin5.get()
                                            cost5=a5*(float(n5))
                                            totlunch+=cost5

                                            
                                        if var6.get()==1:
                                            m6=lst1.index('UTTAPPAM')
                                            a6=lst2[m6]
                                            n6=spin6.get()
                                            cost6=a6*(float(n6))
                                            totlunch+=cost6

                                        if var7.get()==1:
                                            m7=lst1.index('PONGAL')
                                            a7=lst2[m7]
                                            n7=spin7.get()
                                            cost7=a7*(float(n7))
                                            totlunch+=cost7
                                            
                                        if var8.get()==1:
                                            m8=lst1.index('CHOLE BATURA')
                                            a8=lst2[m8]
                                            n8=spin8.get()
                                            cost8=a8*(float(n8))
                                            totlunch+=cost8

                                        if var9.get()==1:
                                            m9=lst1.index('AKKI ROTI')
                                            a9=lst2[m9]
                                            n9=spin9.get()
                                            cost9=a9*(float(n9))
                                            totlunch+=cost9

                                        if var10.get()==1:
                                            m10=lst1.index('MINI TIFFIN')
                                            a10=lst2[m10]
                                            n10=spin10.get()
                                            cost10=a10*(float(n10))
                                            totlunch+=cost10
                                            
                                        if var11.get()==1:
                                            m11=lst1.index('MEDU VADA')
                                            a11=lst2[m11]
                                            n11=spin11.get()
                                            cost11=a11*(float(n11))
                                            totlunch+=cost11
                                        totcost=totlunch
                                        

                                        room_no = ent1.get()
                                        booking_id = value[lst0.index(room_no)][0]

                                        g1 = spin1.get()
                                        service_id="RB01"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g1))
                                
                                        g2 = spin2.get()
                                        service_id="RB02"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g2))

                                        g3 = spin3.get()
                                        service_id="RB03"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g3))
                                
                                        g4 = spin4.get()
                                        service_id="RB04"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g4))

                                        g5 = spin5.get()
                                        service_id="RB05"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g5))

                                        g6 = spin6.get()
                                        service_id="RB06"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g6))

                                        g7 = spin7.get()
                                        service_id="RB07"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g7))

                                        g8 = spin8.get()
                                        service_id="RB08"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g8))

                                        g9 = spin9.get()
                                        service_id="RB09"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g9))

                                        g10 = spin10.get()
                                        service_id="RB10"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g10))

                                        g11 = spin11.get()
                                        service_id="RB11"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g11))

                                        lbl2=Label(window1,fg="forest green",text="Rs "+str(totlunch),font=("Cambria",16,"bold"),width=12)
                                        lbl2.place(x=750,y=470)

                                        messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                                lbl1=Label(window1,text="FOOD'S COST",fg="forest green",font=("Cambria",16,"bold"),width=12)
                                lbl1.place(x=580,y=470)
                                btn6=Button(window1,text="OK",font=("Cambria",14),fg="blanched almond",bg="forest green",width=6,command= okbutton)
                                btn6.place(x=500,y=620)

                                lbl20=Label(window1,fg="forest green",text="ROOM NO.",font=("Cambria",16,"bold"),width=12)
                                lbl20.place(x=580,y=510)
                                s=StringVar()
                                
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                                value=cur.fetchall()
                                lst0=[]
                                for i in value:
                                     lst0.append(i[1])
                                m=StringVar()
                                ent1=ttk.Combobox(window1,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                                ent1['values']=lst0
                                ent1.place(x=750,y=510)

                                window1.mainloop()

                            ################################################################                        ################################################################

                            def Dinner():
                                window.destroy()
                                dinner()
                            def dinner():
                                window=Tk()
                                def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                                def back():
                                    window.destroy()
                                    Restaurant_Func()

                                window.title("DINNER")
                                window.geometry("1000x700")
                                bg = PhotoImage(file = "dinner bg.png")
                                lbl8=Label(window,image=bg)
                                lbl8.place(x=0,y=0)

                                lbl=Label(window,text="DINNER",fg="forest green",font=("Cambria",36,"bold"),width=15)
                                lbl.place(x=290,y=30)
                                btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn4=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn4.place(x=870,y=10)

                                var1=IntVar()
                                var2=IntVar()
                                var3=IntVar()
                                var4=IntVar()
                                var5=IntVar()
                                var6=IntVar()
                                var7=IntVar()
                                var8=IntVar()
                                var9=IntVar()

                                idli=Checkbutton(window,text='Idli',variable=var1,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                idli.place(x=130,y=130)
                                spin1=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin1.place(x=350,y=130)

                                gheeroast=Checkbutton(window,text='Ghee roast',variable=var2,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                gheeroast.place(x=130,y=180)
                                spin2=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin2.place(x=350,y=180)

                                parotta=Checkbutton(window,text='Parotta',variable=var3,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                parotta.place(x=130,y=230)
                                spin3=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin3.place(x=350,y=230)

                                onionparatha=Checkbutton(window,text='Onion paratha',variable=var4,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                onionparatha.place(x=130,y=280)
                                spin4=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin4.place(x=350,y=280)

                                naan=Checkbutton(window,text='Naan',variable=var5,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                naan.place(x=130,y=330)
                                spin5=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin5.place(x=350,y=330)

                                butternaan=Checkbutton(window,text='Butter naan',variable=var6,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                butternaan.place(x=130,y=380)
                                spin6=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin6.place(x=350,y=380)

                                veghakkanoodles=Checkbutton(window,text='Veg hakka noodles',variable=var7,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                veghakkanoodles.place(x=130,y=430)
                                spin7=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin7.place(x=350,y=430)

                                masalacheesedosa=Checkbutton(window,text='Masala cheese dosa',variable=var8,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                masalacheesedosa.place(x=130,y=480)
                                spin8=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin8.place(x=350,y=480)

                                riceupma=Checkbutton(window,text='Rice upma',variable=var9,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                riceupma.place(x=130,y=530)
                                spin9=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin9.place(x=350,y=530)

                                columns = ('NAME','PRICE')
                                wth=[160,50]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window, columns=columns, show='headings',height=13)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=585,y=160)
                                cur.execute('SELECT NAME,PRICE FROM Services WHERE service_id LIKE "RD%"')
                                records=cur.fetchall()
                                for record in records:
                                    tree.insert('',END,values=record)

                                def get_price_of_service(service_id):
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                    t=cur.fetchall()
                                    lprice = int(t[0][1])
                                    return(lprice)

                                def insert_to_services_db(booking_id, service_id, room_no, qty):
                                    if (qty == 0):
                                        return
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select uservice_id from user_services")
                                    t=len(cur.fetchall())
                                    uservice_id = "U" + str(t+1)
                                    price = get_price_of_service(service_id)
                                    cost = qty * price
                                    try:
                                       sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                                  VALUES (%s, %s, %s, %s, %s, %s)"
                                       val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                       mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                       cur=mydb.cursor()
                                       cur.execute(sql, val)
                                       mydb.commit()

                                    except Exception as e:
                                       print(e)
                                       mydb.rollback()
                                       mydb.close()


                                def okbutton():
                                    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get()) and ent1.get():
                                        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                        cursor = db.cursor()
                                        query = "SELECT name,price FROM services"
                                        cursor.execute(query)
                                        names = cursor.fetchall()
                                        lst=[]
                                        lst1=[]
                                        lst2=[]
                                        for name in names:
                                            lst+=[name][0]
                                        for i in range(len(lst)):
                                            if i%2==0:
                                                lst1+=[lst[i]]
                                            else:
                                                lst2+=[lst[i]]
                                        
                                        totlunch=0
                                            
                                        if var1.get()==1:
                                            m1=lst1.index('IDLI')
                                            a1=lst2[m1]
                                            n1=spin1.get()
                                            cost1=a1*(float(n1))
                                            totlunch+=cost1
                                                
                                                    
                                        if var2.get()==1:
                                            m2=lst1.index('GHEE ROAST')
                                            a2=lst2[m2]
                                            n2=spin2.get()
                                            cost2=a2*(float(n2))
                                            totlunch+=cost2
                                            
                                        if var3.get()==1:
                                            m3=lst1.index('PAROTTA')
                                            a3=lst2[m3]
                                            n3=spin3.get()
                                            cost3=a3*(float(n3))
                                            totlunch+=cost3
                                            
                                        if var4.get()==1:
                                            m4=lst1.index('ONION PARATHA')
                                            a4=lst2[m4]
                                            n4=spin4.get()
                                            cost4=a4*(float(n4))
                                            totlunch+=cost4

                                        if var5.get()==1:
                                            m5=lst1.index('NAAN')
                                            a5=lst2[m5]
                                            n5=spin5.get()
                                            cost5=a5*(float(n5))
                                            totlunch+=cost5
                                    
                                        if var6.get()==1:
                                            m6=lst1.index('BUTTER NAAN')
                                            a6=lst2[m6]
                                            n6=spin6.get()
                                            cost6=a6*(float(n6))
                                            totlunch+=cost6

                                        if var7.get()==1:
                                            m7=lst1.index('VEG HAKKA NOODLES')
                                            a7=lst2[m7]
                                            n7=spin7.get()
                                            cost7=a7*(float(n7))
                                            totlunch+=cost7
                                            
                                        if var8.get()==1:
                                            m8=lst1.index('MASALA CHEESE DOSA')
                                            a8=lst2[m8]
                                            n8=spin8.get()
                                            cost8=a8*(float(n8))
                                            totlunch+=cost8

                                        if var9.get()==1:
                                            m9=lst1.index('RICE UPMA')
                                            a9=lst2[m9]
                                            n9=spin9.get()
                                            cost9=a9*(float(n9))
                                            totlunch+=cost9

                                        totcost=totlunch
                                        

                                        room_no = ent1.get()
                                        booking_id = value[lst0.index(room_no)][0]

                                        g1 = spin1.get()
                                        service_id="RD01"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g1))
                                
                                        g2 = spin2.get()
                                        service_id="RD02"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g2))

                                        g3 = spin3.get()
                                        service_id="RD03"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g3))
                                
                                        g4 = spin4.get()
                                        service_id="RD04"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g4))

                                        g5 = spin5.get()
                                        service_id="RD05"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g5))

                                        g6 = spin6.get()
                                        service_id="RD06"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g6))

                                        g7 = spin7.get()
                                        service_id="RD07"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g7))

                                        g8 = spin8.get()
                                        service_id="RD08"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g8))

                                        g9 = spin9.get()
                                        service_id="RD09"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g9))

                                        lbl2=Label(window,fg="forest green",text="Rs "+str(totlunch),font=("Cambria",16,"bold"),width=12)
                                        lbl2.place(x=750,y=470)

                                        messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                                lbl1=Label(window,text="FOOD'S COST",fg="forest green",font=("Cambria",16,"bold"),width=12)
                                lbl1.place(x=580,y=470)
                           
                                lbl20=Label(window,fg="forest green",text="ROOM NO.",font=("Cambria",16,"bold"),width=12)
                                lbl20.place(x=580,y=510)
                                s=StringVar()
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                                value=cur.fetchall()
                                lst0=[]
                                for i in value:
                                     lst0.append(i[1])
                                m=StringVar()
                                ent1=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                                ent1['values']=lst0
                                ent1.place(x=750,y=510)

                                btn6=Button(window,text="OK",font=("Cambria",14),fg="blanched almond",bg="forest green",width=6,command=okbutton)
                                btn6.place(x=500,y=620)

                                window.mainloop()

                            ################################################################                            ################################################################
                                
                            def Bd():
                                window.destroy()
                                bd()
                            def bd():
                                def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                                def back():
                                    window.destroy()
                                    Restaurant_Func()

                                window=Tk()
                                window.title("BEVERAGES AND DRINKS")
                                window.geometry("1000x700")
                                bg = PhotoImage(file = "beverages bg.png")
                                lbl8=Label(window,image=bg)
                                lbl8.place(x=0,y=0)

                                lbl=Label(window,text="BEVERAGES AND DRINKS",fg="forest green",font=("Cambria",36,"bold"),width=20)
                                lbl.place(x=250,y=30)
                                btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn4=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn4.place(x=870,y=10)

                                var1=IntVar()
                                var2=IntVar()
                                var3=IntVar()
                                var4=IntVar()
                                var5=IntVar()
                                var6=IntVar()
                                var7=IntVar()
                                var8=IntVar()

                                filtercoffee=Checkbutton(window,text='Filter coffee',variable=var1,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                filtercoffee.place(x=130,y=130)
                                spin1=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin1.place(x=350,y=130)

                                tea=Checkbutton(window,text='Tea',variable=var2,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                tea.place(x=130,y=180)
                                spin2=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin2.place(x=350,y=180)

                                badammilk=Checkbutton(window,text='Badam milk',variable=var3,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                badammilk.place(x=130,y=230)
                                spin3=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin3.place(x=350,y=230)

                                rosemilk=Checkbutton(window,text='Rose milk',variable=var4,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                rosemilk.place(x=130,y=280)
                                spin4=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin4.place(x=350,y=280)

                                soup=Checkbutton(window,text='Soup',variable=var5,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                soup.place(x=130,y=330)
                                spin5=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin5.place(x=350,y=330)

                                fruitjuice=Checkbutton(window,text='Fruit juice',variable=var6,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                fruitjuice.place(x=130,y=380)
                                spin6=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin6.place(x=350,y=380)

                                cocacola=Checkbutton(window,text='Coca cola',variable=var7,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                cocacola.place(x=130,y=430)
                                spin7=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin7.place(x=350,y=430)

                                miranda=Checkbutton(window,text='Miranda',variable=var8,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                miranda.place(x=130,y=480)
                                spin8=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin8.place(x=350,y=480)

                                columns = ('NAME','PRICE')
                                wth=[160,50]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window, columns=columns, show='headings',height=13)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=585,y=160)
                                cur.execute('SELECT NAME,PRICE FROM Services WHERE service_id LIKE "RBD%"')
                                records=cur.fetchall()
                                for record in records:
                                    tree.insert('',END,values=record)

                                def get_price_of_service(service_id):
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                    t=cur.fetchall()
                                    lprice = int(t[0][1])
                                    return(lprice)

                                def insert_to_services_db(booking_id, service_id, room_no, qty):
                                    if (qty == 0):
                                        return
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select uservice_id from user_services")
                                    t=len(cur.fetchall())
                                    uservice_id = "U" + str(t+1)
                                    price = get_price_of_service(service_id)
                                    cost = qty * price
                                    try:
                                       sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                                  VALUES (%s, %s, %s, %s, %s, %s)"
                                       val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                       mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                       cur=mydb.cursor()
                                       cur.execute(sql, val)
                                       mydb.commit()

                                    except Exception as e:
                                       print(e)
                                       mydb.rollback()
                                       mydb.close()

                                def okbutton():
                                    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get()) and ent1.get():
                                        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                        cursor = db.cursor()
                                        query = "SELECT name,price FROM services"
                                        cursor.execute(query)
                                        names = cursor.fetchall()
                                        lst=[]
                                        lst1=[]
                                        lst2=[]
                                        for name in names:
                                            lst+=[name][0]
                                        for i in range(len(lst)):
                                            if i%2==0:
                                                lst1+=[lst[i]]
                                            else:
                                                lst2+=[lst[i]]
                                        
                                        totlunch=0
                                            
                                        if var1.get()==1:
                                            m1=lst1.index('FILTER COFFEE')
                                            a1=lst2[m1]
                                            n1=spin1.get()
                                            cost1=a1*(float(n1))
                                            totlunch+=cost1
                                                         
                                        if var2.get()==1:
                                            m2=lst1.index('TEA')
                                            a2=lst2[m2]
                                            n2=spin2.get()
                                            cost2=a2*(float(n2))
                                            totlunch+=cost2
                                            
                                        if var3.get()==1:
                                            m3=lst1.index('BADAM MILK')
                                            a3=lst2[m3]
                                            n3=spin3.get()
                                            cost3=a3*(float(n3))
                                            totlunch+=cost3
                                            
                                        if var4.get()==1:
                                            m4=lst1.index('ROSE MILK')
                                            a4=lst2[m4]
                                            n4=spin4.get()
                                            cost4=a4*(float(n4))
                                            totlunch+=cost4

                                        if var5.get()==1:
                                            m5=lst1.index('SOUP')
                                            a5=lst2[m5]
                                            n5=spin5.get()
                                            cost5=a5*(float(n5))
                                            totlunch+=cost5

                                            
                                        if var6.get()==1:
                                            m6=lst1.index('FRUIT JUICE')
                                            a6=lst2[m6]
                                            n6=spin6.get()
                                            cost6=a6*(float(n6))
                                            totlunch+=cost6

                                        if var7.get()==1:
                                            m7=lst1.index('COCA COLA')
                                            a7=lst2[m7]
                                            n7=spin7.get()
                                            cost7=a7*(float(n7))
                                            totlunch+=cost7
                                            
                                        if var8.get()==1:
                                            m8=lst1.index('MIRANDA')
                                            a8=lst2[m8]
                                            n8=spin8.get()
                                            cost8=a8*(float(n8))
                                            totlunch+=cost8
                                        
                                        totcost=totlunch
                                        

                                        room_no = ent1.get()
                                        booking_id = value[lst0.index(room_no)][0]

                                        g1 = spin1.get()
                                        service_id="RBD01"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g1))
                                
                                        g2 = spin2.get()
                                        service_id="RBD02"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g2))

                                        g3 = spin3.get()
                                        service_id="RBD03"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g3))
                                
                                        g4 = spin4.get()
                                        service_id="RBD04"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g4))

                                        g5 = spin5.get()
                                        service_id="RBD05"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g5))

                                        g6 = spin6.get()
                                        service_id="RBD06"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g6))

                                        g7 = spin7.get()
                                        service_id="RBD07"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g7))

                                        g8 = spin8.get()
                                        service_id="RBD08"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g8))
                                        

                                        lbl2=Label(window,fg="forest green",text="Rs "+str(totlunch),font=("Cambria",16,"bold"),width=12)
                                        lbl2.place(x=750,y=470)

                                        messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                                lbl1=Label(window,text="FOOD'S COST",fg="forest green",font=("Cambria",16,"bold"),width=12)
                                lbl1.place(x=580,y=470)
                            
                                lbl20=Label(window,fg="forest green",text="ROOM NO.",font=("Cambria",16,"bold"),width=12)
                                lbl20.place(x=580,y=510)
                                s=StringVar()
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                                value=cur.fetchall()
                                lst0=[]
                                for i in value:
                                     lst0.append(i[1])
                                m=StringVar()
                                ent1=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                                ent1['values']=lst0
                                ent1.place(x=750,y=510)
                            
                                btn6=Button(window,text="OK",font=("Cambria",14),fg="blanched almond",bg="forest green",width=6,command=okbutton)
                                btn6.place(x=500,y=620)

                                window.mainloop()

                            ################################################################                        ################################################################

                            def Qb():
                                window.destroy()
                                qb()
                            def qb():
                                def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                                def back():
                                    window.destroy()
                                    Restaurant_Func()

                                window=Tk()
                                window.title("QUICK BITES")
                                window.geometry("1000x700")
                                bg = PhotoImage(file = "quick bites bg.png")
                                lbl8=Label(window,image=bg)
                                lbl8.place(x=0,y=0)

                                lbl=Label(window,text="QUICK BITES",fg="forest green",font=("Cambria",36,"bold"),width=15)
                                lbl.place(x=290,y=30)
                                btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn4=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn4.place(x=870,y=10)

                                var1=IntVar()
                                var2=IntVar()
                                var3=IntVar()
                                var4=IntVar()
                                var5=IntVar()
                                var6=IntVar()
                                var7=IntVar()
                                var8=IntVar()
                                var9=IntVar()

                                breadpockets=Checkbutton(window,text='Breadpockets',variable=var1,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                breadpockets.place(x=130,y=130)
                                spin1=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state= "readonly")
                                spin1.place(x=350,y=130)

                                pizza=Checkbutton(window,text='Pizza',variable=var2,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                pizza.place(x=130,y=180)
                                spin2=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin2.place(x=350,y=180)

                                gobimanchurian=Checkbutton(window,text='Gobi manchurian',variable=var3,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                gobimanchurian.place(x=130,y=230)
                                spin3=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin3.place(x=350,y=230)

                                burger=Checkbutton(window,text='Burger',variable=var4,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                burger.place(x=130,y=280)
                                spin4=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin4.place(x=350,y=280)

                                samosa=Checkbutton(window,text='Samosa',variable=var5,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                samosa.place(x=130,y=330)
                                spin5=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin5.place(x=350,y=330)

                                paneerpuffs=Checkbutton(window,text='Paneerpuffs',variable=var6,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                paneerpuffs.place(x=130,y=380)
                                spin6=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin6.place(x=350,y=380)

                                aloobonda=Checkbutton(window,text='Aloo bonda',variable=var7,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                aloobonda.place(x=130,y=430)
                                spin7=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin7.place(x=350,y=430)

                                bhelpuri=Checkbutton(window,text='Bhel puri',variable=var8,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                bhelpuri.place(x=130,y=480)
                                spin8=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin8.place(x=350,y=480)

                                dahipuri=Checkbutton(window,text='Dahi puri',variable=var9,onvalue=1,offvalue=0,font=('cambria',14,'bold'))
                                dahipuri.place(x=130,y=530)
                                spin9=Spinbox(window,from_=0,to=5,font=("cambria",16),width=8,state="readonly")
                                spin9.place(x=350,y=530)

                                columns = ('NAME','PRICE')
                                wth=[160,50]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window, columns=columns, show='headings',height=13)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=585,y=160)
                                cur.execute('SELECT NAME,PRICE FROM Services WHERE service_id LIKE "RQ%"')
                                records=cur.fetchall()
                                for record in records:
                                    tree.insert('',END,values=record)

                                def get_price_of_service(service_id):
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                    t=cur.fetchall()
                                    lprice = int(t[0][1])
                                    return(lprice)

                                def insert_to_services_db(booking_id, service_id, room_no, qty):
                                    if (qty == 0):
                                        return
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                    cur=mydb.cursor()
                                    cur.execute("select uservice_id from user_services")
                                    t=len(cur.fetchall())
                                    uservice_id = "U" + str(t+1)
                                    price = get_price_of_service(service_id)
                                    cost = qty * price
                                    try:
                                       sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                                  VALUES (%s, %s, %s, %s, %s, %s)"
                                       val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                       mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                       cur=mydb.cursor()
                                       cur.execute(sql, val)
                                       mydb.commit()

                                    except Exception as e:
                                       print(e)
                                       mydb.rollback()
                                       mydb.close()


                                def okbutton():
                                    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get()) and ent1.get():
                                        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                        cursor = db.cursor()
                                        query = "SELECT name,price FROM services"
                                        cursor.execute(query)
                                        names = cursor.fetchall()
                                        lst=[]
                                        lst1=[]
                                        lst2=[]
                                        for name in names:
                                            lst+=[name][0]
                                        for i in range(len(lst)):
                                            if i%2==0:
                                                lst1+=[lst[i]]
                                            else:
                                                lst2+=[lst[i]]
                                        
                                        totlunch=0
                                            
                                        if var1.get()==1:
                                            m1=lst1.index('BREAD POCKETS')
                                            a1=lst2[m1]
                                            n1=spin1.get()
                                            cost1=a1*(float(n1))
                                            totlunch+=cost1
                                                
                                                    
                                        if var2.get()==1:
                                            m2=lst1.index('PIZZA')
                                            a2=lst2[m2]
                                            n2=spin2.get()
                                            cost2=a2*(float(n2))
                                            totlunch+=cost2
                                            
                                        if var3.get()==1:
                                            m3=lst1.index('GOBI MANCHURIAN')
                                            a3=lst2[m3]
                                            n3=spin3.get()
                                            cost3=a3*(float(n3))
                                            totlunch+=cost3
                                            
                                        if var4.get()==1:
                                            m4=lst1.index('BURGER')
                                            a4=lst2[m4]
                                            n4=spin4.get()
                                            cost4=a4*(float(n4))
                                            totlunch+=cost4

                                        if var5.get()==1:
                                            m5=lst1.index('SAMOSA')
                                            a5=lst2[m5]
                                            n5=spin5.get()
                                            cost5=a5*(float(n5))
                                            totlunch+=cost5

                                            
                                        if var6.get()==1:
                                            m6=lst1.index('PANEER PUFFS')
                                            a6=lst2[m6]
                                            n6=spin6.get()
                                            cost6=a6*(float(n6))
                                            totlunch+=cost6

                                        if var7.get()==1:
                                            m7=lst1.index('ALOO BONDA')
                                            a7=lst2[m7]
                                            n7=spin7.get()
                                            cost7=a7*(float(n7))
                                            totlunch+=cost7
                                            
                                        if var8.get()==1:
                                            m8=lst1.index('BHEL PURI')
                                            a8=lst2[m8]
                                            n8=spin8.get()
                                            cost8=a8*(float(n8))
                                            totlunch+=cost8

                                        if var9.get()==1:
                                            m9=lst1.index('DAHI PURI')
                                            a9=lst2[m9]
                                            n9=spin9.get()
                                            cost9=a9*(float(n9))
                                            totlunch+=cost9
                                        totcost=totlunch
                                       

                                        room_no = ent1.get()
                                        booking_id = value[lst0.index(room_no)][0]

                                        g1 = spin1.get()
                                        service_id="RQ01"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g1))
                                
                                        g2 = spin2.get()
                                        service_id="RQ02"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g2))

                                        g3 = spin3.get()
                                        service_id="RQ03"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g3))
                                
                                        g4 = spin4.get()
                                        service_id="RQ04"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g4))

                                        g5 = spin5.get()
                                        service_id="RQ05"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g5))

                                        g6 = spin6.get()
                                        service_id="RQ06"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g6))

                                        g7 = spin7.get()
                                        service_id="RQ07"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g7))

                                        g8 = spin8.get()
                                        service_id="RQ08"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g8))

                                        g9 = spin9.get()
                                        service_id="RQ09"
                                        insert_to_services_db(booking_id, service_id, room_no, int(g9))

                                        lbl2=Label(window,fg="forest green",text="Rs "+str(totlunch),font=("Cambria",16,"bold"),width=12)
                                        lbl2.place(x=750,y=470)

                                        messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")
                                    

                                lbl1=Label(window,text="FOOD'S COST",fg="forest green",font=("Cambria",16,"bold"),width=12)
                                lbl1.place(x=580,y=470)
                           
                                lbl20=Label(window,fg="forest green",text="ROOM NO.",font=("Cambria",16,"bold"),width=12)
                                lbl20.place(x=580,y=510)
                                s=StringVar()
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                                value=cur.fetchall()
                                lst0=[]
                                for i in value:
                                     lst0.append(i[1])
                                m=StringVar()
                                ent1=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                                ent1['values']=lst0
                                ent1.place(x=750,y=510)
                                
                                btn6=Button(window,text="OK",font=("Cambria",14),fg="blanched almond",bg="forest green",width=6,command= okbutton)
                                btn6.place(x=500,y=620)

                                window.mainloop()

                                
                            btn3=Button(window,text="LUNCH",font=("Cambria",16),fg="blanched almond",bg="forest green",width=20,command=Lunch)
                            btn3.place(x=400,y=270)

                            btn4=Button(window,text="DINNER",font=("Cambria",16),fg="blanched almond",bg="forest green",width=20,command=Dinner)
                            btn4.place(x=400,y=340)

                            btn5=Button(window,text="BEVERAGES AND DRINKS",font=("Cambria",16),fg="blanched almond",bg="forest green",width=20,command=Bd)
                            btn5.place(x=400,y=410)

                            btn6=Button(window,text="QUICK BITES",font=("Cambria",16),fg="blanched almond",bg="forest green",width=20,command=Qb)
                            btn6.place(x=400,y=480)

                            btn1=Button(window,text="BREAKFAST",font=("Cambria",16),fg="blanched almond",bg="forest green",width=20,command=Breakfast)
                            btn1.place(x=400,y=200)

                            window.mainloop()

                        #################################################################                      #################################################################
                            
                        def Other_Services_Func():
                            window = Tk()
                            window.title("ROOM SERVICES")
                            window.geometry("1000x700")
                            window["bg"]="white"

                            def ExitCmd():
                                 window.destroy()
                                 Home_Page_Func()
                                        
                            def BackCmd():
                                window.destroy()
                                Room_Service_Func()

                            def get_price_of_service(service_id):
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                                t=cur.fetchall()
                                lprice = int(t[0][1])
                                return(lprice)

                            def insert_to_services_db(booking_id, service_id, room_no, qty):
                                if (qty == 0):
                                    return
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                cur=mydb.cursor()
                                cur.execute("select uservice_id from user_services")
                                t=len(cur.fetchall())
                                uservice_id = "U" + str(t+1)
                                price = get_price_of_service(service_id)
                                cost = qty * price
                                try:
                                   sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                              VALUES (%s, %s, %s, %s, %s, %s)"
                                   val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                                   mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                                   cur=mydb.cursor()
                                   cur.execute(sql, val)
                                   mydb.commit()

                                except Exception as e:
                                   print(e)
                                   mydb.rollback()
                                   mydb.close()
                                   
                            def Ok():
                                if sp42.get():
                                    room_no = sp42.get()
                                    booking_id = value[lst.index(room_no)][0]

                                    lcount = sp37.get()
                                    service_id="S1001"
                                    insert_to_services_db(booking_id, service_id, room_no, int(lcount))
                                    
                                    dcount = sp38.get()
                                    service_id="S1002"
                                    insert_to_services_db(booking_id, service_id, room_no, int(dcount))

                                    pcount = sp39.get()
                                    service_id="S1006"
                                    insert_to_services_db(booking_id, service_id, room_no, int(pcount))
                                    
                                    rhcount = sp40.get()
                                    service_id="S1009"
                                    insert_to_services_db(booking_id, service_id, room_no, int(rhcount))

                                    acount = sp41.get()
                                    service_id="S1010"
                                    insert_to_services_db(booking_id, service_id, room_no, int(acount))

                                    messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                            bg = PhotoImage(file="user images.png")
                            label1 = Label( window, image = bg)
                            label1.place(x = 0, y = 0)


                            lbl36=Label(window,fg="forest green",text="ROOM SERVICES",font=("Cambria",36),  width=20)
                            lbl36.place(x=280,y=80)

                            btn32 = Button(window,text="BACK",bg="forest green",fg="white",font=("Cambria",16), width=8, command=BackCmd)
                            btn32.place(x=10, y= 10)

                            btn132 = Button(window,text="SIGNOUT",bg="forest green",fg="white",font=("Cambria",16), width=9, command=ExitCmd)
                            btn132.place(x=870, y= 10)

                            lbl37=Label(window,fg="forest green",text="LAUNDRY",  font=("Cambria",16, "bold"))
                            lbl37.place(x=180,y=230)
                            sp37=Spinbox(window, from_= 0, to = 20)
                            sp37.place(x=370,y=230)

                            lbl38=Label(window,fg="forest green",text="DRY CLEANING",  font=("Cambria",16, "bold"))
                            lbl38.place(x=180,y=280)
                            sp38=Spinbox(window, from_= 0, to = 20)
                            sp38.place(x=370,y=280)

                            lbl39=Label(window,fg="forest green",text="POSTAL SERVICE",    font=("Cambria",16, "bold"))
                            lbl39.place(x=180,y=330)
                            sp39=Spinbox(window, from_= 0, to = 20)
                            sp39.place(x=370,y=330)

                            lbl40=Label(window,fg="forest green",text="ROOM HEATER",    font=("Cambria",16, "bold"))
                            lbl40.place(x=180,y=380)
                            sp40=Spinbox(window, from_= 0, to = 20)
                            sp40.place(x=370,y=380)

                            lbl41=Label(window,fg="forest green",text="AIR COOLER",    font=("Cambria",16, "bold"))
                            lbl41.place(x=180,y=430)
                            sp41=Spinbox(window, from_= 0, to = 20)
                            sp41.place(x=370,y=430)

                            lbl42=Label(window,fg="forest green",text="ROOM NO",  font=("Cambria",16, "bold"))
                            lbl42.place(x=180,y=480)

                            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                            cur=mydb.cursor()
                            cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                            value=cur.fetchall()
                            lst=[]
                            for i in value:
                                lst.append(i[1])
                            m=StringVar()
                            sp42=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                            sp42['values']=lst
                            sp42.place(x=370,y=482)

                            columns = ('NAME','PRICE','UNITS')
                            wth=[160,50,113]
                            tree = ttk.Treeview(window, columns=columns, show='headings',height=10)
                            for i in range(len(columns)):
                                tree.heading(columns[i],text=columns[i])
                                tree.column(columns[i],width=wth[i])
                            tree.place(x=85,y=170)
                            cur.execute('SELECT NAME,PRICE,UNITS FROM Services WHERE SERVICE_ID in ("S1001","S1002","S1006","S1009","S1010")')
                            records=cur.fetchall()
                            for record in records:
                                tree.insert('',END,values=record)
                            tree.place(x=600,y=260)

                            btn34 = Button(window,bg="forest green",fg="white",text="CONFIRM",font=("Cambria",16),  width=16, command=Ok)
                            btn34.place(x=750, y=600)

                            window.mainloop()

                        window=Tk()
                        window.title("ROOM SERVICE PAGE")
                        window.geometry("1000x700")

                        bgimage=PhotoImage(file='user images.png')
                        bg=Label(window,image=bgimage)
                        bg.place(x=0,y=0)

                        signout=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                        signout.place(x=870,y=10)

                        back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=user_home_page_back_func)
                        back.place(x=10,y=10)

                        label1=Label(window,text="ROOM SERVICES",font=('Cambria',36,'bold'),fg="forest green",width=20)
                        label1.place(x=220,y=90)

                        restaurant=Button(window,text='RESTAURANT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=restaurant_func)
                        restaurant.place(x=350,y=250)

                        other_services=Button(window,text='OTHER SERVICES',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=other_services_func)
                        other_services.place(x=350,y=430)

                        window.mainloop()

                #####################################################################             #####################################################################
                        
                def open_bookings():
                    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hotel')
                    cur=mydb.cursor()
                    def sign_out_func():
                            window.destroy()
                            Home_Page_Func()

                    def user_home_page_back_func():
                            window.destroy()
                            User_Home_Page_Func()

                    window = Tk()
                    window.title('open bookings page')
                    window.geometry('1000x700')

                    bgimage=PhotoImage(file='user images.png')   
                    bg=Label(window,image=bgimage)
                    bg.place(x=0,y=0)

                    signout=Button(window,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                    signout.place(x=870,y=10)

                    back=Button(window,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=user_home_page_back_func)
                    back.place(x=10,y=10)

                    label4=Label(window,text="CURRENT STAYS",font=('Cambria',34,'bold'),fg='forest green',width=20)
                    label4.place(x=250,y=50)

                    columns = ('BOOKING_ID','PLACE','CHECKIN','CHECKOUT')
                    wth=[120,120,120,120]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=9)
                    for i in range(len(columns)):
                        tree.heading(columns[i],text=columns[i])
                        tree.column(columns[i],width=wth[i],anchor=CENTER)

                    cur.execute('SELECT DISTINCT BOOKING_ID,PLACE,CHECKIN,CHECKOUT FROM BOOKING_DETAILS,BRANCH WHERE ID="'+userid+'" AND CHECKOUT >= NOW() AND BOOKING_DETAILS.HOTEL_ID=BRANCH.HOTEL_ID')
                    records=cur.fetchall()
                    for record in records:
                        tree.insert('',END,values=record)    
                    tree.place(x=265,y=190)

                    def Reservations_Func(x):
                        
                        values=tree.item(tree.focus())['values']
                        window.destroy()
                        
                        def sign_out_func():
                            window1.destroy()
                            Home_Page_Func()

                        def back_func():
                            window1.destroy()
                            open_bookings()

                        window1 = Tk()
                        window1.title('open bookings page')
                        window1.geometry('1000x700')

                        bgimage=PhotoImage(file='user images.png')
                        bg=Button(window1,image=bgimage)
                        bg.place(x=0,y=0)

                        signout=Button(window1,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                        signout.place(x=870,y=10)

                        back=Button(window1,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=back_func)
                        back.place(x=10,y=10)

                        if values[2]>str(datetime.date.today()):
                            columns = ('BOOKING_ID','ID','PLACE','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                            wth=[89,53,100,120,80,80,80,60,80]
                            tree1 = ttk.Treeview(window1, columns=columns, show='headings',height=14)
                            for i in range(len(columns)):
                                tree1.heading(columns[i],text=columns[i])
                                tree1.column(columns[i],width=wth[i],anchor=CENTER)

                            cur.execute('SELECT BOOKING_ID,ID,PLACE,NAME,ROOM_NO,CHECKIN,CHECKOUT,ADULTS,CHILDREN FROM BOOKING_DETAILS,BRANCH\
                                WHERE BOOKING_DETAILS.HOTEL_ID=BRANCH.HOTEL_ID AND BOOKING_ID="'+values[0]+'"')
                            records=cur.fetchall()
                            for record in records:
                                tree1.insert('',END,values=record)    
                            tree1.place(x=125,y=140)

                            def cancel():
                                cur.execute('DELETE FROM BOOKING_DETAILS WHERE BOOKING_ID="'+values[0]+'"')
                                mydb.commit()
                                messagebox.showinfo('info','Reservations for Booking ID : '+values[0]+' Cancelled Successfully')

                            cancel=Button(window1,text='CANCEL BOOKING',font=('Cambria',19),bg='forest green',fg='blanched almond',width=18,command=cancel)
                            cancel.place(x=380,y=550 )

                        elif values[2]<=str(datetime.date.today()):
                            columns = ('BOOKING_ID','ID','PLACE','NAME','ROOM_NO','CHECKIN','CHECKOUT','ADULTS','CHILDREN')
                            wth=[89,53,100,120,80,80,80,60,80]
                            tree1 = ttk.Treeview(window1, columns=columns, show='headings',height=5)
                            for i in range(len(columns)):
                                    tree1.heading(columns[i],text=columns[i])
                                    tree1.column(columns[i],width=wth[i],anchor=CENTER)

                            cur.execute('SELECT BOOKING_ID,ID,PLACE,NAME,ROOM_NO,CHECKIN,CHECKOUT,ADULTS,CHILDREN FROM BOOKING_DETAILS,BRANCH\
                                WHERE BOOKING_DETAILS.HOTEL_ID=BRANCH.HOTEL_ID AND BOOKING_ID="'+values[0]+'"')
                            records=cur.fetchall()
                            for record in records:
                                tree1.insert('',END,values=record)    
                            tree1.place(x=125,y=90)

                            columns = ('USERVICE_ID','BOOKING_ID','NAME','ROOM_NO','QUANTITY','COST','PAYMENT')
                            wth=[80,80,130,80,80,80,80]
                            tree2 = ttk.Treeview(window1, columns=columns, show='headings',height=12)
                            for i in range(len(columns)):
                                tree2.heading(columns[i],text=columns[i])
                                tree2.column(columns[i],width=wth[i],anchor=CENTER)
                            cur.execute('SELECT USERVICE_ID,BOOKING_ID,NAME,ROOM_NO,QTY,COST,PAYMENT FROM User_Services,services\
                                WHERE BOOKING_ID ="'+values[0]+'" AND User_Services.SERVICE_ID=services.SERVICE_ID')
                            records=cur.fetchall()
                            for record in records:
                                tree2.insert('',END,values=record)    
                            tree2.place(x=125,y=275)

                            def services_payment_func():
                                window1.destroy()

                                def sign_out_func():
                                    window2.destroy()
                                    Home_Page_Func()

                                def back_func():
                                    window2.destroy()
                                    open_bookings()

                                window2 = Tk()
                                window2.title('open bookings page')
                                window2.geometry('1000x700')

                                mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hotel')
                                cur=mydb.cursor()

                                bgimage=PhotoImage(file='user images.png')
                                bg=Label(window2,image=bgimage)
                                bg.place(x=0,y=0)

                                signout=Button(window2,text='SIGN OUT',font=('Cambria',16),bg='forest green',width=9,fg='blanched almond',command=sign_out_func)
                                signout.place(x=870,y=10)

                                back=Button(window2,text="BACK",font=("Cambria",16),bg="forest green",width=8,fg='blanched almond',command=back_func)
                                back.place(x=10,y=10)

                                bill=Text(window2,font=("Californian FB",16),bd=5,width=39,height=21)
                                bill.place(x=100,y=110)

                                bill.insert(END,'\n')

                                cur.execute('SELECT NAME,QTY*COST FROM User_Services,services\
                                WHERE BOOKING_ID ="'+values[0]+'" AND User_Services.SERVICE_ID=services.SERVICE_ID AND PAYMENT="PENDING"')
                                records=cur.fetchall()
                                tot_cost=0
                                for record in records:
                                    bill.insert(END,'     '+record[0]+'\t\t\tRs. '+str(record[1])+'\n')
                                    tot_cost+=record[1]

                                bill.insert(END,'\n    '+'-'*55+'\n')
                                bill.insert(END,'      '+'Total    :'+'\t\t\tRs. '+str(tot_cost)+'\n')
                                bill.insert(END,'      '+'Tax Amount(18%)    :'+'\t\t\tRs. '+str(0.18*tot_cost)+'\n')
                                bill.insert(END,'      '+'Grand Total    :'+'\t\t\tRs. '+str(0.18*tot_cost+tot_cost)+'\n')
                                bill.insert(END,'    '+'-'*55+'\n')

                                bill.config(state='disabled')

                                def ok():
                                    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hotel')
                                    cur=mydb.cursor()
                                    cur.execute('UPDATE USER_SERVICES SET PAYMENT="PAID" WHERE BOOKING_ID ="'+values[0]+'"')
                                    mydb.commit()
                                    messagebox.showinfo("User", "PAYMENT DONE SUCCESSFULLY!!")
                                
                                pay=Button(window2,text='PAYMENT',font=('Cambria',16),bg='forest green',fg='blanched almond',width=17,command=ok)
                                pay.place(x=640,y=540)

                                mydb.close()

                                window2.mainloop()

                            BILL=Button(window1,text='PROCEED TO PAY',font=('Cambria',16),bg='forest green',fg='blanched almond',width=17,command=services_payment_func)
                            BILL.place(x=660,y=570)
                                
                        window1.mainloop()

                    tree.bind('<ButtonRelease>', Reservations_Func)
                    
                    window.mainloop()

                #####################################################################       #####################################################################

                def Edit_Profile_Func():
                    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                    cur=mydb.cursor()

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def back_func():
                                window.destroy()
                                User_Home_Page_Func()            
                 
                    def GetDetails():
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM user_admin limit 0,10")
                        for user in mycursor:
                            if (userid == user[0]):
                               return user

                    def Ok():
                        if ent31.get() and ent32.get() and ent33.get() and ent41.get() and ent34.get() and ent35.get() and address.get("1.0","end-1c"):
                            username = ent31.get()
                            name = ent33.get()
                            gender = ent41.get()[0]
                            passwd = ent32.get()
                            phno = ent34.get()
                            email=ent35.get()
                            addr=address.get("1.0","end-1c")
                            if len(name) > 30:
                                messagebox.showinfo('error','Length of name should not exceed 30')
                                return
                            if not any(char.isalpha() for char in name):
                                messagebox.showerror('error','Invalid Name !')
                                return
                            
                            SpecialSym =['$', '@', '#', '%','!']
           
                            if len(username) < 4:
                                messagebox.showerror('error','Username should have atleast 4 characters')
                                return
                            if len(username) > 15:
                                messagebox.showerror('error','Length of username should not exceed 15')
                                return
                            if len(passwd) < 6:
                                messagebox.showerror('error','Password should have atleast 6 characters')
                                return             
                            if len(passwd) > 20:
                                messagebox.showerror('error','Length of password should not exceed 20')
                                return              
                            if not any(char.isdigit() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one numeral')
                                return            
                            if not any(char.isupper() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one uppercase letter')
                                return              
                            if not any(char.islower() for char in passwd):
                                messagebox.showerror('error','Password should have atleast one lowercase letter')
                                return
                            if not any(char in SpecialSym for char in passwd):
                                messagebox.showerror('error','Password should have atleast special character')
                                return
                            if (not str(phno).isdigit()) or len(str(phno))!=10:
                                messagebox.showerror('error','Invalid Phone Number !')
                                return
                            if '@' not in email:
                                messagebox.showerror('error','Invalid Email-Id !')
                                return

		     
                            mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                            mycursor=mydb.cursor()
                            mycursor.execute("SELECT * FROM user_admin limit 0,10")
                            i=0
                            found = 0
                            for user in mycursor:
                                if (userid == user[0]):
                                   idproof = user[3]
                                   data_update = (name,gender,idproof,int(phno),email,addr,username,passwd,user[0])
                                   found = 1
                                   break   
                            if (found == 1):
                                print ("Proceeding to update")
                                mydb1=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL')
                                cur=mydb1.cursor()
                                sql="UPDATE user_admin set  name=%s,gender=%s,idproof=%s,phoneno=%s,email=%s,address=%s,username=%s,pswd=%s where ID=%s"
                                try:
                                   cur.execute(sql, data_update)
                                   mydb1.commit()
                                except Exception as e:
                                   print(e)
                                   mydb1.rollback()
                                   mydb1.close()
                            messagebox.showinfo("User", "CHANGES STORED SUCCESSFULLY!!")

                    window = Tk()
                    window.title("EDIT PROFILE")
                    window.geometry("1000x700")
                    window["bg"]="blanched almond"
                    bg = PhotoImage(file="user images.png")
                    label1 = Label( window, image = bg)
                    label1.place(x = 0, y = 0)
                    data_display = GetDetails()

                    btn32 = Button(window,bg="forest green",fg="white",text="BACK",font=("Cambria",16),   width=8,command=back_func)
                    btn32.place(x=10, y= 10)
                    btn33 = Button(window,bg="forest green",fg="white",text="SIGNOUT",font=("Cambria",16),   width=8,command=sign_out_func)
                    btn33.place(x=870, y= 10)
                    lbl36=Label(window,text="EDIT PROFILE DETAILS",fg="forest green", font=("Cambria",36),   width=20)
                    lbl36.place(x=280,y=70)

                    lbl37=Label(window,text="USER NAME",fg="forest green", font=("Cambria",16, "bold"))
                    lbl37.place(x=180,y=180)
                    ent31=Entry(window)
                    ent31.config(font=("Californian F8", 16),bd=3,width=25)
                    ent31.delete(0, END)
                    ent31.insert(0, data_display[7])
                    ent31.place(x=370, y=180)

                    lbl38=Label(window,text="PASSWORD",fg="forest green",font=("Cambria",16, "bold"))
                    lbl38.place(x=180,y=230)
                    ent32=Entry(window)
                    ent32.config(font=("Californian F8", 16),bd=3,width=25)
                    ent32.delete(0, END)
                    ent32.insert(0, data_display[8])
                    ent32.place(x=370, y=230)

                    lbl39=Label(window,text="NAME",fg="forest green",font=("Cambria",16, "bold"))
                    lbl39.place(x=180,y=280)
                    ent33=Entry(window)
                    ent33.config(font=("Californian F8", 16),bd=3,width=25)
                    ent33.delete(0, END)
                    ent33.insert(0, data_display[1])
                    ent33.place(x=370, y=280)

                    lbl41=Label(window,text="GENDER",fg="forest green",font=("Cambria",16, "bold"))
                    lbl41.place(x=180,y=330)
                    ent441 = StringVar()
                    data=("Male", "Female")
                    ent41=ttk.Combobox(window, textvariable=ent441,font=("Californian F8",16),state="readonly")
                    ent41['values']=data
                    if (data_display[2] == "M"):
                        ent41.current(0)
                    else:
                        ent41.current(1)
                    ent41.place(x=370, y=330)

                    lbl40=Label(window,text="PHONE NUMBER",fg="forest green",font=("Cambria",16, "bold"))
                    lbl40.place(x=180,y=380)
                    ent34=Entry(window)
                    ent34.config(font=("Californian F8", 16),bd=3,width=25)
                    ent34.delete(0, END)
                    ent34.insert(0, data_display[4])
                    ent34.place(x=370, y=380)

                    lbl41=Label(window,text="EMAIL",fg="forest green",font=("Cambria",16, "bold"))
                    lbl41.place(x=180,y=430)
                    ent35=Entry(window)
                    ent35.config(font=("Californian F8", 16),bd=3,width=25)
                    ent35.delete(0, END)
                    ent35.insert(0, data_display[5])
                    ent35.place(x=370, y=430)

                    lbl42=Label(window,text="ADDRESS",fg="forest green",font=("Cambria",16, "bold"))
                    lbl42.place(x=180,y=490)
                    address=Text(window)
                    address.config(font=("Californian F8", 16),bd=3,width=25,height=6)
                    Fact=data_display[6]
                    address.insert(END, Fact)
                    address.place(x=370,y=490)

                    btn34 = Button(window,bg="forest green",fg="white",text="SAVE",font=("Cambria",16),   width=8, command=Ok)
                    btn34.place(x=750, y= 590)

                    window.mainloop()

                #####################################################################                #####################################################################
                    
                def Book_Rooms_Func():
                    window= Tk()
                    window.geometry("1000x700")
                    window.title("NEW BOOKING")
                    bg = PhotoImage(file = "user images.png")
                    lbl1=Label(window,image=bg)
                    lbl1.place(x=0,y=0)

                    def sign_out_func():
                        window.destroy()
                        Home_Page_Func()

                    def user_home_page_back_func():
                        window.destroy()
                        User_Home_Page_Func()

                    def explore2():
                        window.destroy()
                        Explore2()

                    def Explore2():

                        def back():
                            window.destroy()
                            Book_Rooms_Func()
                        
                        window = Tk()
                        window.geometry("1000x700")
                        window.title("BRANCH")
                        window["bg"]="blanched almond"

                        btn5=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                        btn5.place(x=10,y=10)

                        lbl=Label(window,fg="forest green",bg="blanched almond",text="HILLTOP HEAVEN RESORTS",font=("Cambria",26,"bold"),width=24)
                        lbl.place(x=290,y=20)

                        bg1 = PhotoImage(file="presidential suite.png")
                        label1 = Label( window, image = bg1)
                        label1.place(x = 150, y = 80)

                        bg2 = PhotoImage(file="one bedroom chalet.png")
                        label2 = Label( window, image = bg2)
                        label2.place(x =600, y = 80)

                        bg3 = PhotoImage(file="interconnecting rooms.png")
                        label3= Label( window, image = bg3)
                        label3.place(x = 150, y =400)

                        bg4 = PhotoImage(file="twin rooms.png")
                        label4= Label( window, image = bg4)
                        label4.place(x = 600, y =400)


                        mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel")
                        cur = mydb.cursor()
                        query="SELECT NAME, NOP,AC_nonAC,COST FROM ROOM_TYPE"
                        cur.execute(query)
                        names=cur.fetchall()

                        txt1=Text(window,fg="forest green",bg="blanched almond",font=("Cambria",16,"bold"),width=24,height=4)
                        txt1.place(x=105,y=260)

                        txt1.insert(END,'NAME:'+names[0][0])
                        txt1.insert(END,'\nNOP: '+str(names[0][1]))
                        txt1.insert(END,'\nAC/nonAC: '+names[0][2])
                        txt1.insert(END,'\nCOST: Rs. '+str(names[0][3]))
                        txt1.config(state="disabled")

                        txt2=Text(window,fg="forest green",bg="blanched almond",font=("Cambria",16,"bold"),width=26,height=4)
                        txt2.place(x=550,y=260)

                        txt2.insert(END,'NAME:'+names[1][0])
                        txt2.insert(END,'\nNOP: '+str(names[1][1]))
                        txt2.insert(END,'\nAC/nonAC: '+names[1][2])
                        txt2.insert(END,'\nCOST: Rs. '+str(names[1][3]))
                        txt2.config(state="disabled")

                        txt3=Text(window,fg="forest green",bg="blanched almond",font=("Cambria",16,"bold"),width=29,height=4)
                        txt3.place(x=85,y=580)

                        txt3.insert(END,'NAME:'+names[2][0])
                        txt3.insert(END,'\nNOP: '+str(names[2][1]))
                        txt3.insert(END,'\nAC/nonAC: '+names[2][2])
                        txt3.insert(END,'\nCOST: Rs. '+str(names[2][3]))
                        txt3.config(state="disabled")

                        txt4=Text(window,fg="forest green",bg="blanched almond",font=("Cambria",16,"bold"),width=23,height=4)
                        txt4.place(x=570,y=580)

                        txt4.insert(END,'NAME:'+names[3][0])
                        txt4.insert(END,'\nNOP: '+str(names[3][1]))
                        txt4.insert(END,'\nAC/nonAC: '+names[3][2])
                        txt4.insert(END,'\nCOST: Rs. '+str(names[2][3]))
                        txt4.config(state="disabled")

                        mydb.commit()
                        window.mainloop()
                    def explore1():
                        window.destroy()
                        Explore1()

                    def Explore1():
                        def back():
                            window.destroy()
                            Book_Rooms_Func()
                            
                        window = Tk()
                        window.geometry("1000x700")
                        window.title("BRANCH")
                        window["bg"]="blanched almond"

                        bg1 = PhotoImage(file="coorg image.png")
                        label1 = Label( window, image = bg1)
                        label1.place(x = 80, y = 160)
                        lbl1=Label(window,fg="forest green",bg="blanched almond",text="COORG",font=("Cambria",20,"bold"),width=14)
                        lbl1.place(x=85,y=100)

                        btn5=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                        btn5.place(x=10,y=10)

                        lbl=Label(window,fg="forest green",bg="blanched almond",text="HILLTOP HEAVEN RESORTS",font=("Cambria",26,"bold"),width=24)
                        lbl.place(x=290,y=20)

                        bg2 = PhotoImage(file="kodaikanal bg.png")
                        label2 = Label( window, image = bg2)
                        label2.place(x = 380, y = 160)
                        lbl2=Label(window,fg="forest green",bg="blanched almond",text="KODAIKANAL",font=("Cambria",20,"bold"),width=14)
                        lbl2.place(x=390,y=100)

                        bg3 = PhotoImage(file="munnar bg.png")
                        label3 = Label( window, image = bg3)
                        label3.place(x = 690, y = 160)
                        lbl3=Label(window,fg="forest green",bg="blanched almond",text="MUNNAR",font=("Cambria",20,"bold"),width=14)
                        lbl3.place(x=695,y=100)

                        lbl4=Label(window,fg="forest green",bg="blanched almond",text="7th Hoskote,\nSuntikoppa P.O.,\nKodagu, \nKarnataka 571237",font=("Cambria",14,"bold"),width=21, height=5)
                        lbl4.place(x=85,y=350)
                        lbl5=Label(window,fg="forest green",bg="blanched almond",text="NEARBY TOURIST SPOTS:  \n\n1. Raja's seat \n2. Madikeri fort \n3.Omkareshwara temple\n4. Abbey Falls \n5. Raja's tomb",font=("Cambria",14,"bold"),width=23, height=10)
                        lbl5.place(x=85,y=450)

                        lbl6=Label(window,fg="forest green",bg="blanched almond",text="17/328, Laws Ghat Rd, \nKodaikanal, \nTamil Nadu 624101",font=("Cambria",14,"bold"),width=21, height=5)
                        lbl6.place(x=385,y=350)
                        lbl7=Label(window,fg="forest green",bg="blanched almond",text="NEARBY TOURIST SPOTS:  \n\n1. Kodaikanal lake \n2. Bryant park \n3. Bear shola falls \n4. Coakers Walk \n5. Silver cascade falls",font=("Cambria",14,"bold"),width=21, height=10)
                        lbl7.place(x=385,y=450)

                        lbl6=Label(window,fg="forest green",bg="blanched almond",text="Bison Valley - \nPooppara Rd, Munnar, \nKerala 685612",font=("Cambria",14,"bold"),width=21, height=5)
                        lbl6.place(x=690,y=350)
                        lbl7=Label(window,fg="forest green",bg="blanched almond",text="NEARBY TOURIST SPOTS:  \n\n1. Tea museum \n2. Attukad Waterfalls \n3.Eravikulam national park \n4. The Blossom Hydel park \n5. Kolukumallai Tea Estate",font=("Cambria",14,"bold"),width=23, height=10)
                        lbl7.place(x=690,y=450)

                        window.mainloop()


                    btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=user_home_page_back_func)
                    btn2.place(x=10,y=10)
                    btn5=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                    btn5.place(x=870,y=10)

                    while True:
                        c="B"
                        n1=random.randint(10000,99999)
                        a=str(c)+str(n1)
                        sqlCon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                        cur=sqlCon.cursor()
                        cur.execute("select BOOKING_ID from booking_details where BOOKING_ID='"+a+"'")
                        if len(cur.fetchall())==0:break

                    lbl2=Label(window,text="BOOKING_ID:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl2.place(x=100,y=90)
                    lbl3=Label(window,fg="forest green",width=15,font=("Cambria",16,"bold"),text=a)
                    lbl3.place(x=250,y=90)

                    lbl5=Label(window,text="SELECT BRANCH:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl5.place(x=100,y=150)
                    lbl6=Label(window,text="CHECK IN:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl6.place(x=100,y=230)
                    lbl7=Label(window,text="CHECK OUT:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl7.place(x=450,y=230)

                    n=tk.StringVar()
                    combo1= ttk.Combobox(window, width = 20,font=("cambria",16), textvariable = n)
                    combo1.place(x=280,y=150)
                    combo1['values'] = ('KODAIKANAL','COORG','MUNNAR')

                    btn1=Button(window,text="EXPLORE",font=("Cambria",13),fg="blanched almond",bg="forest green",width=18,command=explore1)
                    btn1.place(x=580,y=150)

                    cal1 = DateEntry(window, width=12, bg='blue',font=("cambria",13),fg='white', borderwidth=2,selectmode='day')
                    cal1.place(x=210,y=230)
                    cal2 = DateEntry(window, width=12, bg='blue',fg='white',font=("cambria",13),borderwidth=2,selectmode='day')
                    cal2.place(x=590,y=230)

                    spin1=Spinbox(window,from_=0,to=5,font=("cambria",10),state="readonly")
                    spin1.place(x=270,y=285)
                    spin2=Spinbox(window,from_=0,to=5,font=("cambria",10),state="readonly")
                    spin2.place(x=700,y=285)
                    lbl8=Label(window,text="NO. OF ADULTS:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl8.place(x=100,y=280)
                    lbl9=Label(window,text="NO. OF CHILDREN:",fg="forest green",font=("Cambria",16,"bold"))
                    lbl9.place(x=500,y=280)

                    global c1
                    global c2

                    btn2=Button(window,text="EXPLORE",font=("Cambria",13),fg="blanched almond",bg="forest green",width=18,command=explore2)
                    btn2.place(x=550,y=385)

                    lbl11=Label(window,text="SELECT ROOM NO.",fg="forest green",font=("Cambria",16,"bold"))
                    lbl11.place(x=250,y=385)

                    global listbox1
                    global listbox2
                    global listbox3
                    global listbox4

                    #presidential suite
                    listbox1=Listbox(window,selectmode="multiple",font = ("cambria",10),height=7,width=16,exportselection=False)  
                    listbox1.place(x=150,y=485)
                    lbl13= Label(window, text ="PRESIDENTIAL SUITE")
                    lbl13.place(x=150,y=450)

                    #one bedroom chalet
                    listbox2=Listbox(window,selectmode="multiple",font = ("cambria",10),height=7,width=19,exportselection=False)  
                    listbox2.place(x=300,y=485)
                    lbl14= Label(window, text ="ONE BEDROOM CHALET")
                    lbl14.place(x=300,y=450)

                    #interconnecting rooms
                    listbox3=Listbox(window,selectmode="multiple",font = ("cambria",10),height=7,width=22,exportselection=False)  
                    listbox3.place(x=470,y=485)
                    lbl15 = Label(window, text ="INTERCONNECTING ROOMS")
                    lbl15.place(x=470,y=450)

                    #twin rooms
                    listbox4=Listbox(window,selectmode="multiple",font = ("cambria",10),height=7,width=11,exportselection=False)  
                    listbox4.place(x=670,y=485)
                    lbl16= Label(window, text ="TWIN ROOMS")
                    lbl16.place(x=670,y=450)


                    def roomno():
                        if cal1.get_date() and cal2.get_date() and combo1.get() and cal1.get_date()>=datetime.date.today() and cal2.get_date()>=cal1.get_date():
                            sqlCon=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                            cur=sqlCon.cursor()
                            c1=str(cal1.get_date())
                            c2=str(cal2.get_date())

                            cur.execute("SELECT ROOM_NO FROM BOOKING_DETAILS WHERE (NOT(('"+ c2 +"'<CHECKIN AND '" + c1 +"'<CHECKIN) OR ('"+ c2 + "'>CHECKOUT AND '"+c1+"'>CHECKOUT)))")
                            rooms=cur.fetchall()
                            cur.execute("SELECT ROOM_NO,NAME FROM ROOMS WHERE BRANCH='"+combo1.get()+"'")
                            ROOMS=cur.fetchall()
                            availrooms=[]
                            for i in ROOMS:
                                if (i[0],) not in tuple(rooms):
                                    availrooms.append(i)
                            for i in availrooms:
                                if i[1]=="PRESIDENTIAL SUITE":
                                    listbox1.insert(END,i[0])
                                elif i[1]=="ONE BEDROOM CHALET":
                                    listbox2.insert(END,i[0])
                                elif i[1]=="INTERCONNECTING ROOMS":
                                    listbox3.insert(END,i[0])
                                elif i[1]=="TWIN ROOM":
                                    listbox4.insert(END,i[0])

                    def Confirm():
                        if  (listbox1.curselection()!=tuple() or listbox2.curselection()!=tuple() or listbox3.curselection()!=tuple() or listbox4.curselection()!=tuple()) and spin1.get():
                            mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hotel')
                            cur=mydb.cursor()

                            bid=a
                            a1=combo1.get()
                            s=userid
                            c1=cal1.get_date()
                            c2=cal2.get_date()

                            if a1=="COORG":
                                k="H0001"
                            elif a1=="KODAIKANAL":
                                k="H0002"
                            elif a1=="MUNNAR":
                                k="H0003"
                            else:
                                print("lollipop")

                            cur.execute('SELECT NAME FROM USER_ADMIN WHERE ID="'+str(s)+'"')
                            for i in cur:
                                name=i[0]

                            selected_rooms=[]

                            for i in listbox1.curselection():
                                selected_rooms.append(listbox1.get(i))
                            for i in listbox2.curselection():
                                selected_rooms.append(listbox2.get(i))
                            for i in listbox3.curselection():
                                selected_rooms.append(listbox3.get(i))
                            for i in listbox4.curselection():
                                selected_rooms.append(listbox4.get(i))

                            for i in selected_rooms:
                                cur.execute('INSERT INTO BOOKING_DETAILS VALUES("'+a+'","'+str(s)+'","'+k+'","'+name+'","'+i+'","'+str(c1)+'","'+str(c2)+'",'+str(spin1.get())+','+str(spin2.get())+')')
                                mydb.commit()

                            mydb.close()

                            
                            def Payment():
                                def sign_out_func():
                                    window.destroy()
                                    Home_Page_Func()

                                def back():
                                    window.destroy()
                                    Book_Rooms_Func()

                                window= Tk()
                                window.geometry("1000x700")
                                window.title("PAYMENT")
                                bg = PhotoImage(file = "user images.png")
                                lbl1=Label(window,image=bg)
                                lbl1.place(x=0,y=0)

                                lbl2=Label(window,text="PAY HERE",fg="forest green",font=("Cambria",30,"bold"),width=18)
                                lbl2.place(x=300,y=70)
                                btn2=Button(window,text="BACK",font=("Cambria",16),fg="blanched almond",bg="forest green",width=8,command=back)
                                btn2.place(x=10,y=10)
                                btn5=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                                btn5.place(x=870,y=10)

                                columns = ('ROOM','NAME','CHECKIN','CHECKOUT','PRICE')
                                wth=[100,100,100,100,100]
                                db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
                                cur=db.cursor()
                                tree =ttk.Treeview(window, columns=columns, show='headings',height=10)
                                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                                    tree.place(x=255,y=160)

                                cur.execute("SELECT booking_details.ROOM_NO,rt.NAME,CHECKIN,CHECKOUT,rt.COST*datediff(CHECKOUT,CHECKIN) FROM booking_details,ROOM_TYPE rt,ROOMS WHERE ROOMS.ROOM_NO=BOOKING_DETAILS.ROOM_NO AND ROOMS.TYPE_ID=rt.TYPE_ID AND booking_details.BOOKING_ID='"+bid+"'")
                                records=cur.fetchall()
                                tot_cost=0
                                for record in records:
                                    tree.insert('',END,values=record)
                                    tot_cost+=record[4]

                                lbl3=Label(window,text="TOTAL",fg="forest green",font=("Cambria",16,"bold"),width=14)
                                lbl3.place(x=350,y=420)
                                lbl4=Label(window,fg="forest green",font=("Cambria",16,"bold"),width=12,text=str(tot_cost))
                                lbl4.place(x=550,y=420)
                                lbl3=Label(window,text="TAXES",fg="forest green",font=("Cambria",16,"bold"),width=14)
                                lbl3.place(x=350,y=470)
                                lbl6=Label(window,fg="forest green",font=("Cambria",16,"bold"),width=12,text=str(round(tot_cost*0.18,2)))
                                lbl6.place(x=550,y=470)
                                lbl3=Label(window,text="GRAND TOTAL",fg="forest green",font=("Cambria",16,"bold"),width=14)
                                lbl3.place(x=350,y=520)
                                lbl6=Label(window,fg="forest green",font=("Cambria",16,"bold"),width=12,text=str(round(tot_cost*0.18,2)+round(tot_cost,2)))
                                lbl6.place(x=550,y=520)

                                def ok():
                                    messagebox.showinfo("User", "PAYMENT DONE SUCCESSFULLY!!")

                                btn1=Button(window,text='PAY',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9, command=ok)
                                btn1.place(x=550,y=600)
                                
                                window.mainloop()
                            
                        window.destroy()
                        Payment()

                    btn = Button(window, text='OK',font=("Cambria",13),fg="blanched almond",bg="forest green",width=10,command=roomno)
                    btn.place(x=750,y=230)

                    btn3=Button(window,text="CONFIRM",font=("Cambria",13),fg="blanched almond",bg="forest green",width=18,command=Confirm)
                    btn3.place(x=550,y=630)


                    combo1.current()

                    window.mainloop()

                #####################################################################    #####################################################################
                    
                def Resort_Amenities_Func():
                    window = Tk()
                    window.title("RESORT AMENITIES")
                    window.geometry("1000x700")

                    def ExitCmd():
                         window.destroy()
                         Home_Page_Func()
                                
                    def BackCmd():
                         window.destroy()
                         User_Home_Page_Func()
                        
                    def get_price_of_service(service_id):
                        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                        cur=mydb.cursor()
                        cur.execute("select service_id, price from services where service_id='"+service_id+"'")
                        t=cur.fetchall()
                        lprice = int(t[0][1])
                        return(lprice)

                    def insert_to_services_db(booking_id, service_id, room_no, qty):
                        if (qty == 0):
                            return
                        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                        cur=mydb.cursor()
                        cur.execute("select uservice_id from user_services")
                        t=len(cur.fetchall())
                        uservice_id = "U" + str(t+1)
                        price = get_price_of_service(service_id)
                        cost = qty * price
                        try:
                           sql = "INSERT INTO user_services(uservice_id, booking_id,service_id,room_no,Qty,cost)\
                                      VALUES (%s, %s, %s, %s, %s, %s)"
                           val = (uservice_id, booking_id, service_id, room_no, qty, cost)
                           mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                           cur=mydb.cursor()
                           cur.execute(sql, val)
                           mydb.commit()

                        except Exception as e:
                           print(e)
                           mydb.rollback()
                           mydb.close()

                    def Ok():
                        if sp42.get():
                            room_no = sp42.get()
                            booking_id = value[lst.index(room_no)][0]

                            ccount = sp37.get()
                            service_id="S1004"
                            insert_to_services_db(booking_id, service_id, room_no, int(ccount))
                            
                            gcount = sp38.get()
                            service_id="S1007"
                            insert_to_services_db(booking_id, service_id, room_no, int(gcount))

                            swcount = sp39.get()
                            service_id="S1008"
                            insert_to_services_db(booking_id, service_id, room_no, int(swcount))
                            
                            scount = sp40.get()
                            service_id="S1003"
                            insert_to_services_db(booking_id, service_id, room_no, int(scount))

                            icount = sp41.get()
                            service_id="S1005"
                            insert_to_services_db(booking_id, service_id, room_no, int(icount))

                            messagebox.showinfo("User", "ORDER PLACED SUCCESSFULLY!!")

                    bg = PhotoImage(file="user images.png")
                    label1 = Label( window, image = bg)
                    label1.place(x = 0, y = 0)


                    lbl36=Label(window,fg="forest green",text="RESORT AMENITIES",font=("Cambria",36),    width=20)
                    lbl36.place(x=280,y=80)

                    btn32 = Button(window,text="BACK",bg="forest green",fg="white",font=("Cambria",16), width=8, command=BackCmd)
                    btn32.place(x=10, y= 10)

                    btn132 = Button(window,text="SIGNOUT",bg="forest green",fg="white",font=("Cambria",16), width=9, command=ExitCmd)
                    btn132.place(x=870, y= 10)

                    lbl37=Label(window,fg="forest green",text="CAR RENTAL",  font=("Cambria",16, "bold"))
                    lbl37.place(x=180,y=230)
                    sp37=Spinbox(window, from_= 0, to = 20)
                    sp37.place(x=370,y=230)

                    lbl38=Label(window,fg="forest green",text="GYMNASIUM",    font=("Cambria",16, "bold"))
                    lbl38.place(x=180,y=280)
                    sp38=Spinbox(window, from_= 0, to = 20)
                    sp38.place(x=370,y=280)

                    lbl39=Label(window,fg="forest green",text="SWIMMING POOL",    font=("Cambria",16, "bold"))
                    lbl39.place(x=180,y=330)
                    sp39=Spinbox(window, from_= 0, to = 20)
                    sp39.place(x=370,y=330)

                    lbl40=Label(window,fg="forest green",text="SPA",  font=("Cambria",16, "bold"))
                    lbl40.place(x=180,y=380)
                    sp40=Spinbox(window, from_= 0, to = 20)
                    sp40.place(x=370,y=380)

                    lbl41=Label(window,fg="forest green",text="INDOOR GAMES",  font=("Cambria",16, "bold"))
                    lbl41.place(x=180,y=430)
                    sp41=Spinbox(window, from_= 0, to = 20)
                    sp41.place(x=370,y=430)

                    lbl42=Label(window,fg="forest green",text="ROOM NO",  font=("Cambria",16, "bold"))
                    lbl42.place(x=180,y=480)

                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="hotel")
                    cur=mydb.cursor()
                    cur.execute('SELECT BOOKING_ID,ROOM_NO FROM BOOKING_DETAILS WHERE CURDATE() >= CHECKIN AND CURDATE() <= CHECKOUT AND ID="'+userid+'"')
                    value=cur.fetchall()
                    lst=[]
                    for i in value:
                        lst.append(i[1])
                    m=StringVar()
                    sp42=ttk.Combobox(window,font=('Californian FB',13),state='readonly',width=12,textvariable=m)
                    sp42['values']=lst
                    sp42.place(x=370,y=482)

                    columns = ('NAME','PRICE','UNITS')
                    wth=[160,50,113]
                    tree = ttk.Treeview(window, columns=columns, show='headings',height=10)
                    for i in range(len(columns)):
                        tree.heading(columns[i],text=columns[i])
                        tree.column(columns[i],width=wth[i])
                    tree.place(x=85,y=170)
                    cur.execute('SELECT NAME,PRICE,UNITS FROM Services WHERE SERVICE_ID in ("S1003","S1004","S1005","S1007","S1008")')
                    records=cur.fetchall()
                    for record in records:
                        tree.insert('',END,values=record)
                    tree.place(x=600,y=260)

                    btn34 = Button(window,bg="forest green",fg="white",text="CONFIRM",font=("Cambria",16), width=16, command=Ok)
                    btn34.place(x=750, y=600)

                    window.mainloop()

                window=Tk()
                window.title("USER HOME PAGE")
                window.geometry("1000x700")

                bgimage=PhotoImage(file='user images.png')
                bg=Label(window,image=bgimage)
                bg.place(x=0,y=0)

                signout=Button(window,text='SIGN OUT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=9,command=sign_out_func)
                signout.place(x=870,y=10)

                editprofile=Button(window,text='EDIT PROFILE',font=('Cambria',16),fg='blanched almond',bg='forest green',width=12,command=edit_profile_func)
                editprofile.place(x=700,y=10)

                booking_history=Button(window,text='BOOKING HISTORY',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=booking_history_func)
                booking_history.place(x=125,y=150)

                current_stay=Button(window,text='OPEN BOOKINGS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=current_stay_func)
                current_stay.place(x=540,y=150)

                book_rooms=Button(window,text='BOOK ROOMS',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27, height=2,command=book_rooms_func)
                book_rooms.place(x=350,y=340)

                room_service=Button(window,text='ROOM SERVICE',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=room_service_func)
                room_service.place(x=125,y=530)

                resort_amenities=Button(window,text='RESORT AMENITIES',font=('Cambria',16),fg='blanched almond',bg='forest green',width=27,height=2,command=resort_amenities_func)
                resort_amenities.place(x=540,y=530)

                window.mainloop()

                #####################################################################              #####################################################################
     
        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "hotel")
        cursor = db.cursor()
        query = "SELECT USERNAME,PSWD,ID FROM user_admin"
        cursor.execute(query)
        names = cursor.fetchall()
        a1=ent1.get()
        a2=ent2.get()               

        lst1=[]
        lst2=[]
        for lst in names:
            lst1.append(lst[0])
            lst2.append(lst[1])
                
        for b in range (0,len(lst1)):
            if a1==lst1[b]:
                c=b
                break
            else: c=0
            
        if (a2)==lst2[c]:
            userid=names[c][2]
            window.destroy()
            User_Home_Page_Func()
        elif a2!=lst2[c]:
            lbl3=Label(window,text="INCORRECT PASSWORD/USERNAME",fg="red",font=("Cambria",13))
            lbl3.place(x=355,y=480)

        
    btn1=Button(window,text="SIGN IN",font=("Cambria",16),fg="blanched almond",bg="forest green",width=10,command=sql)
    btn1.place(x=450,y=410)

    lbl5=Label(window,text="New here??",fg="forest green",font=("Cambria",13))
    lbl5.place(x=355,y=550)
    btn3=Button(window,text="Create an account",font=("Cambria",13),fg="blanched almond",bg="forest green",width=22,command=user_signup)
    btn3.place(x=455,y=550)
        
    window.mainloop()

######################################################################
######################################################################

def Home_Page_Func():

    def Exit_Func():
        window.destroy()

    def about_us_func():
        window.destroy()
        About_Us_Func()

    def admin_signin_func():
        window.destroy()
        Admin_Signin_Func()

    def user_signin_func():
        window.destroy()
        User_Signin_Func()

    window=Tk()
    window.title("HOME PAGE")
    window.geometry("1000x700")

    bgimage=PhotoImage(file='bg image 10.png')
    bg=Label(window,image=bgimage)
    bg.place(x=0,y=0)

    Exit=Button(window,text='EXIT',font=('Cambria',16),fg='blanched almond',bg='forest green',width=6,command=Exit_Func)
    Exit.place(x=910,y=10)

    about_us=Button(window,text='ABOUT US',font=('Cambria',16),fg='blanched almond',bg='forest green',width=10,command=about_us_func)
    about_us.place(x=765,y=10)

    admin=Button(window,text='ADMIN',font=('Cambria',16),fg='blanched almond',bg='forest green',width=15,command=admin_signin_func)
    admin.place(x=275,y=530)

    user=Button(window,text='USER',font=('Cambria',16),fg='blanched almond',bg='forest green',width=15,command=user_signin_func)
    user.place(x=540,y=530)

    window.mainloop()

######################################################################
######################################################################

Home_Page_Func()

######################################################################
##############################################################

