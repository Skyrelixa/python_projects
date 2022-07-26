list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list[1:5]
print(a)

# step index
a = list[::1]
print(a)

a = list[::-1]
print(a)


list_org = ["banana", "cherry", "apple"]
list_cpy = list_org # note: if you now modify cpy, it will also modify org. they are assigned as "the same"

# using copy function to avoid the above error:
list_cpy = list_org.copy()    # can also be written as "list_cpy = list(list_org)" OR "list_cpy = list_org[:]"
list_cpy.append("lemon")

print(list_org)
print(list_cpy)
