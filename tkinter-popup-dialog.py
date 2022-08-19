# Program to display a pop-up dialog box
from tkinter import messagebox
title = "Student End Semester Feedback"
text = "The overall quality of teaching-learning process in your institute is very good, do you agree?"
reply = messagebox.askquestion(title, text)
if reply == 'yes':
    print("Congratulations for choosing our institute..")
else:
    print("Next year onwards more efforts for improving teaching-learning process..")
