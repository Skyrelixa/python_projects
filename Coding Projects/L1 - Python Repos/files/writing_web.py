# creating a web page
file = open("files/index.html", "w") # r,w,a,r+, read write append readandwrite

file.write("<p>This is HTML</p>")

# we always have to close a file upon completion of using it
file.close()