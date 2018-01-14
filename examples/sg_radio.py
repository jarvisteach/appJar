import sys
sys.path.append("../")
from appJar import gui

def press():
    print(app.getRadioButton("song"))

with gui() as app:
    app.radio("song", "Killer Queen", change=press, bg="red")
    app.radio("song", "Paradise City")
    app.button("PLAY", press)
