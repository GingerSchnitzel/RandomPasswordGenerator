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

#generates a password of a customizable length which can include (or not) uppercase and/or lowercase letters, numbers and symbols
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
    

#window
window = tk.Tk()
window.title("Code In Place Final Project")
window.geometry("800x500")

#Canvas frame which adds padding between the window and title
padding_frame = tk.Frame(master = window, padx=10, pady=10)


#title
title_label = ttk.Label(master = padding_frame, text = "Random Password Generator", font ="Poppins 22 bold" )
title_label.pack(pady = 10)
padding_frame.pack()

# Frame to hold label and slider
label_slider_frame = tk.Frame(master = window)


# Label for password length
length_label = tk.Label(master = window, text="Password Length:",font ="Poppins 12" )


# Password length slider
password_length = tk.IntVar()
length_slider = tk.Scale(master = window, from_=1, to=50, orient=tk.HORIZONTAL, variable=password_length)
length_label.pack(side="left", padx= 10, pady = 12.5)
length_slider.pack(side="left")  
label_slider_frame.pack()








#run
window.mainloop()

