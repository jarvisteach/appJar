import sys
sys.path.append("../../")
from appJar import gui

app = gui()

with app.panedFrame("pf"):
    with app.pagedWindow("pw"):
        with app.page():
            with app.labelFrame("l1"):
                app.addLabel("l1", "some text")
        with app.page():
            with app.labelFrame("l2"):
                app.addLabel("l2", "some text")
        with app.page():
            with app.labelFrame("l3"):
                app.addLabel("l3", "some text")

app.go()
