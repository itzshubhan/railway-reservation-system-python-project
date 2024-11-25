import customtkinter as ctk

# Initialize customtkinter
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

def create_ticket_page():
    # Main window
    root = ctk.CTk()
    root.title("Railway Reservation - Ticket")
    root.geometry("750x500")
    
    # Header
    header = ctk.CTkLabel(
        master=root,
        text="Railway Reservation System\nFinal Ticket",
        font=("Helvetica", 26, "bold"),
        text_color="#00FF7F",
    )
    header.pack(pady=10)
    
    # Divider Line
    divider = ctk.CTkFrame(master=root, height=2, width=700, fg_color="#00FF7F")
    divider.pack(pady=5)
    
    # Main Content Frame
    content = ctk.CTkFrame(master=root, corner_radius=10)
    content.pack(padx=20, pady=20, fill="both", expand=True)
    
    # Passenger Details Section
    passenger_section = ctk.CTkLabel(
        master=content,
        text="Passenger Details:",
        font=("Helvetica", 20, "bold"),
        text_color="white",
    )
    passenger_section.grid(row=0, column=0, pady=10, sticky="w", padx=10)

    passenger_details = [
        "Name: Shuban",
        "Age: 30",
        "Gender: Male",
        "Contact: 9876543210"
    ]
    for i, detail in enumerate(passenger_details, 1):
        label = ctk.CTkLabel(master=content, text=detail, font=("Helvetica", 16))
        label.grid(row=i, column=0, sticky="w", padx=20)
    
    # Train Details Section
    train_section = ctk.CTkLabel(
        master=content,
        text="Train Details:",
        font=("Helvetica", 20, "bold"),
        text_color="white",
    )
    train_section.grid(row=5, column=0, pady=20, sticky="w", padx=10)

    train_details = [
        "Train Name: InterCity Express",
        "Train Number: 12210",
        "Date: 24-Nov-2024",
        "Departure: 10:00 AM",
        "Arrival: 2:00 PM",
    ]
    for i, detail in enumerate(train_details, 6):
        label = ctk.CTkLabel(master=content, text=detail, font=("Helvetica", 16))
        label.grid(row=i, column=0, sticky="w", padx=20)
    
    # Ticket Summary Section
    summary_section = ctk.CTkLabel(
        master=content,
        text="Ticket Summary:",
        font=("Helvetica", 20, "bold"),
        text_color="white",
    )
    summary_section.grid(row=11, column=0, pady=20, sticky="w", padx=10)

    ticket_summary = [
        "Class: AC Tier 1",
        "Seat Number: B3-21",
        "Price: ₹2,350",
        "PNR: 1234567890",
    ]
    for i, detail in enumerate(ticket_summary, 12):
        label = ctk.CTkLabel(master=content, text=detail, font=("Helvetica", 16))
        label.grid(row=i, column=0, sticky="w", padx=20)
    
    # Footer
    footer = ctk.CTkLabel(
        master=root,
        text="Thank you for choosing Indian Railways!",
        font=("Helvetica", 14, "italic"),
        text_color="#00FF7F",
    )
    footer.pack(pady=10)

    root.mainloop()

# Run the Ticket Page
create_ticket_page()
