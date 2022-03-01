#imported modules
from tkinter import *
from PIL import Image, ImageTk
from custm import Customer_win
from booking import Booking_win
from details import Details_win

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #cover image
        img1 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\hotel1.jpg")
        img1 = img1.resize((1550,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=150)

        #logo
        img2 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img2 = img2.resize((150,150),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=150,height=150)

        #title
        lbl_title = Label(self.root,text="Hotel Management System",font=("clarendon",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1550,height=30)

        #frame
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1550,height=620)

        #menu
        menu_frame = Label(main_frame,text="MENU",font=("clarendon",25,"bold"),bd=4,relief=RIDGE)
        menu_frame.place(x=0,y=0,width=230)

        #buttons
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=45,width=230,height=210)  

        btn1 = Button(btn_frame,text="Customer",command=self.custm_details,width=18,font=("clarendon",15,"bold"),bd=0,bg="black",fg="gold",cursor="hand2")
        btn1.grid(row=0,column=0,pady=1)

        btn2 = Button(btn_frame,text="Bookings",command=self.booking_details,width=18,font=("clarendon",15,"bold"),bd=0,bg="black",fg="gold",cursor="hand2")
        btn2.grid(row=1,column=0,pady=1)

        btn3 = Button(btn_frame,text="Management",command=self.mangage_details,width=18,font=("clarendon",15,"bold"),bd=0,bg="black",fg="gold",cursor="hand2")
        btn3.grid(row=2,column=0,pady=1)

        btn4 = Button(btn_frame,text="Report",width=18,font=("clarendon",15,"bold"),bd=0,bg="black",fg="gold",cursor="hand2")
        btn4.grid(row=3,column=0,pady=1)

        btn5 = Button(btn_frame,text="Logout",command=self.logout,width=18,font=("clarendon",15,"bold"),bd=0,bg="black",fg="gold",cursor="hand2")
        btn5.grid(row=4,column=0,pady=1)


        img3 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)


        img4 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img4 = img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=250,width=230,height=210)

        img5 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\logo.png")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame,image=self.logo,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=430,width=230,height=210)

    #Customer Window
    def custm_details(self):
        self.new_win = Toplevel(self.root)
        self.cust = Customer_win(self.new_win)

    #Booking Window
    def booking_details(self):
        self.new_win = Toplevel(self.root)
        self.cust = Booking_win(self.new_win)

    #Management Window
    def mangage_details(self):
        self.new_win = Toplevel(self.root)
        self.cust = Details_win(self.new_win)

    #logout
    def logout(self):
        self.root.destroy()


if __name__  == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()