#!/usr/bin/env python
# coding: utf-8

# In[13]:


from datetime import datetime
from typing import List, Optional

class Administrators:
    """Class for park administrators to manage users and generate reports."""
    
    def __init__(self, admin_id: int, username: str, password: str):
        self.admin_id = admin_id
        self.username = username
        self.password = password

    def log_in(self):
        print(f"Administrator {self.username} logged in successfully.")

    def manage_users(self):
        print("Managing users...")

    def generate_reports(self):
        print("Generating reports...")

class CapacityManager(Administrators):
    """Class to manage park capacity, inherits from Administrators."""
    
    def __init__(self, admin_id: int, username: str, password: str, date: int, current_attendance: int, max_capacity: int):
        super().__init__(admin_id, username, password)
        self.date = date
        self.current_attendance = current_attendance
        self.max_capacity = max_capacity

    def update_attendance(self, new_attendance: int):
        self.current_attendance = new_attendance
        print(f"Attendance updated to {self.current_attendance}.")

    def check_capacity_status(self):
        if self.current_attendance >= self.max_capacity:
            print("Park is at full capacity.")
        else:
            print("Capacity available.")

class Event:
    """Class representing an event in the park."""
    
    def __init__(self, event_id: int, event_name: str, schedule: str, description: str):
        self.event_id = event_id
        self.event_name = event_name
        self.schedule = schedule
        self.description = description

    def get_event_info(self):
        return f"Event: {self.event_name}, Schedule: {self.schedule}, Description: {self.description}"

    def update_event_schedule(self, new_schedule: str):
        self.schedule = new_schedule
        print("Event schedule updated.")

class Attraction:
    """Class representing an attraction in the park."""
    
    def __init__(self, attraction_id: int, name: str, status: bool, wait_time: float):
        self.attraction_id = attraction_id
        self.name = name
        self.status = status
        self.wait_time = wait_time

    def get_attraction_status(self):
        return f"Attraction {self.name} is {'open' if self.status else 'closed'}."

    def update_wait_time(self, new_wait_time: float):
        self.wait_time = new_wait_time
        print(f"Wait time updated to {self.wait_time} minutes.")

class Visitor:
    """Class representing a visitor to the theme park."""
    
    def __init__(self, visitor_id: int, name: str, email: str, payment_info: str):
        self.visitor_id = visitor_id
        self.name = name
        self.email = email
        self.payment_info = payment_info

    def update_profile(self, new_name: str, new_email: str):
        self.name = new_name
        self.email = new_email
        print("Visitor profile updated.")

    def make_payment(self, amount: float):
        print(f"Payment of {amount} processed for {self.name}.")

class Account:
    """Class representing a user account linked to a visitor."""
    
    def __init__(self, account_id: int, visitor: Visitor, username: str, password: str):
        self.account_id = account_id
        self.visitor = visitor
        self.username = username
        self.password = password
        self.purchase_history = PurchaseHistory(self.account_id)

    def log_in(self):
        print(f"Account {self.username} logged in successfully.")

    def log_out(self):
        print(f"Account {self.username} logged out.")

    def update_account_info(self, new_username: str, new_password: str):
        self.username = new_username
        self.password = new_password
        print("Account information updated.")

class Reservation:
    """Class representing a reservation."""
    
    def __init__(self, reservation_id: int, visitor: Visitor, ticket: 'Ticket', visit_date: datetime):
        self.reservation_id = reservation_id
        self.visitor = visitor
        self.ticket = ticket
        self.visit_date = visit_date

    def create_reservation(self):
        print("Reservation created successfully.")

    def modify_reservation(self, new_date: datetime):
        self.visit_date = new_date
        print("Reservation date modified.")

    def cancel_reservation(self):
        print("Reservation cancelled.")

