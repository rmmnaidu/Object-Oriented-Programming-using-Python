# Program to create a top-level window which will be closed when the button is clicked
from tkinter import Tk, Toplevel, Button
root = Tk()
# Create new top level window
top_level_window = Toplevel()
top_level_window.title('Top Level Window')
# Destroy Top Level Window - window
def destroy_top_level_window():
    top_level_window.destroy()
closeButton = Button(root, text = 'Close Top Level Window', command = destroy_top_level_window)
closeButton.pack()
root.mainloop()
