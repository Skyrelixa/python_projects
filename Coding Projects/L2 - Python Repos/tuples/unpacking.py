mytuple = "Max", 28, "Boston"

name, age, city = mytuple
print(name)
print(age)
print(city)

mytuple = 0,1,2,3,4

i1, *i2, i3 = mytuple
print(i1)               # first item in the tuple
print(i3)               # second item in the tuple
print(i2)               # all items in between i1 and i3, shown as a LIST