import sys
sys.path.append("../")
from appJar import gui

def fill(btn):
    if btn=="FILL": app.setTabbedFrameTabExpand("NB")
    elif btn=="SMALL": app.setTabbedFrameTabExpand("NB", False)
    elif btn=="SELECT": app.setTabbedFrameSelectedTab("NB", app.getEntry("Select Tab"))
    elif btn=="DISABLE": app.setTabbedFrameDisabledTab("NB", app.getEntry("Select Tab"))
    elif btn=="ENABLE": app.setTabbedFrameDisabledTab("NB", app.getEntry("Select Tab"), False)
    elif btn=="RENAME": app.setTabText("NB", app.getEntry("Select Tab"), False)
    elif btn=="HIDE": app.hideTabbedFrameTab("NB", app.getEntry("Select Tab"))
    elif btn=="SHOW": app.showTabbedFrameTab("NB", app.getEntry("Select Tab"))
    elif btn=="DELETE": app.deleteTabbedFrameTab("NB", app.getEntry("Select Tab"))
    elif btn=="ALL": app.setTabbedFrameDisableAllTabs("NB")

app = gui()

app.startTabbedFrame("NB")

app.startTab("Tab1")
app.addLabel("l1", "TabbedFrame Tab 1 Demo")
app.addEntry("e1")
app.addButton("BUTTON", None)
app.addCheckBox("CHECKER")
app.stopTab()

app.startTab("Tab2")
app.setBg("pink")
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
app.addButtons(["FILL", "SMALL", "SELECT", "DISABLE", "ENABLE"], fill)
app.addButtons(["RENAME", "HIDE", "SHOW", "DELETE", "ALL"], fill)

#tabs=app.getTabbedFrameWidget("NB")
#
#app.setTabbedFrameActiveFg("NB", "tomato")
#app.setTabbedFrameActiveBg("NB", "saddlebrown")
#
#app.setTabbedFrameFg("NB", "coral")
#app.setTabbedFrameInactiveBg("NB", "wheat")
#
#app.setTabbedFrameDisabledFg("NB", "cornsilk")
#app.setTabbedFrameBg("NB", "purple")

#app.setBg("pink")
app.setBg("green")
app.go()
