
import random
import string

def get_password_length():
  while True:
    length = input("Enter password length: ")
    # Try converting the input to an integer
    try:
      length = int(length)
      # If conversion is successful, check if it's at least 8 characters
    except ValueError:
      # Handle the case where conversion fails (non-numeric input)
      print("Invalid input for the length of the password. Please try again.")
      continue
    if length < 8:
        print("Password minimum length is 8 characters. Please try again.")
        continue
    
    return length


def generate_password (length=8, include_upper=True, include_lower=True, include_numbers=True, include_symbols= True):
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
    

    


def main():
    password = generate_password()
    print(password)

if __name__ == '__main__':
    main()
