#! /home/codespace/.python/current/bin/python3
instructions = """
Welcome to the Calculator Program!
Instructions:
1. Prepare two desired numbers for calculation and be ready to input
2. Choose the desired calculation action
3. Enjoy with the results
"""

print(instructions)

while True:
    try:
        number1 = float(input("Please enter the first number:"))
        print("Your first number is: {0:g}".format(number1))
    except ValueError:
        print("Error: Invalid input type. Please enter numeric values.")
        continue
    break

while True:
    try:
        number2 = float(input("Please enter the second number:"))
        print("Your second number is: {0:g}".format(number2))

    except ValueError:
        print("Error: Invalid input type. Please enter numeric values.")
        continue
    break


select = """
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""

choices = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",   
    4: "Division"
}


while True:
    try:
        choice = int(input("Enter your choice (1-4):"))
        if choice < 1 or choice > 4:
            raise ValueError("Wrong input value")
        print("Your choice is: {}. {}". format(choice, choices[choice]))
        break # Break out of the loop if the input is valid

    except ValueError as ve:
        if str(ve) == "Wrong input value":
            print("Error: Wrong input value. Please enter a number from 1 to 4.")
        else:
            print("Error: Invalid input type. Please enter numeric values.")
        continue


  

if choice == 1:
    result = number1 + number2
elif choice == 2:
    result = number1 - number2
elif choice == 3:
    result = number1 * number2
elif choice == 4:
    if number2 != 0:  # Handle division by zero
        result = number1 / number2
    else:
        print("Error: Division by zero is not allowed.")
        exit(1)


print("\nThe result of the operation is: {0:g}".format(result))
