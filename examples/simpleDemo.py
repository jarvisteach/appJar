import sys
sys.path.append("../")

from appJar import gui

def press(btnName):
    app.popUp("INFO", "You pressed " + btnName)

def update(value):
    if value == "list": app.slider("slider", app.listbox(value)[0])
    elif value == "slider": app.listbox("list", app.slider(value))
    app.label("display", app.listbox("list")[0])

with gui("Version 1.0", bg="teal") as app:
    app.label("Version 1.0 Demo", colspan=2, bg="red")
    with app.labelFrame("Big Buttons", colspan=2, sticky="news", expand="both"):
        app.button("BUTTON A", press)
        app.button("BUTTON B", press)
        app.button("BUTTON C", press)
    app.listbox("list", [1, 2, 3, 4, 5], rows=5, selected=0, submit=update)
    app.label("display", "1", row=2, column=1, bg="yellow", sticky="news")
    app.slider("slider", colspan=2, range=(1,5), change=update, interval=1)
