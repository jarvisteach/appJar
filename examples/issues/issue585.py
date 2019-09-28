import sys
sys.path.append("../../")

from appJar import gui

def press():
    app.thread(app.reloadImage, "q", "./bStar.png")

with gui() as app:
    app.label('hello world')
    app.addImage("q", "./bStar.png")
    app.button('PRESS', press)
