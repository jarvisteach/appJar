import sys
sys.path.append("../../")
from appJar import gui

def launcher(btn):
    app.showSubWindow(btn)

with gui("Quiz Demo") as app:
    app.buttons(["Quiz", "Scores"], launcher)

    with app.subWindow("Quiz", modal=True):
        app.label("Quiz")

    with app.subWindow("Scores", modal=True):
        app.label("Scores")
