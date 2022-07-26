# makes a list separated by spaces " "

mystring = 'how are you'
mylist = mystring.split(" ")
print(mylist)

# makes a string from a list, with spaces in between words
newstring = ' '.join(mylist)
print(newstring)