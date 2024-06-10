import random
import string
import tkinter as tk
from tkinter import ttk
import clipboard 
from ttkthemes import ThemedStyle


# Generates a password of a customizable length which can include (or not) uppercase and/or lowercase letters, numbers and symbols
def generate_password(length, include_upper, include_lower, include_numbers, include_symbols):
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
    clipboard.copy(password_label.cget("text"))  # Copy current password

def show_password():
    password_label.grid(row = 0, column = 0, padx = 0, pady =(20, 10)) 
    copied_label.grid_forget()

def show_copy_success_message(): 
    password_label.grid_forget()
    copied_label.grid(row = 0, column = 0, padx = 0, pady =(20, 10))

    # Schedule update function after 1.5 second 
    window.after(1500, show_password)

def toggle_night_mode(): 
    if turned_on.get():
        apply_theme(dark_theme)
    else:
        apply_theme(light_theme)

def apply_theme(theme):
 
    for frame in [background_frame, title_frame, label_slider_frame, label_checkbox_frame, password_frame, copy_regenerate_buttons_frame, night_mode_frame, uppercase_checkbox, lowercase_checkbox, numbers_checkbox, symbols_checkbox, night_mode_checkbox]:
        frame.configure(background=theme['background'])

    for label in [title_label, length_label, uppercase_label, lowercase_label, numbers_label, symbols_label, night_mode_label, password_label, copied_label]:
        label.configure(background=theme["background"])
        label.configure(foreground=theme["text"])

    for button in [minus_button, plus_button, copy_button, regenerate_button]:
        button.configure(background=theme['TButton'], foreground=theme['text'], highlightbackground=theme['background'])

    length_slider.configure(background=theme["background"],foreground=theme["text"], highlightbackground=theme['background'] )



# Window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("760x620")

# Define style
style = ThemedStyle(window)

dark_theme = {
    "background": "#282828",  
    "text": "#FFFFFF",        
    "TLabel": "#FFFFFF",  
    "TButton": "#777777"
}

light_theme = {
    "background": "#F0F0F0",  
    "text": "#000000",        
    "TLabel": "#000000",  
    "TButton": "#C9C9C9"
}

# Background frame
background_frame = tk.Frame(master=window)

# Frame which contains the title
title_frame = tk.Frame(master=background_frame)

# Title
title_label = ttk.Label(master=title_frame, text="Random Password Generator", font="Poppins 22 bold")
title_label.grid(row=0, column=0, padx=60, pady=(16, 18), sticky="nsew")


# Frame to hold label and slider
label_slider_frame = tk.Frame(master=background_frame)

# Label for password length
length_label = tk.Label(label_slider_frame, text="Password Length:", font="Poppins 12")
length_label.grid(row=0, column=0, padx=(0, 298), pady=(14, 5))  # Place within the frame

# Minus button
def decrease_slider_value():
    current_value = password_length.get()
    if current_value > 1: 
        password_length.set(current_value - 1)
        update_on_slider_change()  # Trigger update

minus_button = tk.Button(label_slider_frame, text="-", command=decrease_slider_value)
minus_button.grid(row=0, column=0, padx=(128, 0), pady=(16, 0))  # Place next to slider

# Password length slider
password_length = tk.IntVar(value=8)
length_slider = tk.Scale(label_slider_frame, from_=1, to=50, font="Poppins 9", orient=tk.HORIZONTAL, variable=password_length, command=update_on_slider_change)
length_slider.grid(row=0, column=0, padx=(272, 0), pady=(0, 6))  # Place within the frame

# Plus button
def increase_slider_value():
    current_value = password_length.get()
    password_length.set(current_value + 1)
    update_on_slider_change()  # Trigger update

plus_button = tk.Button(label_slider_frame, text="+", command=increase_slider_value)
plus_button.grid(row=0, column=0, padx=(420, 0), pady=(15, 1))  # Place next to slider

