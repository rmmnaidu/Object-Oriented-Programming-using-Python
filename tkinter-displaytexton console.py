# Program to display the text on the console when a label is pressed
from tkinter import Tk, Label
root=Tk()
label = Label(root, text = 'Message Printing label..')
label.pack()
def my_callback():
    print("GUI Programming with tkinter package in Python..")
# Bind left mouse button clicl on label
label.bind("<Button-1>", lambda e:my_callback())
root.mainloop()




