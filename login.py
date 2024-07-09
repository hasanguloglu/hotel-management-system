from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random, os
from time import strftime
from datetime import datetime

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images", "loginbg.jpg")
        image_path = image_path.replace("\\", "\\\\")
        self.bg = ImageTk.PhotoImage(file= fr"{image_path}")

        labelbg = Label(self.root, image = self.bg)
        labelbg.place(x = 0, y = 0, relwidth= 1, relheight=1)

        loginframe = Frame(self.root, bg = "white")
        loginframe.place(x = 450, y=100, width=340, height=450)


        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images", "userimg.jpg")
        image_path = image_path.replace("\\", "\\\\")

        img1 = Image.open(fr"{image_path}")
        img1 = img1.resize((100, 100),)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimg1 = Label(self.root, image = self.photoimg1, bg = "black", borderwidth=0)
        labelimg1.place(x = 570, y = 105, width= 100, height= 100)

        label_title = Label(loginframe, text="Get Started", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "white", fg="black",)
        label_title.place(x=95, y=110)

        username = Label(loginframe, text="Username", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        username.place(x=40, y=170 )

        self.txtuser = ttk.Entry(loginframe, font=("TkDefaultFont", 10, "bold"))
        self.txtuser.place(x = 40, y=197, width=270)

        password = Label(loginframe, text="Password", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        password.place(x=40, y=227 )

        self.txtpassword = ttk.Entry(loginframe, font=("TkDefaultFont", 10, "bold"))
        self.txtpassword.place(x = 40, y=254, width=270)

        # buttons

        button_login = Button(loginframe, text="Login", justify="center", font=("TkDefaultFont", 10, "bold"), bd=3, bg= "dark blue", fg="white", width=6, relief=RIDGE)
        button_login.place(x=40, y= 300, width=120, height=35, )

        button_signup = Button(loginframe, text="Sign Up", justify="center", font=("TkDefaultFont", 10, "bold"), bd=3, bg= "dark blue", fg="white", width=6, relief=RIDGE)
        button_signup.place(x=180, y= 300, width=120, height=35, )

        button_forget = Button(loginframe, text="Forgot Password", justify="center", font=("TkDefaultFont", 8, "bold"), borderwidth=0,  fg="black", bg="white", width=6, activebackground= "white", activeforeground="black")
        button_forget.place(x=30, y= 340, width=120,)

    def login(self):
        if self.txtuser()== "" or self.txtpassword()== "":
            messagebox.showerror("Error", "All fields are required")
        



if __name__ == "__main__":
    root = Tk()
    obj = login_window(root)
    root.mainloop()