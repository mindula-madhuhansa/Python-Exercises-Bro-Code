operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

if operator == "+":
    result = number1 + number2
    print(f"{number1} {operator} {number2} = {round(result, 3)}")
elif operator == "-":
    result = number1 - number2
    print(f"{number1} {operator} {number2} = {round(result, 3)}")
elif operator == "*":
    result = number1 * number2
    print(f"{number1} {operator} {number2} = {round(result, 3)}")
elif operator == "/":
    result = number1 / number2
    print(f"{number1} {operator} {number2} = {round(result, 3)}")
else:
    print("Enter a valid operator")
