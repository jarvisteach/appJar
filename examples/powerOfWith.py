import sys
sys.path.append("../")

from appJar import gui
with gui("My first GUI") as app:

    app.setBg("lightblue")

    with app.labelFrame("Left"):
        app.addLabel("left", "Hello world!")

    with app.abelFrame("Right", row=0, column=1):
        app.addLabel("right", "Hello world again!")

    app.addNamedButton("PRESS ME", "Pop-up", app.showSubWindow, colspan=2)

    with app.subWindow("Pop-up"):
        app.addLabel("popLab", "Here's a pop-up!")
