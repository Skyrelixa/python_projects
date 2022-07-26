# opening the file
employee_file = open("files\employees.txt", "a") # r,w,a,r+, read write append readandwrite

employee_file.write("\nToby - Human Resources")

# we always have to close a file upon completion of using it
employee_file.close()

# creating a new file
employee_file = open("files\employees.txt1", "w") # r,w,a,r+, read write append readandwrite

employee_file.write("\nToby - Human Resources")

# we always have to close a file upon completion of using it
employee_file.close()