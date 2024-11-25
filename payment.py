import customtkinter as ctk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk  # Required to load and display images in tkinter

# Initialize the main application window
app = ctk.CTk()
app.title("Passenger Details")
app.geometry("800x700")  # Adjusted window size to fit everything

# Title Label
title_label = ctk.CTkLabel(app, text="Passenger Details", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=(10, 5), sticky="n")

# Subheading
subheading_label = ctk.CTkLabel(
    app,
    text="Enhance Your Travel with Taste! Opt for Onboard Catering for a Delicious Dining Experience!",
    font=("Arial", 10),
    text_color="green",
)
subheading_label.grid(row=1, column=0, columnspan=4, pady=(5, 20), sticky="n")

# Create a scrollable frame to hold passenger entries
scrollable_frame_1 = ctk.CTkScrollableFrame(app, width=750, height=350)
scrollable_frame_1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Configure grid to expand the scrollable frame dynamically
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)

# Global variables for tracking passenger count and prices
passenger_count = 0
ticket_price = 100  # Example ticket price
donation_per_passenger = 10  # Hunger relief donation per passenger

# Label to display the total amount to be paid
total_label = ctk.CTkLabel(app, text="Total Amount to Pay: ₹0", font=("Arial", 14))
total_label.grid(row=3, column=0, columnspan=4, pady=(10, 5))

# Function to calculate the total amount for all passengers
def calculate_total():
    total_amount = passenger_count * (ticket_price + donation_per_passenger)
    total_label.configure(text=f"Total Amount to Pay: ₹{total_amount}")  # Use configure instead of config
    return total_amount

# Function to add a passenger's details dynamically
def add_passenger():
    global passenger_count
    row = passenger_count * 6  # Create space for each passenger's details within the scrollable frame

    # Passenger Name Entry
    name_label = ctk.CTkLabel(scrollable_frame_1, text="Passenger Name:")
    name_label.grid(row=row, column=0, padx=(10, 5), pady=5, sticky="e")
    name_entry = ctk.CTkEntry(scrollable_frame_1, width=150)
    name_entry.grid(row=row, column=1, padx=(5, 10), pady=5)

    # Age Entry
    age_label = ctk.CTkLabel(scrollable_frame_1, text="Age:")
    age_label.grid(row=row, column=2, padx=(10, 5), pady=5, sticky="e")
    age_entry = ctk.CTkEntry(scrollable_frame_1, width=50)
    age_entry.grid(row=row, column=3, padx=(5, 10), pady=5)

    # Gender Option Menu (Dropdown)
    gender_label = ctk.CTkLabel(scrollable_frame_1, text="Gender:")
    gender_label.grid(row=row + 1, column=0, padx=(10, 5), pady=5, sticky="e")
    gender_option = ctk.CTkOptionMenu(scrollable_frame_1, values=["Male", "Female", "Other"])
    gender_option.grid(row=row + 1, column=1, padx=(5, 10), pady=5)

    # Nationality Option Menu (Dropdown)
    nationality_label = ctk.CTkLabel(scrollable_frame_1, text="Nationality:")
    nationality_label.grid(row=row + 1, column=2, padx=(10, 5), pady=5, sticky="e")
    nationality_option = ctk.CTkOptionMenu(scrollable_frame_1, values=["India", "Other"])
    nationality_option.grid(row=row + 1, column=3, padx=(5, 10), pady=5)

    # Catering Service Option Menu (Dropdown) - Below Gender
    catering_label = ctk.CTkLabel(scrollable_frame_1, text="Catering Service Option:")
    catering_label.grid(row=row + 2, column=0, padx=(10, 5), pady=5, sticky="e")
    catering_option = ctk.CTkOptionMenu(scrollable_frame_1, values=["Veg", "Non-Veg", "No Preference"])
    catering_option.grid(row=row + 2, column=1, padx=(5, 10), pady=5)

    # Seat Preference Option Menu (Dropdown) - Below Nationality
    seat_pref_label = ctk.CTkLabel(scrollable_frame_1, text="Seat Preference:")
    seat_pref_label.grid(row=row + 2, column=2, padx=(10, 5), pady=5, sticky="e")
    seat_pref_option = ctk.CTkOptionMenu(scrollable_frame_1, values=["Window", "Aisle", "No Preference"])
    seat_pref_option.grid(row=row + 2, column=3, padx=(5, 10), pady=5)

    # Increment passenger count
    passenger_count += 1

    # Update total amount when a passenger is added
    calculate_total()

# Add Passenger Button (positioned dynamically below passenger entries)
add_passenger_button = ctk.CTkButton(app, text="+ Add Passenger", command=add_passenger)
add_passenger_button.grid(row=4, column=0, columnspan=4, pady=20, sticky="s")

# Initial call to add the first passenger
add_passenger()

# Acknowledge checkbox
acknowledge_var = ctk.BooleanVar()
acknowledge_checkbox = ctk.CTkCheckBox(app, text="I acknowledge the total amount", variable=acknowledge_var)
acknowledge_checkbox.grid(row=5, column=0, columnspan=4, pady=10, sticky="w")

# Proceed button (to show payment methods after acknowledgment)
def show_payment_methods():
    if acknowledge_var.get():
        # Clear previous content in the payment frame
        for widget in scrollable_frame_2.winfo_children():
            widget.grid_forget()

        # Show options for Card or UPI payment
        payment_method_label = ctk.CTkLabel(scrollable_frame_2, text="Select Payment Method:")
        payment_method_label.grid(row=0, column=0, padx=20, pady=10)

        card_button = ctk.CTkButton(scrollable_frame_2, text="Card Payment", command=card_payment)
        card_button.grid(row=1, column=0, padx=20, pady=10)

        upi_button = ctk.CTkButton(scrollable_frame_2, text="UPI Payment", command=upi_payment)
        upi_button.grid(row=2, column=0, padx=20, pady=10)
    else:
        messagebox.showwarning("Acknowledgment", "Please acknowledge the total amount to proceed.")

