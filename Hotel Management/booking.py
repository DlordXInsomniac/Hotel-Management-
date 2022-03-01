#imported modules
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Booking_win: 

    def __init__(self,root):
        self.root = root
        self.root.title("Booking Details")
        self.root.geometry("1290x550+235+220")
        self.root.resizable(0,0)

        #variables
        self.var_ref = StringVar()
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_duration = StringVar()
        self.var_food = StringVar()
        self.var_subtotal = StringVar()
        self.var_tax = StringVar()
        self.var_discount = StringVar()
        self.var_total_cost = StringVar()
        self.var_search = StringVar()
        self.var_txt_search = StringVar()

        #window title
        lbl_title = Label(self.root,text="Room Booking Details",font=("clarendon",12,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=25)

        #logo
        img2 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img2 = img2.resize((100,40),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=25)

        #customer_details_frame
        booking_labl_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text=" BOOKING DETAILS",font=("clarendon",12,"bold"),padx=2)
        booking_labl_frm.place(x=5,y=25,width=425,height=490)

        #custm_data_label
        #customer refernce
        cus_ref_lbl = Label(booking_labl_frm,text="Reference No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cus_ref_lbl.grid(row=0,column=0,sticky=W)
        enty_cus_ref = ttk.Entry(booking_labl_frm,width=20,textvariable=self.var_ref,font=("clarendon",10,"normal"))
        enty_cus_ref.grid(row=0,column=1,sticky=W)

        #check button
        btn_chk = Button(booking_labl_frm,text="Check",command=self.fetch_custm_details,font=("clarendon",8,"bold"),bg="black",fg="gold",width=8)
        btn_chk.grid(row=0,column=3,padx=1,pady=1)

        #contact no
        contact_lbl = Label(booking_labl_frm,text="Contact No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        contact_lbl.grid(row=1,column=0,sticky=W)
        enty_contact = ttk.Entry(booking_labl_frm,textvariable=self.var_contact,width=22,font=("clarendon",10,"normal"))
        enty_contact.grid(row=1,column=1)

        #check in 
        chech_in_lbl = Label(booking_labl_frm,text="Check-in Date :",font=("clarendon",12,"bold"),padx=2,pady=6)
        chech_in_lbl.grid(row=2,column=0,sticky=W)
        enty_chech_in = ttk.Entry(booking_labl_frm,textvariable=self.var_checkin,width=22,font=("clarendon",10,"normal"))
        enty_chech_in.grid(row=2,column=1)

        #check out
        check_out_lbl = Label(booking_labl_frm,text="Check-out Date :",font=("clarendon",12,"bold"),padx=2,pady=6)
        check_out_lbl.grid(row=3,column=0,sticky=W)
        enty_check_out = ttk.Entry(booking_labl_frm,textvariable=self.var_checkout,width=22,font=("clarendon",10,"normal"))
        enty_check_out.grid(row=3,column=1)

        #room type
        roomtype_lbl = Label(booking_labl_frm,text="Room Type:",font=("clarendon",12,"bold"),padx=2,pady=6)
        roomtype_lbl.grid(row=4,column=0,sticky=W)
        cb_rt= ttk.Combobox(booking_labl_frm,textvariable=self.var_roomtype,font=("clarendon",10,"normal"),width=20,state="readonly")
        cb_rt["value"]=("Choose","Single","Double","Luxury","Prime")
        cb_rt.current(0)
        cb_rt.grid(row=4,column=1)

        #Room no
        roomno_lbl = Label(booking_labl_frm,text="Room No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        roomno_lbl.grid(row=5,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details where Status ='Vacant'")
        rows = my_cursor.fetchall()

        cb_rn= ttk.Combobox(booking_labl_frm,textvariable=self.var_roomno,font=("clarendon",10,"normal"),width=20,state="readonly")
        cb_rn["value"]=rows
        cb_rn.current(0)
        cb_rn.grid(row=5,column=1)

        #Fooding
        food_lbl = Label(booking_labl_frm,text="Food Service :",font=("clarendon",12,"bold"),padx=2,pady=6)
        food_lbl.grid(row=6,column=0,sticky=W)
        cb_rt= ttk.Combobox(booking_labl_frm,textvariable=self.var_food,font=("clarendon",10,"normal"),width=20,state="readonly")
        cb_rt["value"]=("Choose","Yes","No")
        cb_rt.current(0)
        cb_rt.grid(row=6,column=1)

        #Duration
        duration_lbl = Label(booking_labl_frm,text="Duration :",font=("clarendon",12,"bold"),padx=2,pady=6)
        duration_lbl.grid(row=7,column=0,sticky=W)
        enty_duration = ttk.Entry(booking_labl_frm,textvariable=self.var_duration,width=22,font=("clarendon",10,"normal"),state="readonly")
        enty_duration.grid(row=7,column=1)

        #Sub Total
        contact_lbl = Label(booking_labl_frm,text="Sub-Total :",font=("clarendon",12,"bold"),padx=2,pady=6)
        contact_lbl.grid(row=8,column=0,sticky=W)
        enty_contact = ttk.Entry(booking_labl_frm,width=22,textvariable=self.var_subtotal,font=("clarendon",10,"normal"),state="readonly")
        enty_contact.grid(row=8,column=1)

        #Tax
        contact_lbl = Label(booking_labl_frm,text="Tax :",font=("clarendon",12,"bold"),padx=2,pady=6)
        contact_lbl.grid(row=9,column=0,sticky=W)
        enty_contact = ttk.Entry(booking_labl_frm,textvariable=self.var_tax,width=22,font=("clarendon",10,"normal"),state="readonly")
        enty_contact.grid(row=9,column=1)
        
        #Discount
        discount_lbl = Label(booking_labl_frm,text="Discount :",font=("clarendon",12,"bold"),padx=2,pady=6)
        discount_lbl.grid(row=10,column=0,sticky=W)
        enty_discount = ttk.Entry(booking_labl_frm,textvariable=self.var_discount,width=22,font=("clarendon",10,"normal"),state="readonly")
        enty_discount.grid(row=10,column=1)

        #Total Cost
        total_cost_lbl = Label(booking_labl_frm,text="Total Cost :",font=("clarendon",12,"bold"),padx=2,pady=6)
        total_cost_lbl.grid(row=11,column=0,sticky=W)
        enty_total_cost = ttk.Entry(booking_labl_frm,textvariable=self.var_total_cost,width=22,font=("clarendon",10,"normal"),state="readonly")
        enty_total_cost.grid(row=11,column=1)

        #Bill 
        btn_bill = Button(booking_labl_frm,command=self.total,text="Bill",font=("clarendon",10,"bold"),bg="black",fg="gold",width=9)
        btn_bill.grid(row=11,column=3,padx=5)


        #button_frame
        btn_frm = Frame(booking_labl_frm,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=425,width=415,height=40)

        #buttons
        btn_add = Button(btn_frm,text="Add",command=self.add_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1,pady=1)

        btn_update = Button(btn_frm,text="Update",command=self.update_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1,pady=1)

        btn_delete = Button(btn_frm,text="Delete",command=self.delete_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1,pady=1)

        btn_reset = Button(btn_frm,text="Reset",command=self.reset_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1,pady=1)

        #image
        img3 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img3 = img3.resize((350,200),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=900,y=40,width=350,height=200)

        # Data Table frame
        table_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text="DETAILS",font=("clarendon",12,"bold"),padx=2)
        table_frm.place(x=435,y=255,width=850,height=260)

        searchby_lbl = Label(table_frm,text="Search by:",font=("clarendon",12,"bold"))
        searchby_lbl.grid(row=0,column=0,sticky=W)

        
        cb_sby= ttk.Combobox(table_frm,textvariable=self.var_search,font=("clarendon",10,"normal"),width=15,state="readonly")
        cb_sby["value"]=("Choose","Reference","Contact","roomno")
        cb_sby.current(0)
        cb_sby.grid(row=0,column=1,padx=5)

        enty_sby = ttk.Entry(table_frm,textvariable=self.var_txt_search,width=22,font=("clarendon",10,"bold"))
        enty_sby.grid(row=0,column=2,padx=5)

        btn_search = Button(table_frm,text="Search",command=self.search,font=("clarendon",10,"bold"),bg="black",fg="gold",width=8)
        btn_search.grid(row=0,column=3,padx=5)

        btn_srch_rst = Button(table_frm,text="Reset",command=self.reset_search,font=("clarendon",10,"bold"),bg="black",fg="gold",width=8)
        btn_srch_rst.grid(row=0,column=4,padx=5)

        #data table
        data_table = Frame(table_frm,bd=2,relief=RIDGE)
        data_table.place(x=0,y=50,width=800,height=180)

        #scrollbar
        scroll_x = ttk.Scrollbar(data_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table,orient=VERTICAL)

        self.room_detail_table = ttk.Treeview(data_table,column=("Reference","Contact","checkin","checkout","roomtype","roomno","Duration","Foodservice"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_detail_table.xview)
        scroll_y.config(command=self.room_detail_table.yview)

        self.room_detail_table.heading("Reference",text="Reference No")
        self.room_detail_table.heading("Contact",text="Contact No")
        self.room_detail_table.heading("checkin",text="Check-In Date")
        self.room_detail_table.heading("checkout",text="Check-Out Date")
        self.room_detail_table.heading("roomtype",text="Room Type")
        self.room_detail_table.heading("roomno",text="Room-No")
        self.room_detail_table.heading("Duration",text="Duration")
        self.room_detail_table.heading("Foodservice",text="Food Service")

        self.room_detail_table["show"]="headings"

        self.room_detail_table.column("Reference",width=100)
        self.room_detail_table.column("Contact",width=100)
        self.room_detail_table.column("checkin",width=150)
        self.room_detail_table.column("checkout",width=100)
        self.room_detail_table.column("roomtype",width=100)
        self.room_detail_table.column("roomno",width=100)
        self.room_detail_table.column("Duration",width=100)
        self.room_detail_table.column("Foodservice",width=100)

        self.room_detail_table.pack(fill=BOTH,expand=1)
        self.room_detail_table.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_data()

    #ADD BUTTON
    def add_data(self):
        if self.var_contact.get() == "" or self.var_ref.get()=="":
            messagebox.showerror("Warning","Fill all the Required Fields",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_ref.get(),
                                self.var_contact.get(),
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomno.get(),
                                self.var_duration.get(),
                                self.var_food.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Data has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong: {str(es)}",parent=self.root)

    #Fetching room data from database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_detail_table.delete(*self.room_detail_table.get_children())
            for i in rows:
                self.room_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #show data from database
    def get_data(self,event=""):
        cur_row = self.room_detail_table.focus()
        content = self.room_detail_table.item(cur_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_contact.set(row[1]),
        self.var_checkin.set(row[2]),
        self.var_checkout.set(row[3]),
        self.var_roomtype.set(row[4]),
        self.var_roomno.set(row[5]),
        self.var_duration.set(row[6]),
        self.var_food.set(row[7])

    #Update button
    def update_data(self):
        if self.var_ref.get() == "":
            messagebox.showerror("Error","Please enter Reference no",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set Contact=%s,checkin=%s,checkout=%s,roomtype=%s,roomno=%s,Duration=%s,Foodservice=%s where Reference=%s",(
                                self.var_contact.get(),
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomno.get(),
                                self.var_duration.get(),
                                self.var_food.get(),
                                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Data has been updated",parent=self.root)

    #Delete Button
    def delete_data(self):
        delete = messagebox.askyesno("System","Do you want to delete the data ?",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            query = "delete from room where Reference=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()

    #Reset all the fields
    def reset_data(self):
        self.var_ref.set(""),
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set("Choose"),
        self.var_roomno.set(""),
        self.var_duration.set(""),
        self.var_food.set("Choose"),
        self.var_subtotal.set(""),
        self.var_tax.set(""),
        self.var_discount.set(""),
        self.var_total_cost.set("")

    #Fetching Customer data from database
    def fetch_custm_details(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please Provide Reference No !",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Reference=%s")
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Reference no Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                #frame to show details
                shwdtafrm = Frame(self.root,bd=4,relief=RIDGE,padx=2)
                shwdtafrm.place(x=450,y=40,width=300,height=200)

                #Name
                name_label = Label(shwdtafrm,text="Name :",font=("clarendon",10,"bold"))
                name_label.grid(row=0,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=row,font=("clarendon",10,"bold"))
                lbl.grid(row=0,column=1,padx=2)

                #gender
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Reference=%s")
                value = (self.var_ref.get(),)
                my_cursor.execute(query,value)
                data = my_cursor.fetchone()

                gen_label = Label(shwdtafrm,text="Gender :",font=("clarendon",10,"bold"))
                gen_label.grid(row=1,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=data,font=("clarendon",10,"bold"))
                lbl.grid(row=1,column=1,padx=2)

                #contact
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                query = ("select Contact from customer where Reference=%s")
                value = (self.var_ref.get(),)
                my_cursor.execute(query,value)
                data1 = my_cursor.fetchone()

                contact_label = Label(shwdtafrm,text="Contact :",font=("clarendon",10,"bold"))
                contact_label.grid(row=2,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=data1,font=("clarendon",10,"bold"))
                lbl.grid(row=2,column=1,padx=2)

                #email
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Reference=%s")
                value = (self.var_ref.get(),)
                my_cursor.execute(query,value)
                data2 = my_cursor.fetchone()

                contact_label = Label(shwdtafrm,text="E-Mail ID :",font=("clarendon",10,"bold"))
                contact_label.grid(row=3,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=data2,font=("clarendon",10,"bold"))
                lbl.grid(row=3,column=1,padx=2)

                #Nationality
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Reference=%s")
                value = (self.var_ref.get(),)
                my_cursor.execute(query,value)
                data3 = my_cursor.fetchone()

                nationality_label = Label(shwdtafrm,text="Nationality :",font=("clarendon",10,"bold"))
                nationality_label.grid(row=4,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=data3,font=("clarendon",10,"bold"))
                lbl.grid(row=4,column=1,padx=2)

                #Address
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Reference=%s")
                value = (self.var_ref.get(),)
                my_cursor.execute(query,value)
                data4 = my_cursor.fetchone()

                address_label = Label(shwdtafrm,text="Address :",font=("clarendon",10,"bold"))
                address_label.grid(row=5,column=0,padx=5,sticky=W)

                lbl = Label(shwdtafrm,text=data4,font=("clarendon",10,"bold"))
                lbl.grid(row=5,column=1,padx=2)

    #search system
    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_detail_table.delete(*self.room_detail_table.get_children())
            for i in rows:
                self.room_detail_table.insert("",END,values=i)
            conn.commit()
        else:
            messagebox.showinfo("System "," NO DATA FOUND ",parent=self.root)
            self.reset_search()
        conn.close()

    #reset search panel
    def reset_search(self):
        self.var_search.set("Choose"),
        self.var_txt_search.set("")

        self.fetch_data()

    #Calculate cost
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()

        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")

        self.var_duration.set(abs(outDate-inDate).days)

       # calculate total price
        food = float(250)
        single = float(350)
        doble = float(500)
        luxury = float(750)
        prime = float(1000)
        fd = self.var_food.get()
        nd = self.var_duration.get()
        rt = self.var_roomtype.get()
        duration = float(nd)
            
        if duration < 28 :
            dis_price = 10
        elif duration >= 28 and duration <60:
            dis_price = 20
        else:
            dis_price = 30


        if fd == "Yes":
            if rt == "Single":
                tax1 = 0.3
                st_cost = float((food + single)*duration)
                taxed_price = float(st_cost * tax1)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            elif rt == "Double":
                tax2 = 0.5
                st_cost = float((food + doble)*duration)
                taxed_price = float(st_cost * tax2)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            elif rt == "Luxury":
                tax3 = 0.3
                st_cost = float((food + luxury)*duration)
                taxed_price = float(st_cost * tax3)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            else:
                tax4 = 0.8
                st_cost = float((food + prime)*duration)
                taxed_price = float(st_cost * tax4)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

        else:
            if rt == "Single":
                tax1 = 0.3
                st_cost = float(single*duration)
                taxed_price = float(st_cost * tax1)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            elif rt == "Double":
                tax2 = 0.5
                st_cost = float(doble *duration)
                taxed_price = float(st_cost * tax2)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            elif rt == "Luxury":
                tax3 = 0.3
                st_cost = float(luxury * duration)
                taxed_price = float(st_cost * tax3)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

            else:
                tax4 = 0.8
                st_cost = float(prime * duration)
                taxed_price = float(st_cost * tax4)
                disd = float((st_cost * dis_price )/100 )
                tt_cost = float((st_cost + taxed_price) - disd)

                self.var_subtotal.set(st_cost)
                self.var_tax.set(taxed_price)
                self.var_discount.set(f"{dis_price} %")
                self.var_total_cost.set(tt_cost)

if __name__  == "__main__":
    root = Tk()
    obj = Booking_win(root)
    root.mainloop()