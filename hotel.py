from tkinter import *
from PIL import Image, ImageTk 
from customer import Custom_Window
from room import Roombooking

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open("C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\hotel.jpg")
        img1 = img1.resize((1700, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimg = Label(self.root, image = self.photoimg1, bd = 4, relief = RIDGE)
        labelimg.place(x = 250, y = 0, width= 1700, height= 200)

        # ================= logo =====================
        img2 = Image.open("C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\hotel_logo.jpg")
        img2 = img2.resize((250, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimg = Label(self.root, image = self.photoimg2, bd = 4, relief = RIDGE)
        labelimg.place(x = 0, y = 0, width= 250, height= 200)

        # ================= title =====================
        label_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", justify="center", font=("TkDefaultFont", 40, "bold"), bg= "dark blue", fg="white", bd=4, relief=RIDGE,)
        label_title.place(x=0, y=200, width=1400, height=50)

        # ================= main frame =====================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y= 250, width=1400, height=620)

        # ================= menu =====================
        label_menu = Label(main_frame, text="MENU", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "dark blue", fg="white", bd=4, relief=RIDGE,)
        label_menu.place(x=0, y=0, width=250,)

        # =================button frame=====================
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y= 35, width=250, height=190)

        customer_btn = Button(button_frame, text="CUSTOMER", command=self.custom_details, justify="center", width=20, font=("TkDefaultFont", 14, "bold"), bg= "dark blue", fg="white", bd=0, cursor="hand2")
        customer_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(button_frame, text="ROOM", command=self.roombooking, justify="center", width=20, font=("TkDefaultFont", 14, "bold"), bg= "dark blue", fg="white", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(button_frame, text="DETAILS", justify="center", width=20, font=("TkDefaultFont", 14, "bold"), bg= "dark blue", fg="white", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(button_frame, text="REPORT", justify="center", width=20, font=("TkDefaultFont", 14, "bold"), bg= "dark blue", fg="white", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(button_frame, text="LOGOUT", justify="center", width=20, font=("TkDefaultFont", 14, "bold"), bg= "dark blue", fg="white", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

    
    def custom_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Custom_Window(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()