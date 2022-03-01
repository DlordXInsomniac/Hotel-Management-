#imported modules
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Customer_win:

    def __init__(self,root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1290x550+235+220")
        self.root.resizable(0,0)

        #variables
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_gen = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idno = StringVar()
        self.var_address = StringVar()
        self.var_pincode = StringVar()

        self.var_search = StringVar()
        self.var_txt_search = StringVar()

        #frame

        lbl_title = Label(self.root,text="Customer Details",font=("clarendon",12,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=25)

        #logo
        img2 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img2 = img2.resize((100,40),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=25)


        #customer_details_frame
        cust_labl_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("clarendon",12,"bold"),padx=2)
        cust_labl_frm.place(x=5,y=25,width=425,height=490)

        #custm_data_label
        #reference no
        ref_lbl = Label(cust_labl_frm,text="Reference No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        ref_lbl.grid(row=0,column=0,sticky=W)
        enty_ref = ttk.Entry(cust_labl_frm,textvariable=self.var_ref,width=22,font=("clarendon",12,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        #Name
        cname_lbl = Label(cust_labl_frm,text="Full Name :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cname_lbl.grid(row=1,column=0,sticky=W)
        enty_name = ttk.Entry(cust_labl_frm,textvariable=self.var_name,width=22,font=("clarendon",12,"bold"))
        enty_name.grid(row=1,column=1)

        #gender
        cgen_lbl = Label(cust_labl_frm,text="Gender :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cgen_lbl.grid(row=2,column=0,sticky=W)
        cb_gen = ttk.Combobox(cust_labl_frm,textvariable=self.var_gen,font=("clarendon",12,"normal"),width=20,state="readonly")
        cb_gen["value"]=("Choose","Male","Female","Others")
        cb_gen.current(0)
        cb_gen.grid(row=2,column=1)

        #Mobile
        cmob_lbl = Label(cust_labl_frm,text="Contact No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cmob_lbl.grid(row=3,column=0,sticky=W)
        enty_mob = ttk.Entry(cust_labl_frm,textvariable=self.var_contact,width=22,font=("clarendon",12,"bold"))
        enty_mob.grid(row=3,column=1)

        #email
        cmail_lbl = Label(cust_labl_frm,text="Email Id :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cmail_lbl.grid(row=4,column=0,sticky=W)
        enty_mail = ttk.Entry(cust_labl_frm,textvariable=self.var_email,width=22,font=("clarendon",12,"bold"))
        enty_mail.grid(row=4,column=1)

        #Nationality
        cnalty_lbl = Label(cust_labl_frm,text="Nationality:",font=("clarendon",12,"bold"),padx=2,pady=6)
        cnalty_lbl.grid(row=5,column=0,sticky=W)
        cb_nalty= ttk.Combobox(cust_labl_frm,textvariable=self.var_nationality,font=("clarendon",12,"normal"),width=20,state="readonly")
        cb_nalty["value"]=("Choose","Indian","American","Spanish","British")
        cb_nalty.current(0)
        cb_nalty.grid(row=5,column=1)

        #IDproof
        cidty_lbl = Label(cust_labl_frm,text="Id Proof :",font=("clarendon",12,"bold"),padx=2,pady=6)
        cidty_lbl.grid(row=6,column=0,sticky=W)
        cb_id = ttk.Combobox(cust_labl_frm,textvariable=self.var_idproof,font=("clarendon",12,"normal"),width=20,state="readonly")
        cb_id["value"]=("Choose","Passport","Driving License","PAN card","Addhar Card")
        cb_id.current(0)
        cb_id.grid(row=6,column=1)

        #idnum
        cidno_lbl = Label(cust_labl_frm,text="Id No:",font=("clarendon",12,"bold"),padx=2,pady=6)
        cidno_lbl.grid(row=7,column=0,sticky=W)
        enty_idno = ttk.Entry(cust_labl_frm,textvariable=self.var_idno,width=22,font=("clarendon",12,"bold"))
        enty_idno.grid(row=7,column=1)

        #addresss
        adds_lbl = Label(cust_labl_frm,text="Address:",font=("clarendon",12,"bold"),padx=2,pady=6)
        adds_lbl.grid(row=8,column=0,sticky=W)
        enty_adds = ttk.Entry(cust_labl_frm,textvariable=self.var_address,width=22,font=("clarendon",12,"bold"))
        enty_adds.grid(row=8,column=1)

        #PINCODE
        cpin_lbl = Label(cust_labl_frm,text="PINCODE:",font=("clarendon",12,"bold"),padx=2,pady=6)
        cpin_lbl.grid(row=9,column=0,sticky=W)
        enty_pin = ttk.Entry(cust_labl_frm,textvariable=self.var_pincode,width=22,font=("clarendon",12,"bold"))
        enty_pin.grid(row=9,column=1)

        #button_frame
        btn_frm = Frame(cust_labl_frm,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=400,width=415,height=40)

        #buttons
        btn_add = Button(btn_frm,text="Add",command=self.add_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1,pady=1)

        btn_update = Button(btn_frm,text="Update",command=self.update_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1,pady=1)

        btn_delete = Button(btn_frm,text="Delete",command=self.delete_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1,pady=1)

        btn_reset = Button(btn_frm,text="Reset",command=self.reset_btn,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1,pady=1)

        #Table frame
        table_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text="DETAILS",font=("clarendon",12,"bold"),padx=2)
        table_frm.place(x=435,y=25,width=850,height=490)

        searchby_lbl = Label(table_frm,text="Search by:",font=("clarendon",12,"bold"))
        searchby_lbl.grid(row=0,column=0,sticky=W)

        
        cb_sby= ttk.Combobox(table_frm,textvariable=self.var_search,font=("clarendon",10,"normal"),width=15,state="readonly")
        cb_sby["value"]=("Choose","Reference","Contact","Name")
        cb_sby.current(0)
        cb_sby.grid(row=0,column=1,padx=5)

        enty_sby = ttk.Entry(table_frm,width=22,textvariable=self.var_txt_search,font=("clarendon",10,"bold"))
        enty_sby.grid(row=0,column=2,padx=5)

        btn_search = Button(table_frm,text="Search",command=self.search,font=("clarendon",10,"bold"),bg="black",fg="gold",width=8)
        btn_search.grid(row=0,column=3,padx=5)

        btn_srch_rst = Button(table_frm,text="Reset",command=self.reset_search,font=("clarendon",10,"bold"),bg="black",fg="gold",width=8)
        btn_srch_rst.grid(row=0,column=4,padx=5)

        #data table
        data_table = Frame(table_frm,bd=2,relief=RIDGE)
        data_table.place(x=0,y=50,width=800,height=350)

        #scrollbar
        scroll_x = ttk.Scrollbar(data_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table,orient=VERTICAL)

        self.cust_detail_table = ttk.Treeview(data_table,column=("Reference","Name","Gender","Contact","Email","Nationality","Idproof","Idno","Address","Pincode"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)

        self.cust_detail_table.heading("Reference",text="Reference No")
        self.cust_detail_table.heading("Name",text="Name")
        self.cust_detail_table.heading("Gender",text="Gender")
        self.cust_detail_table.heading("Contact",text="Contact No")
        self.cust_detail_table.heading("Email",text="E-Mail Id")
        self.cust_detail_table.heading("Nationality",text="Nationality")
        self.cust_detail_table.heading("Idproof",text="ID Proof")
        self.cust_detail_table.heading("Idno",text="ID-No")
        self.cust_detail_table.heading("Address",text="Address")
        self.cust_detail_table.heading("Pincode",text="Pincode")

        self.cust_detail_table["show"]="headings"

        self.cust_detail_table.column("Reference",width=100)
        self.cust_detail_table.column("Name",width=150)
        self.cust_detail_table.column("Gender",width=100)
        self.cust_detail_table.column("Contact",width=100)
        self.cust_detail_table.column("Email",width=150)
        self.cust_detail_table.column("Nationality",width=100)
        self.cust_detail_table.column("Idproof",width=100)
        self.cust_detail_table.column("Idno",width=100)
        self.cust_detail_table.column("Address",width=100)
        self.cust_detail_table.column("Pincode",width=100)

        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_name.get()=="":
            messagebox.showerror("Warning","Fill all the Required Fields",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_ref.get(),
                                self.var_name.get(),
                                self.var_gen.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_nationality.get(),
                                self.var_idproof.get(),
                                self.var_idno.get(),
                                self.var_address.get(),
                                self.var_pincode.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Data has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong: {str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_data(self,event=""):
        cur_row = self.cust_detail_table.focus()
        content = self.cust_detail_table.item(cur_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gen.set(row[2]),
        self.var_contact.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_idproof.set(row[6]),
        self.var_idno.set(row[7]),
        self.var_address.set(row[8]),
        self.var_pincode.set(row[9])

    def update_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact no",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Gender=%s,Contact=%s,Email=%s,Nationality=%s,Idproof=%s,Idno=%s,Address=%s,Pincode=%s where Reference=%s",( 
                                self.var_name.get(),
                                self.var_gen.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_nationality.get(),
                                self.var_idproof.get(),
                                self.var_idno.get(),
                                self.var_address.get(),
                                self.var_pincode.get(),
                                self.var_ref.get()
            ))
            conn.commit()
            self.reset_data()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Data has been updated",parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("System","Do you want to delete the data ?",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            query = "delete from customer where Reference=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()

    def reset_data(self):
        self.var_name.set(""),
        self.var_gen.set("Choose"),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_nationality.set("Choose"),
        self.var_idproof.set("Choose"),
        self.var_idno.set(""),
        self.var_address.set(""),
        self.var_pincode.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

    def reset_btn(self):
        self.var_name.set(""),
        self.var_gen.set("Choose"),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_nationality.set("Choose"),
        self.var_idproof.set("Choose"),
        self.var_idno.set(""),
        self.var_address.set(""),
        self.var_pincode.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("",END,values=i)
            conn.commit()
        else:
            messagebox.showinfo("System "," NO DATA FOUND ",parent=self.root)
            self.reset_search()
        conn.close()

    def reset_search(self):
        self.var_search.set("Choose"),
        self.var_txt_search.set("")

        self.fetch_data()

if __name__  == "__main__":
    root = Tk()
    obj = Customer_win(root)
    root.mainloop()