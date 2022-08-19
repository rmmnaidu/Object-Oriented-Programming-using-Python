# Program to display a menu on the menu bar
from tkinter import Tk, Menu
root=Tk()
# Create main menu bar
menu_bar = Menu(root)
# Create the submenu, keeo tearoff denotes the menu can pop out
fileMenu = Menu(menu_bar, tearoff = 0)
# Add commands to submenu
fileMenu.add_command(label = 'Stop', command = root.destroy)
fileMenu.add_command(label = 'Kill', command = root.destroy)
fileMenu.add_command(label = 'Exit', command = root.destroy)
# Add the File drop down sub-menu in the main menu bar
menu_bar.add_cascade(label = "File", menu = fileMenu)
root.config(menu = menu_bar)
root.mainloop()




