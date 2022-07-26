import math

def calculator():   
    operation = input("Please enter the type of operation you'd like to perform: ").upper()
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

# note: because we used return here, "else" will return None with Invalid. Remove this 
# occurrence by not asking the function to return any values. In other words, print(num1+num2) and so on.
    if operation == "MULTIPLICATION":
        return num1*num2
    elif operation == "DIVISION":
        return num1/num2
    elif operation == "ADDITION":
        return num1+num2
    elif operation == "SUBTRACTION":
        return num1 - num2
    else:
        print("Invalid.")

print(calculator())
