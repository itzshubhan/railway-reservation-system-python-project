import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("System")

app = ctk.CTk()
app.geometry("800x500")
app.title("Train Information")
app.resizable(False, False)

# Updated train data with ticket availability
train_data = [
    {'number': '12345', 'name': 'Vande Bharat', 'arrival': '10:00 AM', 'duration': '2h 30m', 'departure': '12:30 PM', 'availability': 'Available'},
    {'number': '67890', 'name': 'Rajdhani', 'arrival': '11:00 AM', 'duration': '3h 15m', 'departure': '2:15 PM', 'availability': 'Waitlist'},
    {'number': '11223', 'name': 'Express 3', 'arrival': '12:00 PM', 'duration': '1h 45m', 'departure': '1:45 PM', 'availability': 'Available'},
    {'number': '33445', 'name': 'Express 4', 'arrival': '1:00 PM', 'duration': '2h 0m', 'departure': '3:00 PM', 'availability': 'Limited'},
    {'number': '55667', 'name': 'Express 5', 'arrival': '2:00 PM', 'duration': '1h 30m', 'departure': '3:30 PM', 'availability': 'Available'},
]

def button_function():
    app.destroy()
    subprocess.run(["python", "passenger_detail.py"])

def create_train_info_page(master):
    # Create a canvas for scrolling
    canvas = ctk.CTkCanvas(master)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Add vertical and horizontal scrollbars
    v_scrollbar = ctk.CTkScrollbar(canvas, orientation="vertical", command=canvas.yview)
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar = ctk.CTkScrollbar(canvas, orientation="horizontal", command=canvas.xview)
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Create a frame to hold the content inside the canvas
    content_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Updated headers with "Ticket Availability"
    headers = ["Train \n Number", "Train \n Name", "Arrival", "Duration", "Departure", "Ticket Availability", "Action"]
    header_frame = ctk.CTkFrame(content_frame)
    header_frame.grid(row=0, column=0, columnspan=1, pady=(10, 10))

    # Configure columns for better alignment
    content_frame.grid_columnconfigure(0, weight=1, uniform="equal")
    content_frame.grid_columnconfigure(1, weight=2, uniform="equal")
    content_frame.grid_columnconfigure(2, weight=1, uniform="equal")
    content_frame.grid_columnconfigure(3, weight=1, uniform="equal")
    content_frame.grid_columnconfigure(4, weight=1, uniform="equal")
    content_frame.grid_columnconfigure(5, weight=1, uniform="equal")
    content_frame.grid_columnconfigure(6, weight=1, uniform="equal")

    # Create header labels
    for col, header in enumerate(headers):
        header_label = ctk.CTkLabel(header_frame, text=header, font=('Arial', 10, 'bold'))
        header_label.grid(row=0, column=col, padx=25, pady=10, sticky="w")

    # Create the train information rows
    for row, train in enumerate(train_data, start=1):
        train_frame = ctk.CTkFrame(content_frame, height=40)
        train_frame.grid(row=row, column=0, padx=26, pady=10, sticky="ew")

        # Train Number
        ctk.CTkLabel(train_frame, text=train['number'], font=('Arial', 12), anchor="w").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Train Name
        ctk.CTkLabel(train_frame, text=train['name'], font=('Arial', 12), anchor="w", width=200).grid(
            row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Arrival
        ctk.CTkLabel(train_frame, text=train['arrival'], font=('Arial', 12), anchor="w").grid(
            row=0, column=2, padx=10, pady=10, sticky="w")
        
        # Duration
        ctk.CTkLabel(train_frame, text=train['duration'], font=('Arial', 12), anchor="w").grid(
            row=0, column=3, padx=10, pady=10, sticky="w")
        
        # Departure
        ctk.CTkLabel(train_frame, text=train['departure'], font=('Arial', 12), anchor="w").grid(
            row=0, column=4, padx=10, pady=10, sticky="w")
        
        # Ticket Availability
        ctk.CTkLabel(train_frame, text=train['availability'], font=('Arial', 12), anchor="w").grid(
            row=0, column=5, padx=10, pady=10, sticky="w")

        # Book Now button
        book_button = ctk.CTkButton(
            train_frame,
            text="Book Now",
            command=lambda tn=train['number']: book_now(tn),
            width=80,
            height=30
        )
        book_button.grid(row=0, column=6, padx=10, pady=10, sticky="e")

    # Update the canvas scroll region after adding all the widgets
    content_frame.update_idletasks()  # Ensure that all widgets are placed before setting scroll region
    canvas.config(scrollregion=canvas.bbox("all"))

def book_now(train_number):
    print(f"Booking train: {train_number}")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

create_train_info_page(app)
app.mainloop()
