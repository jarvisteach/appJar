import sys
sys.path.append("../../")
from tkinter import font as tkFont
from appJar import gui

with gui() as app:
    app.label('hello world')
    app._statusFont = tkFont.Font(family="Helvetica", size=20)
    app.status(text="hello world", bg='red')
