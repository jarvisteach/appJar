import sys
sys.path.append("../")
from appJar import gui

def press():
    print(app.radio("song"))
    app.radio("song", "Paradise City", selected=True, bg="pink")

with gui() as app:
    app.radio("song", "Killer Queen", bg="red")
    app.radio("song", "Paradise City")
    app.radio("song", "a")
    app.radio("song", "b")
    app.radio("song", "c", change=press)
    app.button("PLAY", press)
