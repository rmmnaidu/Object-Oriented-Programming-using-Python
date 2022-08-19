# Program to print the screen size
from tkinter import Tk
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen Width:",screen_width)
print("Screen Height:",screen_height)
'''
OUTPUT:
Screen Width: 1366
Screen Height: 768
'''


