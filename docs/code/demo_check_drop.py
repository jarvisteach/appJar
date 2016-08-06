# http://stackoverflow.com/questions/29019760/how-to-create-a-combobox-that-includes-checkbox-for-each-item
from tkinter import *

master = Tk()

var = StringVar(master)
var.set("Check")
w = OptionMenu(master, variable = var, value="options:")
w.pack()
first = BooleanVar()
second = BooleanVar()
third = BooleanVar()
w['menu'].add_checkbutton(label="First", onvalue=True, offvalue=False, variable=first)
w['menu'].add_checkbutton(label="Second", onvalue=True, offvalue=False, variable=second)
w['menu'].add_checkbutton(label="Third", onvalue=1, offvalue=False, variable=third)


master.bind('<Button-3>', lambda x: print("First:", first.get(), " Second:", 
second.get(), " - Third:", third.get()))
mainloop()
