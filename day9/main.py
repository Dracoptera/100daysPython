from replit import clear # Works in replit only
from art import logo
#HINT: You can call clear() to clear the output in the console.

bidders = {}
more = True

print(logo)

while more is True:
  bidder = input("What is your name? ")
  amount = int(input("What is your bid? $"))
  bidders[bidder] = amount
  decision = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if decision == "no":
    more = False
  elif decision == "yes":
    clear()

top_bidder = ""
max = 0

for k, v in bidders.items():
  if v > max:
    max = v
    top_bidder = k

print(f"The highest bidder is: {top_bidder}, with ${max}.")