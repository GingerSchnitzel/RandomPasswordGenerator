import random
import string
import tkinter as tk
from tkinter import ttk
import clipboard 
from time import sleep


# Generates a password of a customizable length which can include (or not) uppercase and/or lowercase letters, numbers and symbols
def generate_password (length, include_upper, include_lower, include_numbers, include_symbols):
    char_sets = []
    if include_upper:
        char_sets.append(string.ascii_uppercase)
    if include_lower:
        char_sets.append(string.ascii_lowercase)
    if include_numbers:
        char_sets.append(string.digits)
    if include_symbols:
        char_sets.append("!@#$%^&*()-_=+[]{};':\",<.>/?")

    random.shuffle(char_sets)
    password = ""

    for i in range(length):
        chosen_set = random.choice(char_sets)
        password += random.choice(chosen_set)

    return password

# Triggers the update of the password when a change occurs
def update_on_slider_change(event=None):
 
    generated_password = generate_password(
        password_length.get(),
        use_uppercase_letters.get(),
        use_lowercase_letters.get(),
        use_numbers.get(),
        use_symbols.get(),
    )
    password_label.config(text=generated_password)
   

def copy_password():
    if password_label.cget("text") != "Password copied successfully!":
        clipboard.copy(password_label.cget("text"))  # Copy current password

  

def restore_original_password(original_text):
    password_label.config(text=original_text)  # Restore original password
    update_on_slider_change()  # Call update_on_slider_change to ensure password is displayed again


def show_copy_success_message():
    original_text = password_label.cget("text")  # Store original password
    password_label.config(text="Password copied successfully!")  # Show success message 

    # Schedule update function after 10 seconds 
    window.after(2000, restore_original_password, original_text)

 
    

# Window
window = tk.Tk()
window.title("Code In Place Final Project")
window.geometry("700x500")

# Background frame
background_frame = tk.Frame(master = window, background = "yellow")

# Frame which contains the title
title_frame = tk.Frame(master = background_frame, background= "lightblue" )

# Title
title_label = ttk.Label(master = title_frame, text = "Random Password Generator", font ="Poppins 22 bold" )
title_label.grid(row= 0, column = 0, padx = 60, pady = (16, 18), sticky="nsew" )
title_frame.pack()

# Frame to hold label and slider
label_slider_frame = tk.Frame(master=background_frame, background = "pink")


# Label for password length
length_label = tk.Label(label_slider_frame, text="Password Length:", font ="Poppins 12" )
length_label.grid(row=0, column=0, padx = (0, 278), pady=(14,5))  # Place within the frame

# Minus button
def decrease_slider_value():
    current_value = password_length.get()
    if current_value > 1: 
        password_length.set(current_value - 1)
        update_on_slider_change()  # Trigger update

minus_button = tk.Button(label_slider_frame, text="-", command=decrease_slider_value)
minus_button.grid(row=0, column=0, padx=(128, 0), pady=(16,0))  # Place next to slider

# Password length slider
password_length = tk.IntVar(value=8)
length_slider = tk.Scale(label_slider_frame, from_=1, to=50, font= "Poppins 9" ,orient=tk.HORIZONTAL, variable=password_length, command=update_on_slider_change)
length_slider.grid(row=0, column=0, padx = (272,0), pady=(0,6))  # Place within the frame



# Plus button
def increase_slider_value():
    current_value = password_length.get()
    password_length.set(current_value + 1)
    update_on_slider_change()  # Trigger update

plus_button = tk.Button(label_slider_frame, text="+", command=increase_slider_value)
plus_button.grid(row=0, column=0, padx=(420,0), pady=(14,2))  # Place next to slider


# Checkboxes and label variables (checkboxes will be checkd by default)
use_uppercase_letters = tk.IntVar(value=1) 
use_lowercase_letters = tk.IntVar(value=1)
use_numbers = tk.IntVar(value=1)
use_symbols = tk.IntVar(value=1)

# Frame to hold checkboxes and their labels
label_checkbox_frame = tk.Frame(master=background_frame, background = "lightgreen")

# Checkbox creation
uppercase_label = tk.Label(label_checkbox_frame, text="Include Uppercase Letters?", font ="Poppins 12")
uppercase_label.grid(row=0, column=0, padx = (0, 202), pady=(5,5))

uppercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_uppercase_letters, command=update_on_slider_change)
uppercase_checkbox.grid(row=0, column=0, padx = (276,0), pady=(6,5))

lowercase_label = tk.Label(label_checkbox_frame, text="Include Lowercase Letters?", font ="Poppins 12")
lowercase_label.grid(row=1, column=0, padx = (0, 205), pady=(5,5))

lowercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_lowercase_letters, command=update_on_slider_change)
lowercase_checkbox.grid(row=1, column=0, padx = (276,0), pady=(6,5))

numbers_label = tk.Label(label_checkbox_frame, text="Include numbers?", font ="Poppins 12")
numbers_label.grid(row=2, column=0, padx = (0, 276), pady=(5,5))

numbers_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_numbers, command=update_on_slider_change)
numbers_checkbox.grid(row=2, column=0, padx = (276,0), pady=(6,5))

symbols_label = tk.Label(label_checkbox_frame, text="Include symbols?", font ="Poppins 12")
symbols_label.grid(row=3, column=0, padx = (0, 280), pady=(5,5))

symbols_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_symbols, command=update_on_slider_change)
symbols_checkbox.grid(row=3, column=0, padx = (276,0), pady=(6,5))

# Frame to hold generated password
password_frame = tk.Frame(master=background_frame, background = "lightgrey")

# Label for password
password_label = tk.Label(password_frame, font="Poppins 16 bold")
password_label.grid(row = 0, column = 0, padx = 0, pady =(20, 10))  # Pack the label at the bottom

# Copy Button
copy_button = tk.Button(password_frame, text="Copy", font="Poppins 10 bold", command=lambda: [copy_password(), show_copy_success_message()])  # Call update_on_slider_change on click
copy_button.grid(row=1, column=0, padx=(10), pady=(0, 10))  # Place the button below password label

# Regenerate Button
copy_button = tk.Button(password_frame, text="Regenerate", font="Poppins 10 bold", command=update_on_slider_change)  # Call update_on_slider_change on click
copy_button.grid(row=2, column=0, padx=(10), pady=(0, 14))  # Place the button below password label






label_slider_frame.pack()
label_checkbox_frame.pack()
background_frame.pack(expand=True, fill=tk.BOTH)
password_frame.pack()
update_on_slider_change()



#run
window.mainloop()

