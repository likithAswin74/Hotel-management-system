from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+230+220")

        # ============variables=================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


        # =======================title==================

        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 10, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1290, height=50)

        # ====================logo=============

        img2 = Image.open("logo.jpg")
        img2 = img2.resize((100, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bg="black", relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)

        #=============labelframe=========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("times new roman", 10,"bold"),padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ================label and entry==============
        # customer contact
        lbl_cust_contacts = Label(labelframeleft, text="Customer Contact:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contacts.grid(row=0, column=0, sticky=W)

        entry_contacts = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=28, font=("times new roman", 10, "bold"))
        entry_contacts.grid(row=0, column=1, sticky=W)

        # =========================fetch data button ====================

        btnfetch = Button(labelframeleft, command=self.fetch_contact,text="fetch data", font=("times new roman", 10, "bold"), bg="black", fg="gold", width=9)
        btnfetch.place(x=340, y=3)

        # check in date
        check_in_date = Label(labelframeleft, text="check_in Date:", font=("times new roman", 12, "bold"),
                                  padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin,width=39, font=("times new roman", 10, "bold"))
        txtcheck_in_date.grid(row=1, column=1)

        # check out date
        lbl_check_out = Label(labelframeleft, text="Check_out Date:", font=("times new roman", 12, "bold"),
                                  padx=2, pady=6)
        lbl_check_out.grid(row=2, column=0, sticky=W)

        txt_check_out = ttk.Entry(labelframeleft,textvariable=self.var_checkout, width=39, font=("times new roman", 10, "bold"))
        txt_check_out.grid(row=2, column=1)

        # Room type
        label_RoomType = Label(labelframeleft, text="Room Type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)
        combo_Room = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("times new roman", 10, "bold"),
                                    width=37, state="readonly")
        combo_Room["value"] = ("single", "double", "laxary")
        combo_Room.current(0)
        combo_Room.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable = Entry(labelframeleft,textvariable=self.var_roomavailable, width=39, font=("times new roman", 10, "bold"))
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(labelframeleft, text="Meal:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        txtmeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=39,
                                 font=("times new roman", 10, "bold"))
        txtmeal.grid(row=5, column=1)

        # no of days
        lblnofodays = Label(labelframeleft, text="No of Days:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblnofodays.grid(row=6, column=0, sticky=W)
        txtnoofdays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=39,
                                font=("times new roman", 10, "bold"))
        txtnoofdays.grid(row=6, column=1)

        # paid tax
        paid_tax = Label(labelframeleft, text="Paid Tax:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        paid_tax.grid(row=7, column=0, sticky=W)
        txtpaidtax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=39,
                             font=("times new roman", 10, "bold"))
        txtpaidtax.grid(row=7, column=1)

        # subtotal
        subtotal = Label(labelframeleft, text="Sub Total:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        subtotal.grid(row=8, column=0, sticky=W)
        txtsubtotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=39,
                                  font=("times new roman", 10, "bold"))
        txtsubtotal.grid(row=8, column=1)

        # total cost
        totalcost = Label(labelframeleft, text="Total Cost:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        totalcost.grid(row=9, column=0, sticky=W)
        txttotalcost = ttk.Entry(labelframeleft, textvariable=self.var_total,width=39,
                                  font=("times new roman", 10, "bold"))
        txttotalcost.grid(row=9, column=1)

        # =============bill button ==============
        btnbill = Button(labelframeleft, text="Bill",command=self.total, font=("times new roman", 15, "bold"), bg="black",
                        fg="gold", width=8)
        btnbill.grid(row=11, column=0, padx=1,sticky=W)

        # ==================buttons=================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnadd = Button(btn_frame, text="Add",command=self.add_data, font=("times new roman", 15, "bold"), bg="black",
                        fg="gold", width=8)
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 14, "bold"),
                           bg="black", fg="gold", width=8)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="Delete", command=self.Delete, font=("times new roman", 14, "bold"),
                           bg="black", fg="gold", width=8)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 15, "bold"), bg="black",
                          fg="gold", width=8)
        btnreset.grid(row=0, column=3, padx=1)


        # ====================== right side image ==============

        img3 = Image.open("logo.jpg")
        img3 = img2.resize((520, 300))
        self.photoimg3 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg3, bg="black", relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)



        # =============table frame==============
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system",
                                 font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lblsearchby = Label(table_frame, font=("arial", 12, "bold"), text="search By:", bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=27,
                                    state="readonly")
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()
        textsearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=("arial", 12, "bold"), width=24)
        textsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, text="Search",command=self.search, font=("times new roman", 14, "bold"),
                           bg="black", fg="gold", width=8)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(table_frame, text="Show All",command=self.fetch_data,

                            font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", width=8)
        btnshowall.grid(row=0, column=4, padx=1)

        # =====================show data table===============

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,
                                               columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
                                                        "noofdays"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Mobile")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()


    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "all fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get() 

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "room booked", parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

# get cursor
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

# update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:

            conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123",
                                           database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update room set checkin = %s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s where contact=%s",
                (

                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()

                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "room details has been updated successfully", parent=self.root)


    # delete function
    def Delete(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "frist enter the mobile number to delete", parent=self.root)
        else:

            Delete = messagebox.askyesno("Hotel Management System", "do you want to delete this customer",
                                         parent=self.root)
            if Delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123",
                                               database="management")
                my_cursor = conn.cursor()
                query = "delete from room where contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)

            else:
                if not Delete:
                    return

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")

    # =======================all data fetch +=================
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123",
                                           database="management")
            my_cursor = conn.cursor()
            query = ("select name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","this number not found", parent=self.root)
            else:
                # conn.commit()
                # conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=440, y=55, width=300, height=180)

            # ============== displaying name=================
                lblName = Label(showDataframe, text="Name:", font=("arial",12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row,font=("arial",12, "bold"))
                lbl.place(x=90, y=0)

            # ================displaying gender ==================
                # conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123",
                #                                database="management")
                # my_cursor = conn.cursor()
                query = ("select gender from customer where Mobile=%s")
                # value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial",12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row,font=("arial",12, "bold"))
                lbl2.place(x=90, y=30)

            # ====================displaying mobile number ====================
                lblmobile = Label(showDataframe, text="Mobile:",font=("arial",12, "bold"))
                lblmobile.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=value,font=("arial",12, "bold"))
                lbl3.place(x=90, y=60)

            # =================displaying email=============
                query = ("select email from customer where Mobile=%s")
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email:", font=("arial",12, "bold"))
                lblemail.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row,font=("arial",12, "bold"))
                lbl4.place(x=90, y=90)

                # ================ displaying nationality=============
                query = ("select nationality from customer where Mobile=%s")
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnationality.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)
            # =================displaying address=============
                query = ("select address from customer where Mobile=%s")
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address:", font=("arial",12, "bold"))
                lbladdress.place(x=0, y=150)

                lbl6 = Label(showDataframe, text=row,font=("arial",12, "bold"))
                lbl6.place(x=90, y=150)


    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mysql@123", database="management")
        my_cursor = conn.cursor()

        # Correctly formatted query using parameterized query
        query = "SELECT * FROM room WHERE " + self.search_var.get() + " LIKE %s"
        value = ("%" + self.txt_search.get() + "%",)

        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkout.get()
        indate = datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)


        if self.var_meal.get().lower() == "breakfast" and self.var_roomtype.get() == "laxary":
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs." + str("%.2f"%(q5*0.1))
            st = "Rs." +str("%.2f" % q5)
            tt = "Rs."+str("%.2f" % (q5+(q5*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total. set(tt)

        elif self.var_meal.get().lower() == "lunch" and self.var_roomtype.get() == "single":
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs." + str("%.2f"%(q5*0.1))
            st = "Rs." +str("%.2f" % q5)
            tt = "Rs."+str("%.2f" % (q5+(q5*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