# Proceed Button (at the end of the page)
proceed_button = ctk.CTkButton(app, text="Proceed", command=show_payment_methods)
proceed_button.grid(row=6, column=0, columnspan=4, pady=20)

# Payment Method Section (Scrollable frame for Card or UPI)
scrollable_frame_2 = ctk.CTkScrollableFrame(app, width=750, height=200)
scrollable_frame_2.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Card Payment Option (Details)
def card_payment():
    # Clear previous content
    for widget in scrollable_frame_2.winfo_children():
        widget.grid_forget()

    # Card payment form
    card_details_frame = ctk.CTkFrame(scrollable_frame_2)
    card_details_frame.grid(row=1, column=0, columnspan=2, pady=10)

    # Card Number Entry
    card_number_label = ctk.CTkLabel(card_details_frame, text="Card Number:")
    card_number_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    card_number_entry = ctk.CTkEntry(card_details_frame, width=150)
    card_number_entry.grid(row=0, column=1, padx=10, pady=10)

    # Expiry Date Entry
    expiry_label = ctk.CTkLabel(card_details_frame, text="Expiry Date:")
    expiry_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    expiry_entry = ctk.CTkEntry(card_details_frame, width=50)
    expiry_entry.grid(row=1, column=1, padx=10, pady=10)

    # CVV Entry
    cvv_label = ctk.CTkLabel(card_details_frame, text="CVV:")
    cvv_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    cvv_entry = ctk.CTkEntry(card_details_frame, width=50)
    cvv_entry.grid(row=2, column=1, padx=10, pady=10)

    # Contact Number Entry
    contact_label = ctk.CTkLabel(card_details_frame, text="Contact Number:")
    contact_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    contact_entry = ctk.CTkEntry(card_details_frame, width=150)
    contact_entry.grid(row=3, column=1, padx=10, pady=10)

    # "I'm Sure" Checkbox
    sure_var = ctk.BooleanVar()
    sure_checkbox = ctk.CTkCheckBox(card_details_frame, text="I'm sure of paying this sum", variable=sure_var)
    sure_checkbox.grid(row=4, column=0, columnspan=2, pady=10)

    # Proceed to OTP Button (appears once card details are entered)
    proceed_otp_button = ctk.CTkButton(card_details_frame, text="Proceed to OTP", command=show_otp)
    proceed_otp_button.grid(row=5, column=0, columnspan=2, pady=20)

# OTP Section (appears after clicking Proceed to OTP button)
def show_otp():
    otp_label = ctk.CTkLabel(scrollable_frame_2, text="Enter OTP:")
    otp_label.grid(row=6, column=0, padx=10, pady=10)

    otp_entry = ctk.CTkEntry(scrollable_frame_2, width=150)
    otp_entry.grid(row=6, column=1, padx=10, pady=10)

    confirm_otp_button = ctk.CTkButton(scrollable_frame_2, text="Confirm OTP", command=lambda: show_payment_success())
    confirm_otp_button.grid(row=7, column=0, columnspan=2, pady=20)

# Payment Success Function (called after confirming OTP or UPI payment)
def show_payment_success():
    messagebox.showinfo("Payment Success", "Payment Successful!")
    # You can add any additional logic here, e.g., updating the UI or resetting fields

# UPI Payment Option (Selection of UPI Platform)
def upi_payment():
    # Clear the previous buttons
    for widget in scrollable_frame_2.winfo_children():
        widget.grid_forget()

    # UPI selection
    upi_selection_frame = ctk.CTkFrame(scrollable_frame_2)
    upi_selection_frame.grid(row=1, column=0, columnspan=2, pady=20)

    upi_label = ctk.CTkLabel(upi_selection_frame, text="Select UPI Payment Method:")
    upi_label.grid(row=0, column=0, padx=20, pady=10)

    upi_options = ["GPay", "PhonePe", "Amazon Pay", "Bharat Pay"]
    upi_menu = ctk.CTkOptionMenu(upi_selection_frame, values=upi_options)
    upi_menu.grid(row=1, column=0, padx=20, pady=10)

    # Button to generate the QR code for the selected UPI option
    generate_qr_button = ctk.CTkButton(upi_selection_frame, text="Generate QR", command=lambda: generate_qr())
    generate_qr_button.grid(row=2, column=0, padx=20, pady=10)

# Function to generate the QR code for the selected UPI method
def generate_qr():
    qr_image_path = "C:/Users/shubhan s/OneDrive/Desktop/ccr/assets/qr.png"  # Path for all QR codes
    try:
        qr_image = Image.open(qr_image_path)
        qr_image = qr_image.resize((200, 200))  # Resize the QR if needed
        qr_image_tk = ImageTk.PhotoImage(qr_image)

        qr_label = ctk.CTkLabel(scrollable_frame_2, image=qr_image_tk)
        qr_label.grid(row=3, column=0, pady=20)
        qr_label.image = qr_image_tk  # Keep reference to image to prevent garbage collection

        # Add a "Confirm Payment" button to simulate confirming payment after scanning the QR
        confirm_payment_button = ctk.CTkButton(scrollable_frame_2, text="Confirm Payment", command=show_payment_success)
        confirm_payment_button.grid(row=4, column=0, pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load QR image: {str(e)}")

# Start the Tkinter main loop
app.mainloop()
