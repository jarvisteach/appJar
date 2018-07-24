import sys
sys.path.append("../../")

from appJar import gui

def open(btn):
    if btn == 'FILE': print(app.openBox(multiple=app.tick('multiple')))
    elif btn == 'OBJ': print(app.openBox(asFile=True, multiple=app.tick('multiple'), mode=app.entry('mode')))

with gui() as app:
    app.tick('multiple')
    app.entry('mode', 'r')
    app.buttons(['FILE', 'OBJ'], open)
