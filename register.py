from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random, os
from time import strftime
from datetime import datetime

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1550x800+0+0")

        # ========= variables ========
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_question = StringVar()
        self.var_security_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirm_pass = StringVar()

        
        # base_path = os.path.dirname(__file__)
        # image_path = os.path.join(base_path, "images", "register.jpeg")
        # path_list = list()
        # for item in image_path:
        #     path_list.append(item)
        #     if item == "\\":
        #         path_list.append("\\")
        # image_path = "".join(path_list)   
        # print(image_path)

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images", "register.jpeg")
        image_path = image_path.replace("\\", "\\\\")
        self.bg = ImageTk.PhotoImage(file= fr"{image_path}")

        labelbg = Label(self.root, image = self.bg)
        labelbg.place(x = 0, y = 0, relwidth= 1, relheight=1)

        registerframe = Frame(self.root, bg = "white")
        registerframe.place(x = 250, y=100, width=800, height=450)

        label_title = Label(registerframe, text="Sign Up Here", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "white", fg="black",)
        label_title.place(x=45, y=30)


        # ----------first row -----------
        first_name = Label(registerframe, text="First Name", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        first_name.place(x=40, y=100 )

        self.txtuser = ttk.Entry(registerframe, textvariable=self.var_first_name, font=("TkDefaultFont", 10, "bold"))
        self.txtuser.place(x = 40, y=127, width=270)

        last_name = Label(registerframe, text="Last Name", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        last_name.place(x=400, y=100 )

        self.last_name = ttk.Entry(registerframe, textvariable=self.var_last_name, font=("TkDefaultFont", 10, "bold"))
        self.last_name.place(x = 400, y=127, width=270)

        #-------------second row ------------
        contact = Label(registerframe, text="Contact No", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        contact.place(x=40, y=170 )

        self.contact = ttk.Entry(registerframe, textvariable=self.var_contact, font=("TkDefaultFont", 10, "bold"))
        self.contact.place(x = 40, y=197, width=270)

        email = Label(registerframe, text="Email", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        email.place(x=400, y=170 )

        self.email = ttk.Entry(registerframe, textvariable=self.var_email, font=("TkDefaultFont", 10, "bold"))
        self.email.place(x = 400, y=197, width=270)

        #-------------third row ------------
        security_question = Label(registerframe, text="Select Security Question", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        security_question.place(x=40, y=240 )

        questions = ("Select", "Birth Place", "Girl/boyfriend Name", "First Pet Name")
        combo_security_questions = ttk.Combobox(registerframe, textvariable=self.var_security_question, font=("TkDefaultFont", 10, "bold"), state="readonly")
        combo_security_questions["value"] = questions
        combo_security_questions.current(0)
        combo_security_questions.place(x=40, y=267, width=270)

        security_answer = Label(registerframe, text="Answer", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        security_answer.place(x=400, y=240 )

        self.security_answer = ttk.Entry(registerframe, textvariable=self.var_security_answer, font=("TkDefaultFont", 10, "bold"))
        self.security_answer.place(x = 400, y=267, width=270)

        #-------------forth row ------------
        password = Label(registerframe, text="Password", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        password.place(x=40, y=310 )

        self.password = ttk.Entry(registerframe, textvariable=self.var_password, font=("TkDefaultFont", 10, "bold"))
        self.password.place(x = 40, y=337, width=270)

        confirm_pass = Label(registerframe, text="Confirm Password", font=("TkDefaultFont", 12, "bold"), bg= "white", fg="black")
        confirm_pass.place(x=400, y=310 )

        self.confirm_pass = ttk.Entry(registerframe, textvariable=self.var_confirm_pass, font=("TkDefaultFont", 10, "bold"))
        self.confirm_pass.place(x = 400, y=337, width=270)

        # check box
        self.var_checkbox = IntVar()
        checkbox = Checkbutton(registerframe, variable=self.var_checkbox, text="I Agree The Terms & Conditions", font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black", onvalue=1, offvalue=0)
        checkbox.place(x = 40, y=364)

        # buttons

        registerbtn = Button(registerframe, command= self.register_data, text="Register",font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black")
        registerbtn.place(x = 40, y=391 )


        text = Label(registerframe, text="or have an account please", font=("TkDefaultFont", 9, "bold"), bg= "white", fg="blue") 
        text.place(x = 100, y=393)

        loginbtn = Button(registerframe, text="Login",font=("TkDefaultFont", 8, "bold"), bg= "white", fg="black")
        loginbtn.place(x = 257, y=391 )

    def register_data(self):
        if self.var_first_name.get() == "" or self.var_email.get() == "" or self.var_security_question.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get() != self.var_confirm_pass.get():
            messagebox.showerror("Error", "Password & confirm password must be same")
        elif self.var_checkbox.get() == 0:
            messagebox.showerror("Error", "Please agree our terms & conditions")
        else:
            messagebox.showinfo("Success", "Welcome friends")


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()