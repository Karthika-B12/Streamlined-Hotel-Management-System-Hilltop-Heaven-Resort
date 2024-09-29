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
                            
