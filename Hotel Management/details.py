from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Details_win: 

    def __init__(self,root):
        self.root = root
        self.root.title("ROOM MANAGEMENT")
        self.root.geometry("1290x550+235+220")
        self.root.resizable(0,0)


        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()
        self.var_status = StringVar()

        #window title
        lbl_title = Label(self.root,text="Room Management",font=("clarendon",12,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=25)

        #logo
        img2 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img2 = img2.resize((100,40),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=25)

        details_labl_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text=" ROOM DETAILS",font=("clarendon",12,"bold"),padx=2)
        details_labl_frm.place(x=5,y=30,width=550,height=350)

        #custm_data_label
        #customer refernce
        floor_lbl = Label(details_labl_frm,text="Floor :",font=("clarendon",12,"bold"),padx=2,pady=6)
        floor_lbl.grid(row=0,column=0,sticky=W,padx=5)
        enty_floor = ttk.Entry(details_labl_frm,textvariable=self.var_floor,width=22,font=("clarendon",10,"normal"))
        enty_floor.grid(row=0,column=1,sticky=W,padx=5)

        #room_no 
        room_no_lbl = Label(details_labl_frm,text="Room No :",font=("clarendon",12,"bold"),padx=2,pady=6)
        room_no_lbl.grid(row=1,column=0,sticky=W,padx=5)
        enty_room_no = ttk.Entry(details_labl_frm,textvariable=self.var_roomno,width=22,font=("clarendon",10,"normal"))
        enty_room_no.grid(row=1,column=1,padx=5)

        #Room type 
        room_type_lbl = Label(details_labl_frm,text="Room Type:",font=("clarendon",12,"bold"),padx=2,pady=6)
        room_type_lbl.grid(row=2,column=0,sticky=W,padx=5)
        cb_rt= ttk.Combobox(details_labl_frm,textvariable=self.var_roomtype,font=("clarendon",10,"normal"),width=20,state="readonly")
        cb_rt["value"]=("Choose","Single","Double","Luxury","Prime")
        cb_rt.current(0)
        cb_rt.grid(row=2,column=1)

        #status 
        room_type_lbl = Label(details_labl_frm,text="Status:",font=("clarendon",12,"bold"),padx=2,pady=6)
        room_type_lbl.grid(row=3,column=0,sticky=W,padx=5)
        cb_rs= ttk.Combobox(details_labl_frm,textvariable=self.var_status,font=("clarendon",10,"normal"),width=20,state="readonly")
        cb_rs["value"]=("Choose","Vacant","Occupied")
        cb_rs.current(0)
        cb_rs.grid(row=3,column=1)

        #button_frame
        btn_frm = Frame(details_labl_frm,bd=2,relief=RIDGE)
        btn_frm.place(x=10,y=250,width=415,height=40)

        #buttons
        btn_add = Button(btn_frm,text="Add",command=self.add_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1,pady=1)

        btn_update = Button(btn_frm,text="Update",command=self.update_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1,pady=1)

        btn_delete = Button(btn_frm,text="Delete",command=self.delete_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_delete.grid(row=0,column=2,padx=1,pady=1)

        btn_reset = Button(btn_frm,text="Reset",command=self.reset_data,font=("clarendon",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1,pady=1)


        # Data Table frame
        table_frm = LabelFrame(self.root,bd=2,relief=RIDGE,text="MANAGEMENT",font=("clarendon",12,"bold"),padx=2)
        table_frm.place(x=600,y=30,width=650,height=350)

        #scrollbar
        scroll_x = ttk.Scrollbar(table_frm,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frm,orient=VERTICAL)

        self.manage_detail_table = ttk.Treeview(table_frm,column=("Floor","RoomNo","RoomType","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.manage_detail_table.xview)
        scroll_y.config(command=self.manage_detail_table.yview)

        self.manage_detail_table.heading("Floor",text="Floor No")
        self.manage_detail_table.heading("RoomNo",text="Room No")
        self.manage_detail_table.heading("RoomType",text="Room Type")
        self.manage_detail_table.heading("Status",text="Room Status")

        self.manage_detail_table["show"]="headings"

        self.manage_detail_table.column("Floor",width=100)
        self.manage_detail_table.column("RoomNo",width=100)
        self.manage_detail_table.column("RoomType",width=100)
        self.manage_detail_table.column("Status",width=100)
        
        self.manage_detail_table.pack(fill=BOTH,expand=1)
        self.manage_detail_table.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_data()

    #ADD BUTTON
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get()=="":
            messagebox.showerror("Warning","Fill all the Required Fields",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s)",(
                                self.var_floor.get(),
                                self.var_roomno.get(),
                                self.var_roomtype.get(),
                                self.var_status.get()            
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
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.manage_detail_table.delete(*self.manage_detail_table.get_children())
            for i in rows:
                self.manage_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Reset all the fields
    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("Choose"),
        self.var_status.set("Choose")

    #show data from database
    def get_data(self,event=""):
        cur_row = self.manage_detail_table.focus()
        content = self.manage_detail_table.item(cur_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2]),
        self.var_status.set(row[3])

    #Update button
    def update_data(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error","Please enter Room no",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="797816",database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s,Status=%s where RoomNo=%s",(
                                self.var_floor.get(),
                                self.var_roomtype.get(),
                                self.var_status.get(),
                                self.var_roomno.get()
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
            query = "delete from details where RoomNo=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()


if __name__  == "__main__":
    root = Tk()
    obj = Details_win(root)
    root.mainloop()