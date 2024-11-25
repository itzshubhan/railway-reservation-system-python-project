import tkinter
import customtkinter
from PIL import ImageTk, Image
import subprocess

# Set CustomTkinter appearance and color theme
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

# Create the main application window
app = customtkinter.CTk()
app.resizable(False, False)
app.geometry("800x440")
app.title('Login')

# Function to handle the button click, which opens `create_account.py`
def button_function():
    app.destroy()  # Close the login window
    subprocess.run(["python", "create_account.py"])  # Open the create_account.py file

# Load and set background image if available
try:
    img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
except FileNotFoundError:
    print("Image file './assets/pattern.png' not found.")
    img1 = None

# Set background label with image if available
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# Create frame for login inputs and button
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Add label, entry fields, and button to the frame
l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
l3.place(x=155, y=195)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

app.mainloop()
