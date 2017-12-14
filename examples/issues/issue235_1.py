import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    val = app.popUp("a", "b", btn)
    print(val)

def press2(btn):
    val = app.prompt("a", "b", btn)
    print(val)

with gui("Simple Demo") as app:
    app.label("title", "hello world", bg="green", fg="blue", column=0, row=0, tooltip="some info", menu=True)
    app.label("title2", "hello world", bg="red", fg="white", column=1, row=0, submit=press)
    app.label("title3", "hello world", bg="orange", fg="black", column=0, row=1)
    app.label("title4", "hello world", bg="pink", fg="yellow", column=1, row=1)
    app.addButtons(["info", "error", "warning", "yesno", "question", "ok", "retry"], press, colspan=2)
    app.addButtons(["string", "integer", "float", "text", "number", "junk"], press2, colspan=2)
