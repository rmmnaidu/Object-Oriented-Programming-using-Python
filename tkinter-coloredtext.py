# Program to print a colored text on a colored background of GUI window
from tkinter import Tk, Label
root=Tk()
label = Label(root, text = "Welcome to the course Object Oriented Programming using Python!")
label.pack()
label.config(foreground = 'yellow', background = 'green', text = 'Python current version is Python 3.10.6, Release date. Aug. 2, 2022')
root.mainloop()




