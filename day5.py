#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Create a base password
password = ""

# Select random index for each of the letters requested
for x in range(0, nr_letters):
    ran_num = random.randint(0, len(letters) - 1)
    # Add letter to base password
    password += letters[ran_num]

# With symbols 
for x in range(0, nr_symbols):
    ran_num = random.randint(0, len(symbols) - 1)
    # Add letter to base password
    password += symbols[ran_num]

# With numbers
for x in range(0, nr_numbers):
    ran_num = random.randint(0, len(numbers) - 1)
    # Add letter to base password
    password += numbers[ran_num]

print(f"Here's an easy one: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ""
# Randomize each character in the easy password
for c in password:
    ran_num = random.randint(0, len(password) - 1)
    hard_password += password[ran_num]

print(f"Hard one: {hard_password}")

# NOTE: Can also use random.choice() and random.shuffle() to solve this.