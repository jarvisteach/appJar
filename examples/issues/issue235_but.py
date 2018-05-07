import sys
sys.path.append("../../")

from appJar import gui

def change(btn):
    print(btn, "change")

def submit(btn):
    print(btn, "submit")

def drop(btn):
    print(btn, "drop")

def press(btn):
    print(btn)
    app.button("PRESS", bg="red")
    

with gui("Button Demo") as app:
    app.button("PRESS", press, fg="yellow", over=change)
    app.button("PRESSer", press, 2, 0, 1)
    app.button("PRESS2", press, name="SPECIAL NAME")
    app.button("PRESS3", press, icon="OPEN", align="top", fg="green", bg="yellow")
    app.button("PRESS4", press, image="map.gif", fg="yellow", over=change, stretch="BOTH")
