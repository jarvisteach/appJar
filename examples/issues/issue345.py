import sys
sys.path.append("../../")
from appJar import gui

current = 0

def up():
    global current
    current = 1 if current > 4 else current + 1
    app.raiseFrame(str(current))

with gui() as app:
    with app.frame("1", bg='red', row=0, column=0):
        app.label("1")
        for x in range(10): app.radio("A", str(x))
    with app.frame("2", bg='orange', row=0, column=0):
        app.label("2")
        for x in range(10): app.button(str(x))
    with app.frame("3", bg='yellow', row=0, column=0):
        app.label("3")
        for x in range(10): app.check(str(x))
    with app.frame("4", bg='green', row=0, column=0):
        app.label("4")
        for x in range(10): app.option(str(x), [x])
    with app.frame("5", bg='blue', row=0, column=0):
        app.label("5")

    app.button("NEXT", up)
    up()
