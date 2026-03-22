# from tkinter import*
# from PIL import Image,ImageTk  
# from customer import Cust_Win
# from room import Roombooking
# from details import Details

# class Hotel_Management_System:
#     def __init__(self,root):
#       self.root=root
#       self.root.title("Hotel Management System")
#       self.root.geometry("1500x800+0+0")

# if __name__ == "__main__":
#    root=Tk()
#    obj= Hotel_Management_System(root)
#    root.mainloop()

from tkinter import *
from tkinter import ttk  # For Notebook (Tabbed Interface)
from PIL import Image, ImageTk


class Hotel_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")

        # Title Label
        title_label = Label(self.root, text="Hotel Management System", font=("Arial", 30, "bold"), bg="blue", fg="white")
        title_label.pack(side=TOP, fill=X)

        # Create Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=1)

        # Tabs
        self.create_customer_tab()
        self.create_room_booking_tab()
        self.create_details_tab()

    def create_customer_tab(self):
        """Create Customer Tab"""
        customer_frame = Frame(self.notebook)
        self.notebook.add(customer_frame, text="Customer Details")

        Label(customer_frame, text="Customer Management", font=("Arial", 20, "bold")).pack(pady=20)
        Button(customer_frame, text="Add Customer", font=("Arial", 14), command=self.dummy_function).pack(pady=10)

    def create_room_booking_tab(self):
        """Create Room Booking Tab"""
        room_frame = Frame(self.notebook)
        self.notebook.add(room_frame, text="Room Booking")

        Label(room_frame, text="Room Booking Management", font=("Arial", 20, "bold")).pack(pady=20)
        Button(room_frame, text="Book a Room", font=("Arial", 14), command=self.dummy_function).pack(pady=10)

    def create_details_tab(self):
        """Create Details Tab"""
        details_frame = Frame(self.notebook)
        self.notebook.add(details_frame, text="Details")

        Label(details_frame, text="Hotel Details", font=("Arial", 20, "bold")).pack(pady=20)
        Button(details_frame, text="View Details", font=("Arial", 14), command=self.dummy_function).pack(pady=10)

    def dummy_function(self):
        """Placeholder for actual functionality"""
        print("Button clicked!")


if __name__ == "__main__":
    root = Tk()
    obj = Hotel_Management_System(root)
    root.mainloop()
