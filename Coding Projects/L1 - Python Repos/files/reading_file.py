# opening the file
employee_file = open("files\employees.txt", "r") # r,w,a,r+, read write append readandwrite

# making sure it's possible to read it
print(employee_file.readable())

# reading it ALL
# print(employee_file.read())

# reading one line at a time
# print(employee_file.readline()) x1
# print(employee_file.readline()) x2

# reading all the lines and putting in an array, then choosing lines from the array
# print(employee_file.readlines()[0:])

# reading all the lines from the array with a for loop
for employee in employee_file.readlines():
    print(employee)

# we always have to close a file upon completion of using it
employee_file.close()