class Ticket:
    """Class to represent a ticket."""
    
    def __init__(self, ticket_id: int, ticket_type: str, price: float, validity_period: int):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price
        self.validity_period = validity_period

    def calculate_price(self, discount: Optional[float] = None) -> float:
        if discount:
            return self.price * (1 - discount / 100)
        return self.price

    def validate_ticket(self):
        print(f"Ticket {self.ticket_id} validated.")

class Payment:
    """Class representing a payment transaction."""
    
    def __init__(self, payment_id: int, visitor: Visitor, amount: float, payment_method: bool, payment_status: bool):
        self.payment_id = payment_id
        self.visitor = visitor
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def process_payment(self):
        print(f"Payment of {self.amount} processed.")

    def refund_payment(self):
        print(f"Payment of {self.amount} refunded.")

class PurchaseHistory:
    """Class to track purchase history."""
    
    def __init__(self, account_id: int):
        self.history_id = account_id
        self.purchases = []

    def view_history(self):
        return self.purchases

    def add_purchase_record(self, amount: float):
        self.purchases.append(amount)
        print(f"Purchase of {amount} added to history.")

class Discount:
    """Class to apply discounts."""
    
    def __init__(self, discount_id: int, description: str, percentage_off: float):
        self.discount_id = discount_id
        self.description = description
        self.percentage_off = percentage_off

    def apply_discount(self, amount: float) -> float:
        discounted_amount = amount * (1 - self.percentage_off / 100)
        print(f"Discount applied: New amount is {discounted_amount}")
        return discounted_amount

    def modify_discount(self, new_percentage: float):
        self.percentage_off = new_percentage
        print(f"Discount modified to {self.percentage_off}% off.")

class ParkService:
    """Class representing a service in the park."""
    
    def __init__(self, service_id: int, service_name: str, service_description: str):
        self.service_id = service_id
        self.service_name = service_name
        self.service_description = service_description

    def get_service_info(self):
        return f"Service: {self.service_name} - {self.service_description}"

    def update_service_info(self, new_description: str):
        self.service_description = new_description
        print("Service description updated.")

#Test Case 1: Single-Day Pass without Discount     
# Visitor details
visitor1 = Visitor(visitor_id=1, name="Meera Alawadhi", email="meera@example.com", payment_info="Visa")

# Ticket details (Single-Day Pass)
ticket1 = Ticket(ticket_id=101, ticket_type="Single-Day Pass", price=275, validity_period=1)

# Calculate ticket price without any discount
price = ticket1.calculate_price()
print(f"Ticket Price for {visitor1.name}: {price} DHS")  # Expected output: 275 DHS

# Process payment
payment1 = Payment(payment_id=201, visitor=visitor1, amount=price, payment_method=True, payment_status=True)
print(f"Processing payment for {visitor1.name}...")
payment1.process_payment()  # Expected to process payment of 275 DHS

#Test Case 2: Two-Day Pass with Online Discount (10%)
# Visitor details
visitor2 = Visitor(visitor_id=2, name="Ahmed Hattawi", email="Ahmed@example.com", payment_info="MasterCard")

# Ticket details (Two-Day Pass with 10% discount)
ticket2 = Ticket(ticket_id=102, ticket_type="Two-Day Pass", price=480, validity_period=2)

# Apply 10% discount for online purchase
discount = Discount(discount_id=301, description="Online Purchase Discount", percentage_off=10)
discounted_price = discount.apply_discount(ticket2.price)
print(f"Discounted Ticket Price for {visitor2.name}: {discounted_price} DHS")  # Expected output: 432 DHS

# Process payment
payment2 = Payment(payment_id=202, visitor=visitor2, amount=discounted_price, payment_method=True, payment_status=True)
print(f"Processing payment for {visitor2.name}...")
payment2.process_payment()  # Expected to process payment of 432 DHS

#Test Case 3: Group Ticket for 20+ People with Group Discount (20%)
# Visitor details (Group reservation holder)
visitor3 = Visitor(visitor_id=3, name="Alya Alobaidly", email="Alya@example.com", payment_info="Amex")

