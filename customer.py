from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random

class Custom_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1020x500+248+140")
        

        # ================= variables =====================
        self.variable_ref = StringVar()
        x = random.randint(1000, 9999)
        self.variable_ref.set(str(x))

        self.variable_customer_name = StringVar()
        self.variable_mother_name = StringVar()
        self.variable_gender = StringVar()
        self.variable_postcode = StringVar()
        self.variable_mobile = StringVar()
        self.variable_email = StringVar()
        self.variable_nationality = StringVar()
        self.variable_idproof = StringVar()
        self.variable_idnumber = StringVar()
        self.variable_address = StringVar()

        # ================= title =====================
        label_title = Label(self.root, text="ADD CUSTOMER DETAILS", justify="center", font=("TkDefaultFont", 20, "bold"), bg= "dark blue", fg="white", bd=4, relief=RIDGE,)
        label_title.place(x=0, y=0, width=1020, height=50)

        # ================= logo =====================
        img2 = Image.open(r"C:\\Users\\Nazife\\Desktop\\hotel_management_system\\images\\hotel_logo.jpg")
        img2 = img2.resize((105, 45))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        labelimg.place(x = 2, y = 2, width= 105, height= 45)

        # ================= labelFrame =====================
        label_frame_left = LabelFrame(self.root, text="Customer Details", padx=2, font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE,)
        label_frame_left.place(x= 2, y=50, width=250, height=450)

        # ================= labels and entries =====================
        # Customer REF
        label_customer_ref = Label(label_frame_left, text="Customer ID", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        label_customer_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(label_frame_left, textvariable=self.variable_ref, width=10, font=("TkDefaultFont", 10, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer Name
        customer_name = Label(label_frame_left, text="Customer Name", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        customer_name.grid(row=1, column=0, sticky=W)

        entry_customer_name = ttk.Entry(label_frame_left, textvariable=self.variable_customer_name, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_customer_name.grid(row=1, column=1)

        # Mother Name
        mother_name = Label(label_frame_left, text="Mother Name", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        mother_name.grid(row=2, column=0, sticky=W)

        entry_mother_name = ttk.Entry(label_frame_left, textvariable=self.variable_mother_name, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_mother_name.grid(row=2, column=1)

        # Gender Dropdown
        gender = Label(label_frame_left, text="Gender", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(label_frame_left, textvariable=self.variable_gender, font=("TkDefaultFont", 10, "bold"), width=8, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)



        # Postcode
        postcode = Label(label_frame_left, text="Postcode", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        postcode.grid(row=4, column=0, sticky=W)

        entry_postcode = ttk.Entry(label_frame_left, textvariable=self.variable_postcode, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_postcode.grid(row=4, column=1)

        # Mobile Number
        mobile = Label(label_frame_left, text="Mobile", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        mobile.grid(row=5, column=0, sticky=W)

        entry_mobile = ttk.Entry(label_frame_left, textvariable=self.variable_mobile, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_mobile.grid(row=5, column=1)

        # email 
        email = Label(label_frame_left, text="Email", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry(label_frame_left, textvariable=self.variable_email, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_email.grid(row=6, column=1)

        # Nationality
        nationality = Label(label_frame_left, text="Nationality", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        nationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(label_frame_left, textvariable=self.variable_nationality, font=("TkDefaultFont", 10, "bold"), width=8, state="readonly")
        combo_nationality["value"] = ('Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean')
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # idproof type dropdown
        id_proof = Label(label_frame_left, text="ID Proof Type", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        id_proof.grid(row=8, column=0, sticky=W)

        combo_id_proof = ttk.Combobox(label_frame_left, textvariable=self.variable_idproof, font=("TkDefaultFont", 10, "bold"), width=8, state="readonly")
        combo_id_proof["value"] = ("Identity Card", "Passport", "Driving Licence")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=8, column=1)

        # id number
        id_number = Label(label_frame_left, text="ID Number", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        id_number.grid(row=9, column=0, sticky=W)

        entry_id_number = ttk.Entry(label_frame_left, textvariable=self.variable_idnumber, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_id_number.grid(row=9, column=1)

        # Adress
        adress = Label(label_frame_left, text="Address", font=("TkDefaultFont", 10, "bold"), padx=2, pady=6)
        adress.grid(row=10, column=0, sticky=W)

        entry_adress = ttk.Entry(label_frame_left, textvariable=self.variable_address, width=10, font=("TkDefaultFont", 10, "bold"))
        entry_adress.grid(row=10, column=1)

        # =================== buttons ===================
        button_frame = Frame(label_frame_left, bd=2, relief=RIDGE,)
        button_frame.place(x=0, y=370)

        button_add = Button(button_frame, text="Add", command=self.add_data, font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_add.grid(row=0, column=0,)

        button_update = Button(button_frame, text="Update", font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_update.grid(row=0, column=1, padx=1)

        button_delete = Button(button_frame, text="Delete", font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_delete.grid(row=0, column=2, padx=1)

        button_reset = Button(button_frame, text="Reset", font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=6)
        button_reset.grid(row=0, column=3, padx=1)

        # =================== table frame ===================
        table_frame = LabelFrame(self.root, text="View Details and Search System", font=("TkDefaultFont", 10, "bold"), bd=4, relief=RIDGE)
        table_frame.place(x=255, y=50, width=770, height=450)

        searchby = Label(table_frame, text="Search By", font=("TkDefaultFont", 10, "bold"), bg="red", fg="white")
        searchby.grid(row=0, column=0, sticky=W, padx=2)
        combo_id_search = ttk.Combobox(table_frame, font=("TkDefaultFont", 10, "bold"), width=14, state="readonly")
        combo_id_search["value"] = ("Mobile", "Ref",)
        combo_id_search.current(0)
        combo_id_search.grid(row=0, column=1, padx=2)

        search = ttk.Entry(table_frame, width=14, font=("TkDefaultFont", 10, "bold"))
        search.grid(row=0, column=2, padx=2)

        button_search = Button(table_frame, text="Search", font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=7)
        button_search.grid(row=0, column=3, padx=2)

        button_showall = Button(table_frame, text="Show All", font=("TkDefaultFont", 10, "bold"), bg= "dark blue", fg="white", width=7)
        button_showall.grid(row=0, column=4, padx=2)

        # =================== show data table ===================
        details_table = Frame(table_frame, bd=2, relief=RIDGE,)
        details_table.place(x=0, y=50, width=770, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.customer_details_table = ttk.Treeview(details_table, column=("Ref", "Name", "Mother", "Gender", "Postcode", "Mobile", "Email", "Nationality", "IdProof", "IdNumber", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_details_table.xview)
        scroll_y.config(command=self.customer_details_table.yview)

        self.customer_details_table.heading("Ref", text="Refer No")
        self.customer_details_table.heading("Name", text="Name")
        self.customer_details_table.heading("Mother", text="Mother")
        self.customer_details_table.heading("Gender", text="Gender")
        self.customer_details_table.heading("Postcode", text="Postcode")
        self.customer_details_table.heading("Mobile", text="Mobile")
        self.customer_details_table.heading("Email", text="Email")
        self.customer_details_table.heading("Nationality", text="Nationality")
        self.customer_details_table.heading("IdProof", text="Id Proof")
        self.customer_details_table.heading("IdNumber", text="Id Number")
        self.customer_details_table.heading("Address", text="Address")

        self.customer_details_table["show"]="headings"

        self.customer_details_table.column("Ref", width=100)
        self.customer_details_table.column("Name", width=100)
        self.customer_details_table.column("Mother", width=100)
        self.customer_details_table.column("Gender", width=100)
        self.customer_details_table.column("Postcode", width=100)
        self.customer_details_table.column("Mobile", width=100)
        self.customer_details_table.column("Email", width=100)
        self.customer_details_table.column("Nationality", width=100)
        self.customer_details_table.column("IdProof", width=100)
        self.customer_details_table.column("IdNumber", width=100)
        self.customer_details_table.column("Address", width=100)

        self.customer_details_table.pack(fill=BOTH, expand=1)
    

    def add_data(self):
        if self.variable_mobile.get()== "" or self.variable_mother_name.get()== "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password = "Nazi2008", database="management")
                my_cursor = conn.cursor()
            
                my_cursor.execute("insert into customer values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                self.variable_ref.get(),
                                self.variable_customer_name.get(),
                                self.variable_mother_name.get(),
                                self.variable_gender.get(),
                                self.variable_postcode.get(),
                                self.variable_mobile.get(),
                                self.variable_email.get(),
                                self.variable_nationality.get(),
                                self.variable_idproof.get(),
                                self.variable_idnumber.get(),
                                self.variable_address.get(),
                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Custom_Window(root)
    root.mainloop()