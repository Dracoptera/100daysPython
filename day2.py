"""A simple tip calculator"""

print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10, 12 or 15? "))
people = int(input("How many people will split the bill? "))

total_tip = total * percentage / 100 
ind_amount = (total + total_tip) / people

print(f"Each person will pay: {round(ind_amount, 2)}")