# Ticket details (Group Ticket with 20% discount for 20 or more people)
group_ticket_price = 220  # Price per person
number_of_people = 25     # Qualifies for group discount
total_price = group_ticket_price * number_of_people

# Apply 20% group discount
group_discount = Discount(discount_id=302, description="Group Discount", percentage_off=20)
discounted_total_price = group_discount.apply_discount(total_price)
print(f"Total Price for Group Ticket (25 people, with discount) for {visitor3.name}: {discounted_total_price} DHS")  # Expected output: 4400 DHS

# Create reservation
reservation = Reservation(reservation_id=401, visitor=visitor3, ticket=Ticket(ticket_id=103, ticket_type="Group Ticket", price=group_ticket_price, validity_period=1), visit_date=datetime(2024, 12, 25))
print(f"Creating reservation for {visitor3.name}...")
reservation.create_reservation()  # Expected to create a reservation

# Process payment
payment3 = Payment(payment_id=203, visitor=visitor3, amount=discounted_total_price, payment_method=True, payment_status=True)
print(f"Processing payment for {visitor3.name}...")
payment3.process_payment()  # Expected to process payment of 4400 DHS

# Add to purchase history
visitor_account = Account(account_id=501, visitor=visitor3, username="charlie_brown", password="password123")
print(f"Adding purchase record for {visitor3.name}...")
visitor_account.purchase_history.add_purchase_record(discounted_total_price)  # Expected to add 4400 DHS to purchase history

# View purchase history
print(f"Purchase History for {visitor3.name}:", visitor_account.purchase_history.view_history())  # Expected output: [4400 DHS]


import tkinter as tk
from tkinter import messagebox, ttk

# Global color theme
BACKGROUND_COLOR = "#ffe4e1"  # Light pink
BUTTON_COLOR = "#ffcccb"      # Pink button color
TITLE_COLOR = "#ffcc00"       # Yellow color for titles

