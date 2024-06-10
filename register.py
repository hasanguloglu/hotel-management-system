from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file= r"C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\register.jpeg")
        labelbg = Label(self.root, image = self.bg)
        labelbg.place(x = 0, y = 0, relwidth= 1, relheight=1)

        registerframe = Frame(self.root, bg = "white")
        registerframe.place(x = 250, y=100, width=800, height=450)

        label_title = Label(registerframe, text="Sign Up Here", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "white", fg="black",)
        label_title.place(x=45, y=30)


        # ----------first row -----------
        first_name = Label(registerframe, text="First Name", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        first_name.place(x=40, y=100 )

        self.txtuser = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.txtuser.place(x = 40, y=127, width=270)

        last_name = Label(registerframe, text="Last Name", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        last_name.place(x=400, y=100 )

        self.last_name = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.last_name.place(x = 400, y=127, width=270)

        #-------------second row ------------
        contact = Label(registerframe, text="Contact No", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        contact.place(x=40, y=170 )

        self.contact = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.contact.place(x = 40, y=197, width=270)

        email = Label(registerframe, text="Email", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        email.place(x=400, y=170 )

        self.email = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.email.place(x = 400, y=197, width=270)

        #-------------third row ------------
        security_question = Label(registerframe, text="Select Security Question", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        security_question.place(x=40, y=240 )

        questions = ("Select", "Birth Place", "Girl/boyfriend Name", "First Pet Name")
        combo_security_questions = ttk.Combobox(registerframe, font=("TkDefaultFont", 10, "bold"), state="readonly")
        combo_security_questions["value"] = questions
        combo_security_questions.current(0)
        combo_security_questions.place(x=40, y=267, width=270)

        security_answer = Label(registerframe, text="Answer", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        security_answer.place(x=400, y=240 )

        self.security_answer = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.security_answer.place(x = 400, y=267, width=270)

        #-------------forth row ------------
        password = Label(registerframe, text="Password", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        password.place(x=40, y=310 )

        self.password = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.password.place(x = 40, y=337, width=270)

        confirm_pass = Label(registerframe, text="Confirm Password", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        confirm_pass.place(x=400, y=310 )

        self.confirm_pass = ttk.Entry(registerframe, font=("TkDefaultFont", 10, "bold"))
        self.confirm_pass.place(x = 400, y=337, width=270)

        # check box
        checkbox = Checkbutton(registerframe, text="I Agree The Terms & Conditions", font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black")
        checkbox.place(x = 40, y=364)

        # buttons

        registerbtn = Button(registerframe, text="Register",font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black")
        registerbtn.place(x = 40, y=391 )


        text = Label(registerframe, text="or have an account please", font=("TkDefaultFont", 9, "bold"), bg= "white", fg="blue") 
        text.place(x = 100, y=393)

        loginbtn = Button(registerframe, text="Login",font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black")
        loginbtn.place(x = 257, y=391 )


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()