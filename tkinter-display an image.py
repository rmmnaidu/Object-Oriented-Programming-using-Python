# Program to display an image
from tkinter import Tk, Label, PhotoImage
root=Tk()
img=PhotoImage(file='oopdesign1.png')
IMG=Label(root,image=img)
IMG.pack()
root.mainloop()