# Main GUI Application
class ThemeParkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Land Theme Park")
        self.configure(bg=BACKGROUND_COLOR)
        self.geometry("800x600")

        # Navigation Frame
        self.nav_frame = tk.Frame(self, bg=TITLE_COLOR)
        self.nav_frame.pack(side="top", fill="x")

        tk.Button(self.nav_frame, text="Account Management", bg=BUTTON_COLOR, command=self.show_account_management).pack(side="left", padx=10, pady=10)
        tk.Button(self.nav_frame, text="Ticket Purchasing", bg=BUTTON_COLOR, command=self.show_ticket_purchasing).pack(side="left", padx=10, pady=10)
        tk.Button(self.nav_frame, text="Admin Dashboard", bg=BUTTON_COLOR, command=self.show_admin_dashboard).pack(side="left", padx=10, pady=10)

        # Content Frame
        self.content_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        self.content_frame.pack(expand=True, fill="both")
        
        # Start with the Account Management screen
        self.show_account_management()

    def clear_content(self):
        # Clear the content frame for new content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_account_management(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Account Management", font=("Arial", 18), bg=TITLE_COLOR, fg="black").pack(pady=10)

        # Add form to create/update an account
        tk.Label(self.content_frame, text="Username:", bg=BACKGROUND_COLOR).pack(pady=5)
        self.username_entry = tk.Entry(self.content_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.content_frame, text="Password:", bg=BACKGROUND_COLOR).pack(pady=5)
        self.password_entry = tk.Entry(self.content_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.content_frame, text="Create/Update Account", bg=BUTTON_COLOR, command=self.create_update_account).pack(pady=10)
        tk.Button(self.content_frame, text="View Account Details", bg=BUTTON_COLOR, command=self.view_account_details).pack(pady=10)
        tk.Button(self.content_frame, text="Delete Account", bg=BUTTON_COLOR, command=self.delete_account).pack(pady=10)

    def create_update_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            messagebox.showinfo("Success", f"Account for '{username}' has been created/updated.")
        else:
            messagebox.showwarning("Input Error", "Please enter a username and password.")

    def view_account_details(self):
        username = self.username_entry.get()
        if username:
            messagebox.showinfo("Account Details", f"Details for account '{username}':\n[Mock data displayed here]")
        else:
            messagebox.showwarning("Input Error", "Please enter a username to view details.")

    def delete_account(self):
        username = self.username_entry.get()
        if username:
            messagebox.showinfo("Deleted", f"Account '{username}' has been deleted.")
        else:
            messagebox.showwarning("Input Error", "Please enter a username to delete.")

    def show_ticket_purchasing(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Ticket Purchasing", font=("Arial", 18), bg=TITLE_COLOR, fg="black").pack(pady=10)

        # Ticket options
        tk.Label(self.content_frame, text="Select Ticket Type:", bg=BACKGROUND_COLOR).pack(pady=5)
        self.ticket_type = ttk.Combobox(self.content_frame, values=["Single-Day Pass - 275 DHS", "Two-Day Pass - 480 DHS (10% Discount for Online)", "Annual Membership - 1840 DHS (15% Renewal Discount)", "Group Ticket (10+) - 220 DHS per person (20% Discount for 20+ people)", "VIP Experience Pass - 550 DHS"])
        self.ticket_type.pack(pady=5)

        tk.Label(self.content_frame, text="Number of Tickets:", bg=BACKGROUND_COLOR).pack(pady=5)
        self.num_tickets = tk.Entry(self.content_frame)
        self.num_tickets.pack(pady=5)

        tk.Button(self.content_frame, text="Calculate Price", bg=BUTTON_COLOR, command=self.calculate_price).pack(pady=10)
        tk.Button(self.content_frame, text="Make Payment", bg=BUTTON_COLOR, command=self.make_payment).pack(pady=10)

    def calculate_price(self):
        ticket = self.ticket_type.get()
        num_tickets = self.num_tickets.get()
        
        if not ticket:
            messagebox.showwarning("Input Error", "Please select a ticket type.")
            return
        
        if not num_tickets.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid number of tickets.")
            return

        num_tickets = int(num_tickets)
        if "Single-Day Pass" in ticket:
            price = 275 * num_tickets
        elif "Two-Day Pass" in ticket:
            price = 480 * num_tickets * 0.9  # 10% discount for online purchase
        elif "Annual Membership" in ticket:
            price = 1840 * num_tickets * 0.85  # 15% discount on renewal
        elif "Group Ticket" in ticket:
            price_per_person = 220
            if num_tickets >= 20:
                price_per_person *= 0.8  # 20% discount for 20+ people
            price = price_per_person * num_tickets
        elif "VIP Experience Pass" in ticket:
            price = 550 * num_tickets
        else:
            price = 0

        messagebox.showinfo("Total Price", f"The total price is: {price} DHS")

    def make_payment(self):
        ticket = self.ticket_type.get()
        if ticket:
            messagebox.showinfo("Payment", f"Payment for '{ticket}' completed successfully.")
        else:
            messagebox.showwarning("Input Error", "Please select a ticket type to purchase.")

    def show_admin_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Admin Dashboard", font=("Arial", 18), bg=TITLE_COLOR, fg="black").pack(pady=10)

        tk.Button(self.content_frame, text="View Ticket Sales", bg=BUTTON_COLOR, command=self.view_ticket_sales).pack(pady=10)
        tk.Button(self.content_frame, text="Modify Discounts", bg=BUTTON_COLOR, command=self.modify_discounts).pack(pady=10)

    def view_ticket_sales(self):
        messagebox.showinfo("Ticket Sales", "Ticket Sales:\n[Mock data for daily sales shown here]")

    def modify_discounts(self):
        messagebox.showinfo("Modify Discounts", "Discount options are available for modification.")

# Run the application
if __name__ == "__main__":
    app = ThemeParkApp()
    app.mainloop()


# In[ ]:




