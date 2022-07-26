my_list = ["banana", "cherry", "apple"]
print(my_list)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "apple"]
print(mylist3)
print(len(mylist3))

# demonstrating if involving a list
if "bana" in my_list:
    print("Yes")

else:
    print("No")

# demonstrating pop
item = my_list.pop()
print(item)
print(my_list)

# creating a new sorted list from my_list
my_list.append("apple")
new_list = sorted(my_list)
print(new_list)

# demonstrating list index
my_list = [0] * 5
print(my_list)

# concatenating lists
conc_list = my_list + mylist3
print(conc_list)