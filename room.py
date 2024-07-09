from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1020x500+248+140")

        # ================= variables =====================
        self.var_Contact = StringVar()
        self.var_Checkin = StringVar()
        self.var_Checkout = StringVar()
        self.var_Roomtype = StringVar()
        self.var_Roomavailable = StringVar()
        self.var_Meal = StringVar()
        self.var_Noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        # ================= title =====================
        label_title = Label(self.root, text="ROOMBOOKING DETAILS", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "dark blue", fg="white", bd=4, relief=RIDGE,)
        label_title.place(x=0, y=0, width=1020, height=50)

        # ================= logo =====================
        img2 = Image.open(r"C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\hotel_logo.jpg")
        img2 = img2.resize((105, 45))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        labelimg.place(x = 2, y = 2, width= 105, height= 45)

        # ================= labelFrame =====================
        label_frame_left = LabelFrame(self.root, text="Roombooking Details", padx=2, font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE,)
        label_frame_left.place(x= 2, y=50, width=250, height=450)

        # ================= labelFrame =====================
        label_frame_left = LabelFrame(self.root, text="Customer Details", padx=2, font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE,)
        label_frame_left.place(x= 2, y=50, width=250, height=450)

        # ================= labels and entries =====================
        # Customer Contact
        label_customer_contact = Label(label_frame_left, text="Customer Contact", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        label_customer_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(label_frame_left, textvariable=self.var_Contact, width=8, font=("TkDefaultFont", 10, "bold"),)
        entry_contact.grid(row=0, column=1, sticky=W)

        # fetch data button
        button_fetch_data = Button(label_frame_left, command=self.fetch_contact, text="Fetch", font=("TkDefaultFont", 9, "bold"), bg= "dark blue", fg="white", width=6)
        button_fetch_data.place(x=190, y=4)

        # Checkin Date
        check_in_date = Label(label_frame_left, text="Check-in Date", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(label_frame_left, textvariable=self.var_Checkin, width=10, font=("TkDefaultFont", 10, "bold"))
        txtcheck_in_date.grid(row=1, column=1)
    
        # Checkout Date
        check_out_date = Label(label_frame_left, text="Check-out Date", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)

        check_out_date = ttk.Entry(label_frame_left, textvariable=self.var_Checkout, width=10, font=("TkDefaultFont", 10, "bold"))
        check_out_date.grid(row=2, column=1)

        # Room Type
        room_type = Label(label_frame_left, text="Room Type", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        room_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password = "user123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select RoomType from details")
        types = my_cursor.fetchall()

        combo_room_type = ttk.Combobox(label_frame_left, textvariable=self.var_Roomtype, font=("TkDefaultFont", 10, "bold"), width=8, state="readonly")
        combo_room_type["value"] = types
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        # Avail Room
        available_room = Label(label_frame_left, text="Available Room", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        available_room.grid(row=4, column=0, sticky=W)

        # available_room = ttk.Entry(label_frame_left, textvariable=self.var_Roomavailable, width=10, font=("TkDefaultFont", 10, "bold"))
        # available_room.grid(row=4, column=1)


        conn = mysql.connector.connect(host="localhost", username="root", password = "user123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(label_frame_left, textvariable=self.var_Roomavailable, font=("TkDefaultFont", 10, "bold"), width=8, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        meal = Label(label_frame_left, text="Meal", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        meal.grid(row=5, column=0, sticky=W)

        meal = ttk.Entry(label_frame_left, textvariable=self.var_Meal, width=10, font=("TkDefaultFont", 10, "bold"))
        meal.grid(row=5, column=1)

        # number of days 
        No_of_days = Label(label_frame_left, text="Number of days", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        No_of_days.grid(row=6, column=0, sticky=W)

        No_of_days = ttk.Entry(label_frame_left, textvariable=self.var_Noofdays, width=10, font=("TkDefaultFont", 10, "bold"))
        No_of_days.grid(row=6, column=1)

        # Paid Tax
        paid_tax = Label(label_frame_left, text="Paid Tax", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        paid_tax.grid(row=7, column=0, sticky=W)

        paid_tax = ttk.Entry(label_frame_left, textvariable=self.var_paidtax, width=10, font=("TkDefaultFont", 10, "bold"))
        paid_tax.grid(row=7, column=1)

        # Sub Total 
        sub_total = Label(label_frame_left, text="Sub Total", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        sub_total.grid(row=8, column=0, sticky=W)

        sub_total = ttk.Entry(label_frame_left, textvariable=self.var_subtotal, width=10, font=("TkDefaultFont", 10, "bold"))
        sub_total.grid(row=8, column=1)

        # Total Cost 
        total_cost = Label(label_frame_left, text="Total Cost", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        total_cost.grid(row=9, column=0, sticky=W)

        total_cost = ttk.Entry(label_frame_left, textvariable=self.var_total, width=10, font=("TkDefaultFont", 10, "bold"))
        total_cost.grid(row=9, column=1)

        # =================== Bill buttons ===================
        button_bill = Button(label_frame_left, text="Bill", command=self.total, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_bill.grid(row=10, column=0, padx=1, sticky=W)

        # =================== buttons ===================
        button_frame = Frame(label_frame_left, bd=2, relief=RIDGE,)
        button_frame.place(x=0, y=370)

        button_add = Button(button_frame, text="Add", command=self.add_data, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_add.grid(row=0, column=0,)

        button_update = Button(button_frame, text="Update", command=self.update, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_update.grid(row=0, column=1, padx=1)

        button_delete = Button(button_frame, text="Delete", command=self.mDelete, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_delete.grid(row=0, column=2, padx=1)

        button_reset = Button(button_frame, text="Reset", command=self.reset, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_reset.grid(row=0, column=3, padx=1)

        # =================== rightside image ===================
        img3 = Image.open(r"C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\room1.jpg")
        img3 = img3.resize((420, 200))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelimg = Label(self.root, image = self.photoimg3, bd = 0, relief = RIDGE)
        labelimg.place(x = 586, y = 55, width= 420, height= 200)

        # =================== table frame ===================
        table_frame = LabelFrame(self.root, text="View Details and Search System", font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE)
        table_frame.place(x=255, y=280, width=770, height=220)

        searchby = Label(table_frame, text="Search By", font=("TkDefaultFont", 10, "bold"), bg="red", fg="white")
        searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_id_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("TkDefaultFont", 10, "bold"), width=14, state="readonly")
        combo_id_search["value"] = ("Contact", "Roomavailable",)
        combo_id_search.current(0)
        combo_id_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        search = ttk.Entry(table_frame, textvariable=self.txt_search, width=14, font=("TkDefaultFont", 10, "bold"))
        search.grid(row=0, column=2, padx=2)

        button_search = Button(table_frame, text="Search", command= self.search, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=7)
        button_search.grid(row=0, column=3, padx=2)

        button_showall = Button(table_frame, text="Show All", command= self.fetch_data, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=7)
        button_showall.grid(row=0, column=4, padx=2)

        # =================== show data table ===================
        details_table = Frame(table_frame, bd=2, relief=RIDGE,)
        details_table.place(x=0, y=50, width=770, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("Contact", "Checkin", "Checkout", "Roomtype", "Roomavailable", "Meal", "Noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Checkin", text="Check-in Date")
        self.room_table.heading("Checkout", text="Check-out Date")
        self.room_table.heading("Roomtype", text="Room Type")
        self.room_table.heading("Roomavailable", text="Room No")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("Noofdays", text="Number of days")

        self.room_table["show"]="headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("Checkin", width=100)
        self.room_table.column("Checkout", width=100)
        self.room_table.column("Roomtype", width=100)
        self.room_table.column("Roomavailable", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("Noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Contact.get()== "" or self.var_Checkin.get()== "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values (%s, %s, %s, %s, %s, %s, %s)", (
                                self.var_Contact.get(),
                                self.var_Checkin.get(),
                                self.var_Checkout.get(),
                                self.var_Roomtype.get(),
                                self.var_Roomavailable.get(),
                                self.var_Meal.get(),
                                self.var_Noofdays.get()
                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room is booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for item in rows:
                self.room_table.insert("", END, values= item)
            conn.commit()
        conn.close()

    
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']

        self.var_Contact.set(row[0]),
        self.var_Checkin.set(row[1]),
        self.var_Checkout.set(row[2]),
        self.var_Roomtype.set(row[3]),
        self.var_Roomavailable.set(row[4]),
        self.var_Meal.set(row[5]),
        self.var_Noofdays.set(row[6]),
    
    def update(self):
        if self.var_Contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET Checkin =%s, Checkout =%s, Roomtype=%s, Roomavailable =%s, Meal =%s, Noofdays =%s WHERE Contact=%s",
                              (
                                self.var_Checkin.get(),
                                self.var_Checkout.get(),
                                self.var_Roomtype.get(),
                                self.var_Roomavailable.get(),
                                self.var_Meal.get(),
                                self.var_Noofdays.get(),
                                self.var_Contact.get(),
                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)

    
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE Contact =%s"
            value = (self.var_Contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):
        self.var_Contact.set(""),
        self.var_Checkin.set(""),
        self.var_Checkout.set(""),
        self.var_Roomtype.set(""),
        self.var_Roomavailable.set(""),
        self.var_Meal.set(""),
        self.var_Noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_subtotal.set(""),
        self.var_total.set(""),

        
    
    # =================== All data fetch ===================

    def fetch_contact(self):
        if self.var_Contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
            my_cursor = conn.cursor()
            query = ("SELECT Name FROM customer WHERE Mobile=%s")
            value = (self.var_Contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number is not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x = 260, y = 55, width=300, height= 180)

                lblName = Label(showDataframe, text="Name:", font=("TkDefaultFont", 10, "bold"),)
                lblName.place(x=0,y=0)

                lbl = Label(showDataframe, text=row,font=("TkDefaultFont", 10, "bold"),)
                lbl.place(x=90, y=0)

                # =================== Gender ===================

                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                query = ("SELECT Gender FROM customer WHERE Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("TkDefaultFont", 10, "bold"),)
                lblGender.place(x=0,y=30)

                lbl2 = Label(showDataframe, text=row,font=("TkDefaultFont", 10, "bold"),)
                lbl2.place(x=90, y=30)

                # =================== Email ===================
                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM customer WHERE Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email:", font=("TkDefaultFont", 10, "bold"),)
                lblemail.place(x=0,y=60)

                lbl3 = Label(showDataframe, text=row,font=("TkDefaultFont", 10, "bold"),)
                lbl3.place(x=90, y=60)

                # =================== Nationality ===================

                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                query = ("SELECT Nationality FROM customer WHERE Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnationality = Label(showDataframe, text="Nationality:", font=("TkDefaultFont", 10, "bold"),)
                lblnationality.place(x=0,y=90)

                lbl4 = Label(showDataframe, text=row,font=("TkDefaultFont", 10, "bold"),)
                lbl4.place(x=90, y=90)

                # =================== Adress ===================

                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                query = ("SELECT Address FROM customer WHERE Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address:", font=("TkDefaultFont", 10, "bold"),)
                lbladdress.place(x=0,y=120)

                lbl5 = Label(showDataframe, text=row,font=("TkDefaultFont", 10, "bold"),)
                lbl5.place(x=90, y=120)

    # search system

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for item in rows:
                self.room_table.insert("", END, values= item)
            conn.commit()
        conn.close()    


    def total(self):
        inDate = self.var_Checkin.get()
        outDate = self.var_Checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_Noofdays.set(abs(outDate - inDate).days)

        if (self.var_Meal.get() == "Breakfast" and self.var_Roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_Noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f"%((q5)*0.09))
            subtotal = "Rs." + str("%.2f"%((q5)))
            total = "Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(subtotal)
            self.var_total.set(total)

        elif (self.var_Meal.get() == "Lunch" and self.var_Roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_Noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            tax = "Rs." + str("%.2f"%((q5)*0.09))
            subtotal = "Rs." + str("%.2f"%((q5)))
            total = "Rs." + str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(subtotal)
            self.var_total.set(total)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()