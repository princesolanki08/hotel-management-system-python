from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
# import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Variables 
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_total=StringVar()

        # Title
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",40,  "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # Logo
        img2=Image.open(r"D:\My Projects\Hotel Management Project\Images\logoimg2.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
        # Label Frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details ",font=("times new roman",12,  "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # Fetch data Botton
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=340,y=4)

        # Check in Date
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        # Check Out Date
        lbl_Check_out=Label(labelframeleft,text="Check_out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txtcheck_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txtcheck_out.grid(row=2,column=1)

        # Room Type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        lbl_RoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        # Meal
        lbl_Meal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)

        # No of Days
        lbl_NoOfDays=Label(labelframeleft,text="Number of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_NoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        # Total Bill
        lbl_IdNumber=Label(labelframeleft,text="Total Bill:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_IdNumber.grid(row=7,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))
        txtIdNumber.grid(row=7,column=1)

        # Bill Button
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=8,column=0,padx=1,sticky=W)

        # Buttons 
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=310,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9) 
        btnReset.grid(row=0,column=3,padx=1)

        # Right Side Image 
        img7=Image.open(r"D:\My Projects\Hotel Management Project\Images\img7.jpg")
        img7=img7.resize((550,290))
        self.photoimg7=ImageTk.PhotoImage(img7)

        lblimg=Label(self.root,image=self.photoimg7,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=400,height=290)

        # Table Frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Detail and Search System ",font=("times new roman",12,  "bold"),padx=2)
        Table_Frame.place(x=435,y=220,width=860,height=200)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=10,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0) 
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",8,"bold"),bg="black",fg="gold",width=7 )
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btnShowAll.grid(row=0,column=4,padx=2) 

        # Show Data Table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=28,width=600,height=155)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL) 
        
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100) 
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor) 
        self.fetch_data()
 
        # Add Data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Fill All Details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_contact.get(),
                                                                self.var_checkin.get(),
                                                                self.var_checkout.get(),
                                                                self.var_roomtype.get(),
                                                                self.var_roomavailable.get(),
                                                                self.var_meal.get(),
                                                                self.var_noofdays.get()
                                                                # self.var_total=StringVar()
                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.close() 

    # Get Cursor -> database se value boxes me bharna
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
    
    # Update button ka function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s,meal=%s, noofdays=%s WHERE contact=%s""",
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
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)

    # Delete Button Function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor=conn.cursor()
            query = "delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()

    # Reset Button Function
    def reset(self): 
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_total.set("")

    # All Data Fetch
            # Frame and Name
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This Number is Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=435,y=52,width=322,height=167)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=70,y=0)

                # Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=70,y=30)

                # Email
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=70,y=60)

                # Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                # ID Number
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Idnumber from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblIdnumber=Label(showDataframe,text="Id Number:",font=("arial",12,"bold"))
                lblIdnumber.place(x=0,y=120)
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
    
    # search System
    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()        
        my_cursor.execute(f"SELECT * FROM customer WHERE Mobile LIKE '%{self.var_contact.get()}%'")

        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Total Bill
    def total(self):
        try:
            inDate = self.var_checkin.get()
            outDate = self.var_checkout.get()
            inDate = datetime.strptime(inDate, "%d/%m/%y")
            outDate = datetime.strptime(outDate, "%d/%m/%y")

            # Calculate the number of days
            self.var_noofdays.set(abs((outDate - inDate).days))
            no_of_days = float(self.var_noofdays.get())

            # Price 
            if self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "luxury":
                room_price = 1500
                meal_price = 400
            else:
                room_price = 900  # Default room price
                meal_price = 1100  # Default meal price

            total_bill = no_of_days * (room_price + meal_price)
            self.var_total.set(f"Rs. {total_bill:.2f}")
            messagebox.showinfo("Success", f"Total bill is {self.var_total.get()}", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root) 
    root.mainloop()