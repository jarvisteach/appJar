import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "FIRST": app.firstFrame("fs")
    elif btn == "NEXT": app.nextFrame("fs")
    elif btn == "PREV": app.prevFrame("fs")
    elif btn == "LAST": app.lastFrame("fs")
    elif btn == "SETFRAME": app.selectFrame("fs", app.option(btn))

with gui("FRAME STACK", bg='pink') as app:
    with app.frameStack("fs", bg='black'):
        with app.frame(bg='red', sticky='news', stretch='both'):
            app.configure(expand='both')
            app.label("1", bg=app.RANDOM_COLOUR())
            for x in range(10): app.radio("A", str(x))
        with app.frame(bg='orange'):
            app.label("2", bg=app.RANDOM_COLOUR())
            for x in range(10): app.button(str(x))
        with app.frame(bg='yellow'):
            app.label("3", bg=app.RANDOM_COLOUR())
            for x in range(10): app.check(str(x), bg=app.RANDOM_COLOUR(), stretch='both', sticky='news')
    with app.frameStack("fs"):
        with app.frame(bg='green'):
            app.label("4", bg=app.RANDOM_COLOUR())
            for x in range(10): app.option(str(x), [x])
        with app.frame(bg='blue'):
            app.label("5", bg=app.RANDOM_COLOUR())

    app.buttons(["FIRST", "PREV", "NEXT", "LAST"], press)
    app.option("SETFRAME", range(app.countFrames("fs")), change=press)
    with app.frame("aaa", bg="green"):
        app.label("AGAIN")
    app.label("AND AGAIN, AGAIN")

    with app.frame("fs__1"):
        app.label("SUPER NEWBIE")

    with app.frame("aaa"):
        app.label("AND AGAIN")
