from tkinter import *
root = Tk()

# disabling button
# myB = Button(root, text='Click me!', state=DISABLED)

# defining a function for the button
def Click():
    myLabel = Label(root, text='Look! You clicked me.')
    myLabel.pack()

# changing size of button and using def Click
myB = Button(root, text='Click me!', padx=50, pady = 50, command=Click, fg='blue', bg='black')
myB.pack()

root.mainloop()