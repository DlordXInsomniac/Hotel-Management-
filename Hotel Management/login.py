from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from hotel import HotelManagementSystem

class Login_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Log-In")
        self.root.geometry("1530x800+0+0")
        self.root.resizable(0,0)

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\hotel1.jpg")

        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="#FFF")
        frame.place(x=610,y=180,width=350,height=450)
        
        img1 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\user.png")
        img1 = img1.resize((75,75),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.logo,bg="#FFF",borderwidth=0)
        lbl_img1.place(x=750,y=180,width=85,height=75)

        txt_lbl = Label(frame,text="Log-In",font=("times new roman",20,"bold"),fg="black",bg="#FFF")
        txt_lbl.place(x=140,y=75)

        usrname_lbl = Label(frame,text="Username",font=("times new roman",15,"bold"),bg="#FFF")
        usrname_lbl.place(x=75,y=120)
        self.usr_txt = ttk.Entry(frame,font=("times new roman",12,"normal"))
        self.usr_txt.place(x=50,y=150,width=250)

        usr_pass_lbl = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="#FFF")
        usr_pass_lbl.place(x=75,y=190)
        self.pass_txt = ttk.Entry(frame,font=("times new roman",12,"normal"))
        self.pass_txt.place(x=50,y=220,width=250)

        img2 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\username.png")
        img2 = img2.resize((25,25),Image.ANTIALIAS)
        self.logo1 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.logo1,borderwidth=0)
        lbl_img2.place(x=655,y=302,width=25,height=25)

        img3 = Image.open(r"C:\Users\lenovo\Desktop\Python\Hotel Management\images\password.png")
        img3 = img3.resize((25,25),Image.ANTIALIAS)
        self.logo2 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.logo2,borderwidth=0)
        lbl_img3.place(x=655,y=372,width=25,height=25)

        login_btn = Button(frame,text="Login",command=self.login,font=("times new roman",15,"normal"),bd=3,relief=RAISED,fg="white",bg="#0bf",activebackground="#0bf",activeforeground="white")
        login_btn.place(x=120,y=270,width=120,height=40)

        reg_btn = Button(frame,text="Register",font=("times new roman",15,"normal"),bg="white",fg="#0bf",activebackground="#0bf",activeforeground="white")
        reg_btn.place(x=120,y=320,width=120,height=40)


    def login(self):
        if self.usr_txt.get() == "" or self.pass_txt.get()=="":
            messagebox.showerror("Error","Enter all the required fields",parent=self.root)
        else:
            self.new_win = Toplevel(self.root)
            self.hotel = HotelManagementSystem(self.new_win)



if __name__  == "__main__":
    root = Tk()
    obj = Login_win(root)
    root.mainloop()