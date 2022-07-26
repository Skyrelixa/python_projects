# fun fact: tuples do not actually need parentheses
mytuple = "Max", 28, "Boston"

print(mytuple)

# tuples will not be recognized as a tuple with one element (instead as a str), unless...
# included comma
# included type() to verify tuple
mytuple = ("Max",)
print(type(mytuple))

# you can also use the tuple() function to create a tuple from a list
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# and vice versa:
my_list = list(mytuple)
print(my_list)

# demonstrating index
item = mytuple[0:]
print(item)

# what if we want to change the elements of the tuple?
# mytuple[0] = "Tim"  # produces an error. not possible

# iterable access
for i in mytuple:
    print(i)
