import sys
sys.path.append("../../")

from appJar import gui

name = 'new a'

def press():
    global name
    with app.tabbedFrame("tabs"):
        with app.tab(name, beforeTab="generic"):
            app.label(name)
    name += "a"

with gui() as app:
    with app.tabbedFrame("tabs") as tf:
        with app.tab("generic"):
            app.button("New tab", press)
        for c in ['a', 'b', 'c', 'd', 'e']:
            with app.tab(c*5):
                app.label(c)
