# Program to put focus on top-level window
from tkinter import Tk, Toplevel
root = Tk()
top_level_window = Toplevel()
top_level_window.title('New Top Level Window')
# Focus on window
top_level_window.focus_force()
root.mainloop()
