import sys
sys.path.append("../")
from appJar import gui

def press():
    app.radio("song", "Paradise City", selected=True, bg="pink")

def change():
    print(app.radio("song"))

with gui() as app:
    app.radio("song", "Killer Queen", bg="red")
    app.radio("song", "Paradise City")
    app.radio("song", "a")
    app.radio("song", "b")
    app.radio("song", "c", change=change)
    app.button("PLAY", press)
