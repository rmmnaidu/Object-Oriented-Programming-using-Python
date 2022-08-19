# Program to display two buttons and print a message when a button is clicked
from tkinter import Tk, Button
root=Tk()
#Exit window will close the GUI window when clicked
exitButton = Button(root, text = 'Exit Program', command = root.destroy)
exitButton.pack()
#To write a message on the screen and not on GUI window
def my_callback():
    print("You clicked the Message Button..")
msg_button = Button(root, text = 'Click Here', command = my_callback)
msg_button.pack()
root.mainloop()




