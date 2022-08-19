# Program to create a label as a child of the root window
from tkinter import Tk, Label
root = Tk()
msg = Label(root, text = "Welcome to the course Object Oriented Programming using Python!")
msg.pack()
root.mainloop()



