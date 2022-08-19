# Program that has an entry box in which the message entered by user is printed on the IDLE screen
from tkinter import Tk, Entry,Button, INSERT
root=Tk()
# Create an entry box
entry = Entry(root)
entry.pack()
# Print the contents of entry box in console
def printMsg():
    print(entry.get())
# Create a button that when clicked will print the contents of the entry box
button = Button(root, text = 'Print content', command = printMsg)
button.pack()
root.mainloop()




