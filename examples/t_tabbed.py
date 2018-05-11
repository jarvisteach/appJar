import sys
sys.path.append("../")

from appJar import gui

app=gui()

app.startTabbedFrame("TabbedFrame")
app.setTabbedFrameTabExpand("TabbedFrame")
app.startTab("Tab1")
app.addLabel("l1", "Tab 1 Label")
app.stopTab()

app.startTab("Tab2")
app.addLabel("l2", "Tab 2 Label")
app.stopTab()

app.startTab("Tab3")
app.addLabel("l3", "Tab 3 Label")
app.stopTab()
app.stopTabbedFrame()

app.go()
