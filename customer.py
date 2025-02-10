from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+230+220")

        #======================= variables===========
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        # =======================title==================

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 10, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1290, height=50)

        # ====================logo=============

        img2 = Image.open("logo.jpg")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bg="black", relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)


        #=============labelframe=========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 10,"bold"),padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)


        #================label and entry==============
        # customer reference
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, width=39, textvariable=self.var_ref, font=("times new roman", 10, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # cust name
        cname = Label(labelframeleft, text="Customer name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        c_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_cust_name, font=("times new roman", 10, "bold"))
        c_entry.grid(row=1, column=1)

        # mother name
        mother_name = Label(labelframeleft, text="Mother name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        mother_name.grid(row=2, column=0, sticky=W)
        mother_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_mother, font=("times new roman", 10, "bold"))
        mother_entry.grid(row=2, column=1)

        # gender combobox
        gender_label = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        gender_label.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("times new roman", 10, "bold"), width=37, state="readonly")
        combo_gender["value"] = ("male", "female", "other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # post code
        mother_name = Label(labelframeleft, text="Post code:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        mother_name.grid(row=4, column=0, sticky=W)
        post_entry = Entry(labelframeleft, width=39, textvariable=self.var_post, font=("times new roman", 10, "bold"))
        post_entry.grid(row=4, column=1)

        # mobile number
        mobile_name = Label(labelframeleft, text="Mobile number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        mobile_name.grid(row=5, column=0, sticky=W)
        mobile_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_mobile, font=("times new roman", 10, "bold"))
        mobile_entry.grid(row=5, column=1)

        # email
        email_name = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        email_name.grid(row=6, column=0, sticky=W)
        email_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_email, font=("times new roman", 10, "bold"))
        email_entry.grid(row=6, column=1)

        # nationality
        nationality_label = Label(labelframeleft, text="Nationality:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        nationality_label.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("times new roman", 10, "bold"), width=37, state="readonly")
        combo_nationality["value"] = ("Indian", "Foreigner")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # id proof type combobox
        id_proof = Label(labelframeleft, text="Id proof type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        id_proof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("times new roman", 10, "bold"), width=37, state="readonly")
        combo_id["value"] = ("AadharCard", "Driving Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # id number
        id_name = Label(labelframeleft, text="ID number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        id_name.grid(row=9, column=0, sticky=W)
        id_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_id_number, font=("times new roman", 10, "bold"))
        id_entry.grid(row=9, column=1)

        # address
        address_name = Label(labelframeleft, text="Address:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        address_name.grid(row=10, column=0, sticky=W)
        address_entry = ttk.Entry(labelframeleft, width=39, textvariable=self.var_address, font=("times new roman", 10, "bold"))
        address_entry.grid(row=10, column=1)

        # ==================buttons=================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnadd = Button(btn_frame, text="Add", command=self.add_data, font=("times new roman", 15, "bold"), bg="black", fg="gold", width=8)
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 14, "bold"), bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="Delete", command=self.Delete,font=("times new roman", 14, "bold"), bg="black", fg="gold", width=8)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 15, "bold"), bg="black", fg="gold", width=8)
        btnreset.grid(row=0, column=3, padx=1)


        # =============table frame==============
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblsearchby = Label(table_frame, font=("arial", 12, "bold"), text="search By:", bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()
        textsearch = ttk.Entry(table_frame,textvariable=self.txt_search, font=("arial", 12, "bold"), width=24)
        textsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, text="Search",command=self.search, font=("times new roman", 14, "bold"), bg="black", fg="gold", width=8)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(table_frame, text="Show All",command=self.fetch_data, font=("times new roman", 14, "bold"), bg="black", fg="gold", width=8)
        btnshowall.grid(row=0, column=4, padx=1)

        # =====================show data table===============

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(details_table, columns=("ref","name", "mother", "gender", "post", "mobile",
                                                                       "email","nationality","idproof","idnumber","address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref", text="Refer No")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="PostCode")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "all fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "customer details has been added", parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong:{str(es)}", parent=self.root)



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])



    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent = self.root)
        else:

            conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set name = %s, mother=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s , address=%s where ref=%s",(

                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get(),

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "customer details has been upadated successfully", parent=self.root)


    def Delete(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "frist enter the mobile number to delete", parent=self.root)
        else:

            Delete = messagebox.askyesno("Hotel Management System", "do you want to delete this customer", parent=self.root)
            if Delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123",
                                               database="management")
                my_cursor = conn.cursor()
                query = "delete from customer where ref=%s"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)

            else:
                if not Delete:
                    return

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()


    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
        my_cursor = conn.cursor()

        # Correctly formatted query using parameterized query
        query = "SELECT * FROM customer WHERE " + self.search_var.get() + " LIKE %s"
        value = ("%" + self.txt_search.get() + "%",)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
