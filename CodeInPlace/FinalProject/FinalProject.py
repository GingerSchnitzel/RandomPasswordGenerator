import random
import string
import tkinter as tk
from tkinter import ttk


"""
def get_password_length():
  while True:
    length = input("Enter password length: ")
    try:
      length = int(length)
    except ValueError:
      print("Invalid input for the length of the password. Please try again.")
      continue
    if length < 8:
        print("Password minimum length is 8 characters. Please try again.")
        continue
    
    return length
"""

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

# Generates a password with current values
def update_on_slider_change(event= None):
  
  generated_password = generate_password(
      password_length.get(),
      use_uppercase_letters.get(),
      use_lowercase_letters.get(),
      use_numbers.get(),
      use_symbols.get(),
  )  

  # Update password label with generated password
  password_label.config(text=generated_password)

# Window
window = tk.Tk()
window.title("Code In Place Final Project")
window.geometry("600x400")

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
length_label.grid(row=0, column=0, padx = (0, 178), pady=(14,5))  # Place within the frame

# Password length slider
password_length = tk.IntVar(value=8)
length_slider = tk.Scale(label_slider_frame, from_=1, to=50, orient=tk.HORIZONTAL, variable=password_length, command=update_on_slider_change)
length_slider.grid(row=0, column=0, padx = (240,0), pady=(0,6))  # Place within the frame


# Checkboxes and label variables (checkboxes will be checkd by default)
use_uppercase_letters = tk.IntVar(value=1) 
use_lowercase_letters = tk.IntVar(value=1)
use_numbers = tk.IntVar(value=1)
use_symbols = tk.IntVar(value=1)

# Frame to hold checkboxes and their labels
label_checkbox_frame = tk.Frame(master=background_frame, background = "lightgreen")

# Checkbox creation
uppercase_label = tk.Label(label_checkbox_frame, text="Include Uppercase Letters?", font ="Poppins 12")
uppercase_label.grid(row=0, column=0, padx = (0, 102), pady=(5,5))

uppercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_uppercase_letters, command=update_on_slider_change)
uppercase_checkbox.grid(row=0, column=0, padx = (245,0), pady=(6,5))

lowercase_label = tk.Label(label_checkbox_frame, text="Include Lowercase Letters?", font ="Poppins 12")
lowercase_label.grid(row=1, column=0, padx = (0, 105), pady=(5,5))

lowercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_lowercase_letters, command=update_on_slider_change)
lowercase_checkbox.grid(row=1, column=0, padx = (245,0), pady=(6,5))

numbers_label = tk.Label(label_checkbox_frame, text="Include numbers?", font ="Poppins 12")
numbers_label.grid(row=2, column=0, padx = (0, 176), pady=(5,5))

numbers_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_numbers, command=update_on_slider_change)
numbers_checkbox.grid(row=2, column=0, padx = (245,0), pady=(6,5))

symbols_label = tk.Label(label_checkbox_frame, text="Include symbols?", font ="Poppins 12")
symbols_label.grid(row=3, column=0, padx = (0, 180), pady=(5,5))

symbols_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_symbols, command=update_on_slider_change)
symbols_checkbox.grid(row=3, column=0, padx = (245,0), pady=(6,5))

'''
# Generate password with retrieved values
current_password_length = password_length.get()
generated_password = generate_password(current_password_length, use_uppercase_letters, use_lowercase_letters, use_numbers, use_symbols)
print(current_password_length)
'''
# Frame to hold generated password
password_frame = tk.Frame(master=background_frame, background = "lightgrey")
# Label for password
password_label = tk.Label(password_frame, font="Poppins 16 bold")
password_label.grid(row = 0, column = 0, padx = 0, pady =(20, 20))  # Pack the label at the bottom


label_slider_frame.pack()
label_checkbox_frame.pack()
background_frame.pack(expand=True, fill=tk.BOTH)
password_frame.pack()
update_on_slider_change()



#run
window.mainloop()