# Checkboxes and label variables (checkboxes will be checked by default)
use_uppercase_letters = tk.IntVar(value=1) 
use_lowercase_letters = tk.IntVar(value=1)
use_numbers = tk.IntVar(value=1)
use_symbols = tk.IntVar(value=1)

# Frame to hold checkboxes and their labels
label_checkbox_frame = tk.Frame(master=background_frame)

# Checkbox creation
uppercase_label = tk.Label(label_checkbox_frame, text="Include Uppercase Letters?", font="Poppins 12")
uppercase_label.grid(row=0, column=0, padx=(0, 222), pady=(5, 5))

uppercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_uppercase_letters, command=update_on_slider_change)
uppercase_checkbox.grid(row=0, column=0, padx=(276, 0), pady=(6, 5))

lowercase_label = tk.Label(label_checkbox_frame, text="Include Lowercase Letters?", font="Poppins 12")
lowercase_label.grid(row=1, column=0, padx=(0, 225), pady=(5, 5))

lowercase_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_lowercase_letters, command=update_on_slider_change)
lowercase_checkbox.grid(row=1, column=0, padx=(276, 0), pady=(6, 5))

numbers_label = tk.Label(label_checkbox_frame, text="Include numbers?", font="Poppins 12")
numbers_label.grid(row=2, column=0, padx=(0, 296), pady=(5, 5))

numbers_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_numbers, command=update_on_slider_change)
numbers_checkbox.grid(row=2, column=0, padx=(276, 0), pady=(6, 5))

symbols_label = tk.Label(label_checkbox_frame, text="Include symbols?", font="Poppins 12")
symbols_label.grid(row=3, column=0, padx=(0, 300), pady=(5, 5))

symbols_checkbox = tk.Checkbutton(label_checkbox_frame, variable=use_symbols, command=update_on_slider_change)
symbols_checkbox.grid(row=3, column=0, padx=(276, 0), pady=(6, 5))

# Frame to hold generated password
password_frame = tk.Frame(master=background_frame)

# Label for password
password_label = tk.Label(password_frame, font="Poppins 16 bold")
password_label.grid(row=0, column=0, padx=0, pady=(20, 30))  # Pack the label at the bottom

# Label for "Password copied successfully!"
copied_label = tk.Label(password_frame, text="Password copied successfully!", font="Poppins 16 bold")

# Copy and regenerate buttons frame
copy_regenerate_buttons_frame = tk.Frame(master=background_frame)

# Copy Button
copy_button = tk.Button(copy_regenerate_buttons_frame, text="Copy", font="Poppins 10 bold", command=lambda: [copy_password(), show_copy_success_message()])  # Call update_on_slider_change on click
copy_button.grid(row=1, column=0, padx=(10), pady=(0, 10))  # Place the button below password label

# Regenerate Button
regenerate_button = tk.Button(copy_regenerate_buttons_frame, text="Regenerate", font="Poppins 10 bold", command=update_on_slider_change)  # Call update_on_slider_change on click
regenerate_button.grid(row=2, column=0, padx=(10), pady=(0, 14))  # Place the button below password label

copy_regenerate_buttons_frame.rowconfigure(1, weight=1)
copy_regenerate_buttons_frame.columnconfigure(1, weight=1)

# Frame to hold night_mode label and checkbox
night_mode_frame = tk.Frame(master=background_frame)

turned_on = tk.IntVar()
night_mode_label = tk.Label(night_mode_frame, text="Dark Mode", font="Poppins 9")
night_mode_label.grid(row=0, column=0, padx=340, pady=(20, 0))

night_mode_checkbox = tk.Checkbutton(night_mode_frame, variable=turned_on, command=toggle_night_mode)
night_mode_checkbox.grid(row=1, column=0 , pady=(0, 6))


title_frame.pack()
label_slider_frame.pack()
label_checkbox_frame.pack()
background_frame.pack(expand=True, fill=tk.BOTH)
password_frame.pack()
copy_regenerate_buttons_frame.pack()
update_on_slider_change()
night_mode_frame.pack()

# Run the application
window.mainloop()
