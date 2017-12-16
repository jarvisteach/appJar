import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    val = app.popUp("a", "b", btn)
    print(val)
    app.label("title", bg="red")

def press2(btn):
    val = app.prompt("a", "b", btn)
    print(val)

def press3(btn):
    print(btn)

with gui("Simple Demo") as app:
    app.label("title", "TOOLTIP & MENU", bg="green", fg="blue", column=0, row=0, tooltip="some info", menu=True)
    app.label("title2", "SUBMIT", bg="red", fg="white", column=1, row=0, submit=press)
    app.label("title3", "CHANGE & OVER", bg="orange", fg="black", column=0, row=1, over=[press3, press3], change=press)
    app.label("title4", "DRAG & DROP", bg="pink", fg="yellow", column=1, row=1, drop=True, drag=(press3, press3))
    app.label("title5", "FLASH", kind="flash", column=0, row=2, bg="orange", drop=True, drag=press2)
    app.label("title6", "SELECTABLE", kind="selectable", column=1, row=2, bg="green", drop=True)
    app.addButtons(["info", "error", "warning", "yesno", "question", "ok", "retry"], press, colspan=2)
    app.addButtons(["string", "integer", "float", "text", "number", "junk"], press2, colspan=2)
