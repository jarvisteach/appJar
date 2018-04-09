import sys
sys.path.append("../../")

from appJar import gui 

def press(btn):
    if btn == "FIRST": app.firstFrame("Pages")
    elif btn == "NEXT": app.nextFrame("Pages")
    elif btn == "PREV": app.prevFrame("Pages")
    elif btn == "LAST": app.lastFrame("Pages")

with gui("FRAME STACK") as app:
    with app.frameStack("Pages"):
        with app.frame():
            for i in range(5):
                app.label("Text: " + str(i))
        with app.frame():
            for i in range(5):
                app.entry("e" + str(i))
        with app.frame():
            for i in range(5):
                app.button(str(i), None)

    app.buttons(["FIRST", "PREV", "NEXT", "LAST"], press)
