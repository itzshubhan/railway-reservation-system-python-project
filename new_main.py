
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter
from PIL import Image
import subprocess

# MySQL connection
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="railway_system"
    )

# Fetch station data from the database
def fetch_station_data():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT code, name FROM stations")
    station_data = cursor.fetchall()
    connection.close()
    return station_data

customtkinter.set_appearance_mode("System")

# Initialize the app
app = customtkinter.CTk()
app.resizable(False, False)
app.geometry("800x440")
app.title('Booking System')


def train():
    app.destroy()
    subprocess.run(['python', 'train.py'])


# Autocomplete functions
def on_keyrelease(event, entry, listbox, values):
    query = entry.get().lower()
    if query == "":
        listbox.place_forget()
        return

    filtered_values = [
        f"{code} - {name}" for code, name in values
        if query in code.lower() or query in name.lower()
    ]

    if filtered_values:
        listbox.delete(0, tk.END)
        for value in filtered_values:
            listbox.insert(tk.END, value)

        # Adjust dropdown size and position dynamically
        listbox.place(
            x=entry.winfo_x(),
            y=entry.winfo_y() + entry.winfo_height(),
            width=entry.winfo_width()
        )
        listbox.config(height=min(len(filtered_values), 6))  # Limit dropdown height to 6 items
    else:
        listbox.place_forget()


def on_select(event, entry, listbox):
    selected = listbox.get(tk.ACTIVE)
    entry.delete(0, tk.END)
    entry.insert(0, selected.split(" - ")[1])  # Insert station name
    listbox.place_forget()


def create_autocomplete_entry(master, values):
    entry = customtkinter.CTkEntry(master, height=35, corner_radius=6)
    listbox = tk.Listbox(
        master,
        height=0,
        bg="white",
        fg="black",
        font=("Century Gothic", 12),
        selectbackground="lightblue",
        selectforeground="black",
        relief="flat",
        bd=0
    )
    listbox.place_forget()

    entry.bind('<KeyRelease>', lambda event: on_keyrelease(event, entry, listbox, values))
    listbox.bind('<ButtonRelease-1>', lambda event: on_select(event, entry, listbox))

    return entry, listbox


# Station data (fetch from database)
stations = fetch_station_data()

# Background image
try:
    bg_image = Image.open("./assets/background.jpg")
    bg_image = bg_image.resize((600, 440))
    img1 = customtkinter.CTkImage(bg_image)
except FileNotFoundError:
    print("Image file './assets/background.jpg' not found.")
    img1 = None

# Search icon
try:
    search_icon = Image.open("./assets/magnifying_glass.png")
    search_icon = search_icon.resize((20, 20))
    search_icon_img = customtkinter.CTkImage(search_icon)
except FileNotFoundError:
    print("Image file './assets/magnifying_glass.png' not found.")
    search_icon_img = None

# Set background
l1 = customtkinter.CTkLabel(master=app, image=img1 if img1 else None)
l1.place(x=0, y=0, relwidth=1, relheight=1)

# Create main frame
frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame.grid_rowconfigure(0, weight=2)
frame.grid_rowconfigure(1, weight=2)
frame.grid_rowconfigure(2, weight=2)
frame.grid_rowconfigure(3, weight=2)
frame.grid_rowconfigure(4, weight=2)
frame.grid_columnconfigure(0, weight=2)

# Title label
l2 = customtkinter.CTkLabel(master=frame, text="Book Tickets", font=('Century Gothic', 20))
l2.grid(row=0, column=0, pady=10, padx=30, sticky="nsew")

# Autocomplete entries
from_station_entry, from_listbox = create_autocomplete_entry(frame, stations)
from_station_entry.grid(row=1, column=0, pady=10, padx=30, sticky="ew")

to_station_entry, to_listbox = create_autocomplete_entry(frame, stations)
to_station_entry.grid(row=2, column=0, pady=10, padx=30, sticky="ew")

# Date picker
date_frame = customtkinter.CTkFrame(master=frame)
date_frame.grid(row=3, column=0, pady=5, padx=30, sticky="ew")

l7 = customtkinter.CTkLabel(master=date_frame, text="Select Date:", font=('Century Gothic', 15))
l7.pack(side="left", padx=5)

entry3 = DateEntry(master=date_frame, width=15, background="darkblue", foreground="white", borderwidth=2)
entry3.pack(side="left", padx=10)

# Class selection dropdown
entry_class = customtkinter.CTkOptionMenu(master=frame, values=["Select class/coach", "Sleeper", "General"], width=220)
entry_class.set("Select class/coach")
entry_class.grid(row=4, column=0, pady=10, padx=30, sticky="ew")

# Search button
button1 = customtkinter.CTkButton(master=frame, width=120, text="Search Train", command=train,
                                   corner_radius=6,
                                   image=search_icon_img, compound="right")
button1.grid(row=5, column=0, pady=10, padx=30, sticky="ew")

app.mainloop()
