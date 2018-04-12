import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn == "ONE": app.selectFrame("stack", 0)
    elif btn == "TWO": app.selectFrame("stack", 1)

with gui() as app:
    with app.frameStack("stack"):
        with app.frame():
            app.label("In frame one")
        with app.frame():
            app.label("In frame two")
    app.buttons(["ONE", "TWO"], press)
