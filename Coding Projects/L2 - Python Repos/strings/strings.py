mystring = "Hello World" 
print(mystring)

# you can also create multiline strings. using a backslash keeps things on the same line
mystring = """Hello 
World"""
print(mystring)
mystring = """Hello \
World"""
print(mystring)

# removing large spaces at the ends of a string
string1 = '    Hello World    Ey    '
mystring = string1.strip()              # note: this needs an assgn. cannot just be string1.strip() on the line alone
print(mystring)

print(mystring.startswith('Hello'))     # can also use endswith()