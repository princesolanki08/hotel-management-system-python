from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
 
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
       
        # Title
        lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",40,  "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # Logo
        img2=Image.open(r"D:\My Projects\Hotel Management Project\Images\logoimg2.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # Label Frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details ",font=("times new roman",12,  "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # Customer Name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=0,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",13,"bold"))
        txtcname.grid(row=0,column=1)

        # Gender Combox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender",padx=2,pady=6)
        label_gender.grid(row=1,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=1,column=1)

        # Mobile Number
        lblMobile=Label(labelframeleft,text="Mobile Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=2,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
        txtMobile.grid(row=2,column=1)

        # Email
        lblEmail=Label(labelframeleft,text="Email Id",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=3,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
        txtEmail.grid(row=3,column=1)

        # Nationality
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=4,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,text="Nationality",textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("India","Japan","Russia")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=4,column=1)

        # Id Proof Type ComBox
        lblIdProof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=5,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Adhar Card","Driving Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=5,column=1) 

        # Id Number
        lblIdNumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=6,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_id_number,font=("arial",13,"bold"))
        txtIdNumber.grid(row=6,column=1)

        # Buttons 
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=270,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete ,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9) 
        btnReset.grid(row=0,column=3,padx=1)
        
        # Table Frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Detail and Search System ",font=("times new roman",12,  "bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=10,state="readonly")
        combo_Search["value"]=("Mobile")
        combo_Search.current(0) 
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",8,"bold"),bg="black",fg="gold",width=7 )
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btnShowAll.grid(row=0,column=4,padx=2) 

        # Show Data Table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=295)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        # Scroll Bar -> Video 2 code with kiran 47 min 
        
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("name","gender","mobile","email","nationality","idproof","idnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100) 
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # Add Data
    def add_data(self):
        if self.var_cust_name.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","Fill All Details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_cust_name.get(),
                                                                self.var_gender.get(),
                                                                self.var_mobile.get(),
                                                                self.var_email.get(),
                                                                self.var_nationality.get(),
                                                                self.var_id_proof.get(),
                                                                self.var_id_number.get()
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.close() 

    # Get Cursor -> database se value boxes me bharna
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_cust_name.set(row[0]),
        self.var_gender.set(row[1]),
        self.var_mobile.set(row[2]),
        self.var_email.set(row[3]),
        self.var_nationality.set(row[4]),
        self.var_id_proof.set(row[5]),
        self.var_id_number.set(row[6])

    # Update button ka function   
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE customer SET Name=%s, Gender=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s WHERE Mobile=%s""",
            (
                self.var_cust_name.get(),  # Name
                self.var_gender.get(),     # Gender
                self.var_email.get(),      # Email
                self.var_nationality.get(),# Nationality
                self.var_id_proof.get(),   # Idproof
                self.var_id_number.get(),  # Idnumber
                self.var_mobile.get()      # Mobile (WHERE condition)
            ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)

    # Delete Button Function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
            my_cursor=conn.cursor()
            query = "delete from customer where Mobile=%s"
            value=(self.var_mobile.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()

    # Reset Button Function
    def reset(self):
        self.var_cust_name.set(""),  # Name
        # self.var_gender.set(""),     # Gender
        self.var_email.set(""),      # Email
        # self.var_nationality.set(""), # Nationality
        # self.var_id_proof.set(""),   # Idproof
        self.var_id_number.set(""),  # Idnumber
        self.var_mobile.set("")      # Mobile (WHERE condition)
    
    # search System
    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="hotel_management")
        my_cursor=conn.cursor()        
        my_cursor.execute(f"SELECT * FROM customer WHERE Mobile LIKE '%{self.var_mobile.get()}%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()