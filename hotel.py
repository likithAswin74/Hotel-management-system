from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1550x800+0+0")

        # =================top image===============
        img1 = Image.open("hotel.jpg.png")
        img1 = img1.resize((1550, 140))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ====================logo==================
        img2 = Image.open("logo.jpg")
        img2 = img2.resize((230, 140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ====================title==================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ===================main frame=================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================menu=============
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ===========================button frame=================
        btn_frame = Frame(main_frame, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=40, width=228, height=180)

        # ==================buttons===================
        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4,
                          cursor="hand1")
        cust_btn.grid(row=0, column=0)

        room_btn = Button(btn_frame, text="ROOM", width=22,command=self.roombooking_details, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4,
                          cursor="hand1")
        room_btn.grid(row=1, column=0)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4,
                          cursor="hand1")
        details_btn.grid(row=2, column=0)

        logout = Button(btn_frame, text="LOG OUT", width=22,  font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4,
                          cursor="hand1")
        logout.grid(row=3, column=0)

        # ==============right side image=============

        img3 = Image.open("waiting.png")
        img3 = img3.resize((1310,590))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)


        # =============down images===============

        img4 = Image.open("waiting.png")
        img4 = img4.resize((230,210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)


        img5 = Image.open("waiting.png")
        img5 = img5.resize((230,190))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)


    def roombooking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
