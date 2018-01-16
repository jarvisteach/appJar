import sys
sys.path.append("../")
from appJar import gui

def press():
    print("STARTING setter")
    app.radio("song", "Paradise City", selected=True, bg="pink", callFunction=False)
    print("ENDING setter")

def change():
    print("in changer")
    print(app.radio("song"))

with gui() as app:
    app.radio("song", "Killer Queen", bg="red")
    app.radio("song", "Paradise City")
    app.radio("song", "a", bg="green", fg="yellow")
    app.radio("song", "b")
    app.radio("song", "c", change=change)
    app.button("PLAY", press)
