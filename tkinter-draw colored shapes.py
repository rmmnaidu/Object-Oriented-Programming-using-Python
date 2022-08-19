# Program to put focus on top-level window
from tkinter import Tk, Canvas
root = Tk()
canvas = Canvas(root, width = 250, height = 200)
canvas.pack()
# Draw orange dashed line
canvas.create_line(0, 0, 250, 250, fill = 'orange', dash = (5, 15))
# Draw yellow rectangle at (100, 50) to (150, 60)
canvas.create_rectangle(100, 50, 150, 60, fill = 'yellow')
# Draw Oval(circle)from (30, 30) to (50, 50)
canvas.create_oval(30, 30, 50, 50, fill = 'green')
root.mainloop()
