from tkinter import *
root = Tk()

# could also use .grid() at end of Label func
myLabel = Label(root, text='This is a positioned widget.')
myL2 = Label(root, text ='Neat, right?')
myLabel.pack()

myLabel.grid(row=0,column=0)
myL2.grid(row=1,column=0)
root.mainloop()