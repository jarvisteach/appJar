import sys
sys.path.append("../../")

from appJar import gui

def launch(win):
    app.showSubWindow(win)

with gui() as app:
    app.addLabel("l0", "text")
    app.setLabelTooltip("l0", "text")
    app.addButtons(["one", "two"], launch)

    # this is a pop-up
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", "SubWindow One")
    app.stopSubWindow()

    # this is another pop-up
    app.startSubWindow("two")
    app.addLabel("l2", "SubWindow Two")
    app.stopSubWindow()
