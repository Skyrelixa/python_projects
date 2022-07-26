try:
    # value = 10/0 # >> if except has no params, this will produce "Invalid Input"
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")