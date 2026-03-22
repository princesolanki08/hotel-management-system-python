from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
# import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New  Room Add ",font=("times new roman",12,  "bold"),padx=2)
        labelframeleft.place(x=5,y=55,width=500,height=350)
    
        # Floor Details
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_Floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        # Buttons 
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9) 
        btnReset.grid(row=0,column=3,padx=1)

        # Table Frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,  "bold"),padx=2)
        Table_Frame.place(x=530,y=55,width=500,height=350)

        # Scroll Bar
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL) 
        
        self.room_table=ttk.Treeview(Table_Frame,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("RoomNo",text="Room No")
        self.room_table.heading("RoomType",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("Floor",width=100)
        self.room_table.column("RoomNo",width=100)
        self.room_table.column("RoomType",width=100)
       
        self.room_table.pack(fill=BOTH,expand=1)   
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor) 
        self.fetch_data()

     # Add Data
    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","Fill All Details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password = "1234",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                self.var_Floor.get(),
                                                                self.var_RoomNo.get(),
                                                                self.var_RoomType.get()
                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)

    
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_Floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    # Update button ka function
    def update(self):
        if self.var_Floor.get() == "":
            messagebox.showerror("Error", "Enter Floor Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE details SET Floor=%s, RoomType=%s WHERE RoomNo=%s""",
            (
                self.var_Floor.get(),
                self.var_RoomType.get(),
                self.var_RoomNo.get(), 
            ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "New Room details have been updated successfully", parent=self.root)

    # Delete Button Function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor=conn.cursor()
            query = "delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()

    def reset_data(self):
        self.var_Floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Details(root) 
    root.mainloop()