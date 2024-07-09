from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime

class Details_room:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1020x500+248+140")

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
        label_frame_left = LabelFrame(self.root, text="New Room Add", padx=2, font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE,)
        label_frame_left.place(x= 2, y=50, width=365, height=310)

        # Floor
        floor = Label(label_frame_left, text="Floor", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(label_frame_left, textvariable=self.var_floor, width=8, font=("TkDefaultFont", 10, "bold"),)
        entry_floor.grid(row=0, column=1, sticky=W)
        
        # Room No
        room_no = Label(label_frame_left, text="Room No", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        room_no.grid(row=1, column=0, sticky=W)

        self.var_room_no = StringVar()
        entry_room_no = ttk.Entry(label_frame_left, textvariable= self.var_room_no, width=8, font=("TkDefaultFont", 10, "bold"),)
        entry_room_no.grid(row=1, column=1, sticky=W)
        
        # Room Type
        room_type = Label(label_frame_left, text="Room Type", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        room_type.grid(row=2, column=0, sticky=W)

        self.var_room_type = StringVar()
        entry_room_type = ttk.Entry(label_frame_left, textvariable=self.var_room_type, width=8, font=("TkDefaultFont", 10, "bold"),)
        entry_room_type.grid(row=2, column=1, sticky=W)

        # =================== buttons ===================
        button_frame = Frame(label_frame_left, bd=2, relief=RIDGE,)
        button_frame.place(x=0, y=180)

        button_add = Button(button_frame, text="Add", command=self.add_data, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_add.grid(row=0, column=0,)

        button_update = Button(button_frame, text="Update", command= self.update, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_update.grid(row=0, column=1, padx=1)

        button_delete = Button(button_frame, text="Delete", command= self.mDelete, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_delete.grid(row=0, column=2, padx=1)

        button_reset = Button(button_frame, text="Reset", command= self.reset, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_reset.grid(row=0, column=3, padx=1)

        # =================== table frame ===================
        table_frame = LabelFrame(self.root, text="Show Room Details", font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE)
        table_frame.place(x=425, y=50, width=450, height=310)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, column=("Floor", "RoomNo", "RoomType",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomNo", text="Room No")

        self.room_table["show"]="headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("RoomType", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()== "" or self.var_room_type.get()== "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values (%s, %s, %s)", (
                                self.var_floor.get(),
                                self.var_room_no.get(),
                                self.var_room_type.get(),
                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from details")
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

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2]),

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter floor number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET Floor =%s, RoomType=%s WHERE RoomNo =%s",
                              (
                                self.var_floor.get(),
                                self.var_room_type.get(),
                                self.var_room_no.get(),
                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)

    
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="User123", password = "user123", database="management")
            my_cursor = conn.cursor()
            query = "DELETE FROM details WHERE RoomNo =%s"
            value = (self.var_room_no.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def reset(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set(""),
        




if __name__ == "__main__":
    root = Tk()
    obj = Details_room(root)
    root.mainloop()