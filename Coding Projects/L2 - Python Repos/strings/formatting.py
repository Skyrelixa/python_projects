# %, .format(), f-Strings

# OLD % FORMAT
var = "Tom"
mystring = "the variable is %s" % var

print(mystring)

var = 1
mystring = "the variable is %d" % var
print(mystring)

# floats only have 6 dec by default, so if we want to specify we can use %.2f or other nums
var = 3.1415926535
mystring = "the variable is %f" % var
print(mystring)

# NEW FORMAT COMMAND.
var = "Tom"
mystring = "the variable is {}".format(var)
print(mystring)

var = 1.1111111
mystring = "the variable is {:.2f}".format(var)
print(mystring)

# multiple vars
var2 = 6
mystring = "the variable is {} and {}".format(var, var2)
print(mystring)

# NEW F-STRING COMMAND. operates at runtime so you can also execute commands with floats and whatnot
var = 3.14159
var2 = 8
mystring = f"the variable is {var*2} and {var2}"
print(mystring)