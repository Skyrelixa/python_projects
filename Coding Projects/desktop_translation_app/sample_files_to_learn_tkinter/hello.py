# these need to happen b4 any Tkinter program starts
from tkinter import *
root = Tk()

# Creating a Label Widget
myLabel = Label(root, text='Hello World')
# Shoving it on to the screen
myLabel.pack()

root.mainloop()