try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Give the operation you want to perform: \n1. + Addition\n2. - Subtraction\n3. * Multiplication\n4. \\ Division")

    opertaion = input("Enter the operation: ")

    match opertaion:
        case "+":
            print(f"The sum of {a} and {b} is {a + b}")
        case "-":
            print(f"The difference of {a} and {b} is {a - b}")
        case "*":
            print(f"The product of {a} and {b} is {a * b}")
        case "/":
            if b != 0:
                print(f"The division of {a} by {b} is {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")

except ValueError:
    print("Invalid input. Please enter a valid number.")    