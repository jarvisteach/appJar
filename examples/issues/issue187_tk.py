import os
from tkinter import *
from tkinter import ttk
tk = Tk()

ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
ttk.Style().configure('green/black.TButton', foreground='green', background='black')
ttk.Style().configure('green/black.TRadiobutton', foreground='green', background='black')


lab = ttk.Label(tk, text="Testing FG/BG Setting", style='green/black.TLabel')
b = ttk.Button(tk, text="Expand", style='green/black.TButton')
cb = ttk.Checkbutton(tk, text="Expand")
rb = ttk.Radiobutton(tk, text="Expand", style='green/black.TRadiobutton')

lab.pack()
cb.pack()
rb.pack()
b.pack()

tk.wm_attributes("-topmost", 1)
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
mainloop()
