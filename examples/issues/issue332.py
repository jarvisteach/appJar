import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    app.openTabbedFrame("tabs")
    app.startTab("Four")
    app.addLabel("t4", "Tab Four")
    app.stopTab()
    app.stopTabbedFrame()

def pressNew(btn):
    with app.tabbedFrame("tabs"):
        with app.tab("Five"):
            app.label("t5", "Tab Five")

with gui("Tabs") as app:
    with app.tabbedFrame("tabs"):
        app.setTabbedFrameTabExpand("tabs", expand=True)
        with app.tab("One"):
            app.label("t1", "Tab One")
        with app.tab("Two"):
            app.label("t2", "Tab Two")
        with app.tab("Three"):
            app.label("t3", "Tab Three")

    app.addButtons(["OLD TAB", "NEW TAB"], [press, pressNew])
