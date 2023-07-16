from tkinter import *
from tkinter import ttk
import tkinter.font as font
import roll

window = Tk()

# Dice sides selection
sides = IntVar(value=10)

entry = ttk.Entry(window,width=10,textvariable=sides)
scale = Scale(window, from_=2, to=100, width=20, orient="horizontal", variable=sides)

entry.place(relx=0.3, rely=0.7, anchor=CENTER)
scale.place(relx=0.3, rely=0.82, anchor=CENTER)

# Dice amount selection
dice = IntVar(value=10)

entry2 = ttk.Entry(window,width=10,textvariable=dice)
scale2 = Scale(window, from_=1, to=100, width=20, orient="horizontal", variable=dice)

entry2.place(relx=0.7, rely=0.7, anchor=CENTER)
scale2.place(relx=0.7, rely=0.82, anchor=CENTER)

# Roll total text

d_txt = 0

# Dice roll method
def d_roll():
    results = roll.roll(dice.get(), sides.get())
    rolls = results[0]
    total = results[1]
    d_txt = total
    roll_button.config(text=d_txt)

# Dice total button
d_img = PhotoImage(file="d6.png")
txtFont = font.Font(size=30, weight="bold")
roll_button = Button(window, text=d_txt, font=txtFont, image=d_img, compound="center", command=d_roll)
roll_button.place(relx=0.5, rely=0.3, anchor=CENTER)

# Window details
window.title('dInfinity | Dice Roll')
window.geometry("500x500")

window.mainloop()