import sys
sys.path.append("../../")
from appJar import gui
counter = 100

def press(btn):
    global counter
    with app.toggleFrame("tf"):
        app.addLabel("LAB" + str(counter), "More text")
    with app.labelFrame("l1"):
        app.addLabel("llLAB" + str(counter), "More text")
    with app.scrollPane("sp1"):
        app.addLabel("pf" + str(counter), "and again")
    with app.subWindow("sub1"):
        app.addLabel("sub1"+str(counter), "Label Text")
    with app.tab("tabs", "tab"):
        app.addLabel("tab"+str(counter), "Label Text")
    with app.tabbedFrame("tabs"):
        with app.tab("tab" + str(counter)):
            app.addLabel("tabz" + str(counter) ,"text here")
    with app.panedFrame("pf2"):
        app.addLabel("pf2pf" + str(counter), "text")
    counter += 1

def show(btn):
    app.showSubWindow("sub1")

with gui() as app:
    with app.tabbedFrame("tabs"):
        with app.tab("tab"):
            with app.panedFrame("p1"):
                with app.pagedWindow("pw"):
                    with app.page(sticky="news"):
                        with app.scrollPane("sp1"):
                            with app.labelFrame("l1", sticky="nsew"):
                                app.addLabel("l1", "some text")
                            with app.toggleFrame("tf"):
                                app.addLabel("tf1", "In the toggle")
                            app.addButton("PRESS", press)
                            app.addButton("SHOW", show)
                    with app.page():
                        with app.labelFrame("l2"):
                            app.addLabel("l2", "some text")
                    with app.page():
                        with app.labelFrame("l3"):
                            app.addLabel("l3", "some text")
                with app.panedFrame("pf2"):
                    app.addLabel("pf2l", "some text")
            with app.subWindow("sub1"):
                app.addLabel("sub1", "Label Text")
