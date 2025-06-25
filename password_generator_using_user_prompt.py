import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Function to get valid input
def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number.")

# Get inputs safely
nr_letters = get_number("How many letters would you like in your password?\n")
nr_symbols = get_number("How many symbols would you like?\n")
nr_numbers = get_number("How many numbers would you like?\n")

# Build password
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle and create final password
random.shuffle(password_list)
password = "".join(password_list)

print(f'Generated password: {password}')

