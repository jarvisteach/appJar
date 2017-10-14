import sys
sys.path.append("../")

from appJar import gui

with gui() as app:
    with app.labelFrame("lf1"):
        app.addLabel("l1", "text")
        app.addLabel("l2", "text")
        app.addLabel("l3", "text")
    with app.labelFrame("lf2"):
        app.addLabel("l4", "text")
    with app.toggleFrame("tf1"):
        app.addLabel("l5", "text")
    app.addButton("Press", None)
