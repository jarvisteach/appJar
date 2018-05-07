import sys
sys.path.append("../../")

def press(btn):
    with app.panedFrame("ap3"):
        app.addLabel("lll3", "New label")

def press2(btn):
    with app.panedFrameVertical("ap1"):
        app.addLabel("lll13", "New label")

from appJar import gui
with gui() as app:

    with app.tabbedFrame("tf"):

        with app.tab("Vertical Pane"):
            with app.panedFrameVertical("ap1"):
                app.addLabel("al1", "Inside Pane 1")
                with app.panedFrame("ap2"):
                    app.addLabel("al2", "Inside Pane 2")
                with app.panedFrame("ap3"):
                    app.addLabel("al3", "Inside Pane 3")
            app.addButton("PRESS", press)
            app.addButton("PRESS2", press2)

        with app.tab("Horizontal Pane"):
            with app.panedFrame("bp1"):
                app.addLabel("bl1", "Inside Pane 1")
                with app.panedFrame("bp2"):
                    app.addLabel("bl2", "Inside Pane 2")
                with app.panedFrame("bp3"):
                    app.addLabel("bl3", "Inside Pane 3")

        with app.tab("T-Pane"):
            with app.panedFrameVertical("cp1"):
                app.addLabel("cl1", "Inside Pane 1")
                with app.panedFrame("cp2"):
                    app.addLabel("cl2", "Inside Pane 2")
                    with app.panedFrame("cp3"):
                        app.addLabel("cl3", "Inside Pane 3")

        with app.tab("E-Pane"):
            with app.panedFrame("p1"):
                app.addLabel("l1", "Inside Pane 1")
                with app.panedFrameVertical("p2"):
                    app.addLabel("l2", "Inside Pane 2")
                    with app.panedFrame("p3"):
                        app.addLabel("l3", "Inside Pane 3")
                    with app.panedFrame("p4"):
                        app.addLabel("l4", "Inside Pane 4")
                    with app.panedFrame("p5"):
                        app.addLabel("l5", "Inside Pane 5")
