# Program to change the font of the text
from tkinter import Tk, Message
root = Tk()
msg = Message(root, text = "Welcome to the course Object Oriented Programming using Python!")
msg.config(font=('Arial Black',24,'italic bold underline'))
msg.pack()
root.mainloop()



