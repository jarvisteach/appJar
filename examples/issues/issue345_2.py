import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "FIRST": app.firstSubFrame("fs")
    elif btn == "NEXT": app.nextSubFrame("fs")
    elif btn == "PREV": app.prevSubFrame("fs")
    elif btn == "LAST": app.lastSubFrame("fs")
    elif btn == "SETFRAME": app.selectSubFrame("fs", app.option(btn))

with gui("FRAME SET", bg='pink') as app:
    with app.frameSet("fs", bg='black'):
        with app.subFrame(bg='red', sticky='news', stretch='both'):
            app.configure(expand='both')
            app.label("1", bg=app.RANDOM_COLOUR())
            for x in range(10): app.radio("A", str(x))
        with app.subFrame(bg='orange'):
            app.label("2", bg=app.RANDOM_COLOUR())
            for x in range(10): app.button(str(x))
        with app.subFrame(bg='yellow'):
            app.label("3", bg=app.RANDOM_COLOUR())
            for x in range(10): app.check(str(x), bg=app.RANDOM_COLOUR(), stretch='both', sticky='news')
    with app.frameSet("fs"):
        with app.subFrame(bg='green'):
            app.label("4", bg=app.RANDOM_COLOUR())
            for x in range(10): app.option(str(x), [x])
        with app.subFrame(bg='blue'):
            app.label("5", bg=app.RANDOM_COLOUR())

    app.buttons(["FIRST", "PREV", "NEXT", "LAST"], press)
    app.option("SETFRAME", range(app.countSubFrame("fs")), change=press)
