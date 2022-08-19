# Program to display two labels with different colored background
from tkinter import Tk, Label, Y, RIGHT
root = Tk()
label1 = Label(root, text = "Welcome to the course:", background = 'green')
label2 = Label(root, text = "Object Oriented Programming using Python!", background = 'yellow')
label1.pack(fill = Y, padx = 10, ipady = 25, side = RIGHT)
label2.pack(fill = Y, padx = 20, ipady = 40, side = RIGHT)
root.mainloop()



