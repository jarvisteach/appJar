import sys
sys.path.append("../")

from appJar import gui

def s(btn=None): print(app.visible)
def h(): app.visible = False
def w(): app.visible = True

with gui() as app:
    app.guiPadding = (50,10)
    with app.labelFrame("lf1"):
        app.addLabel("l1", "text")
        app.addLabel("l2", "text")
        app.addLabel("l3", "text")
    with app.labelFrame("lf2"):
        app.addLabel("l4", "text")
    with app.toggleFrame("tf1"):
        app.addLabel("l5", "text")
    app.addButton("Press", None)
    app.registerEvent(s)
    app.after(500, h)
    app.after(2000, w)
