# importing mathematic functions
# does not include abs, pow, max, min, round
from math import *

# functs not used by lib: floor, ceil, sqrt

# basic arithmetic
print(-2.09)
print(3+4.05)                   # expecting 7.05
print((3*(4+5)) %2)             # expecting 1

# converting to a string
print(str(2) + " is cool")

# obtaining the absolute val of a number
numb = -5
print(abs(numb))

# determining the power of a number
# params num, exp
print(pow(3,2))                 # expecting a 9

# max function which returns the larger number. min also a funct
num1 = 2
num2 = 6
print(max(num1, num2))

# rounding
print(round(3.45))