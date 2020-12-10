import art

def add(n1, n2):
  """Add"""
  return n1 + n2

def substract(n1, n2):
  """Substract"""
  return n1 - n2

def multiply(n1, n2):
  """Multiply"""
  return n1 * n2

def divide(n1, n2):
  """Divide"""
  return n1 / n2

operations = {
"+":  add, 
"-": substract, 
"*": multiply, 
"/": divide
}

print(art.logo)

def calculator():
    rerun = True

    num1 = float(input("What's the first number? "))

    while rerun == True:
        for k in operations:
            print(k)

        selection = input("Pick an operation from the list above: ")
        while selection not in operations:
            selection = input("Please select a valid calculation: ")

        num2 = float(input("What's the next number? "))

        result = operations[selection](num1, num2)

        print(f"{num1} {selection} {num2} = {result}")

        restart = input(f"Type 'y' to continue calculating with {result}, or type anything else to start a new calculation: ")

        if restart != "y":
            rerun = False
            calculator()
        else:
            num1 = result

calculator()