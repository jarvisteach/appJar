from appJar import gui

def fill(btn):
    if btn=="FILL": app.setTabbedFrameTabExpand("NB")
    elif btn=="SMALL": app.setTabbedFrameTabExpand("NB", False)
    elif btn=="SELECT": app.setTabbedFrameSelectedTab("NB", app.getEntry("Select Tab"))

app = gui()

app.startTabbedFrame("NB")

app.startTab("Tab1")
app.addLabel("l1", "TabbedFrame Tab 1 Demo")
app.stopTab()

app.startTab("Tab2")
app.addLabel("l2", "TabbedFrame Tab 2 Demo")
app.stopTab()

app.startTab("Tab3")
app.addLabel("l3", "TabbedFrame Tab 3 Demo")
app.stopTab()

app.startTab("Tab4")
app.addLabel("l4", "TabbedFrame Tab 4 Demo")
app.stopTab()

app.stopTabbedFrame()

app.addLabelEntry("Select Tab")
app.addButtons(["FILL", "SMALL", "SELECT"], fill)

tabs=app.getTabbedFrameWidget("NB")
tabs.configure(activeforeground="red", foreground="gray", disabledforeground="gray", bg="purple", activebackground="lightblue", inactivebackground="darkblue")
app.setBg("pink")
app.go()
