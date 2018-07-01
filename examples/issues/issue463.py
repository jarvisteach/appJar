import sys
sys.path.append("../../")
from tkinter import font as tkFont
from appJar import gui

with gui() as app:
    app.label('hello world')
    print(app.statusFont)
    app.statusFont = tkFont.Font(family="Helvetica", size=20)
    print(app.getStatusFont())
    app.setStatusFont(40)
    print(app.statusFont)
    app.status(text="hello world", bg='red')
