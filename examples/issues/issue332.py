import sys
sys.path.append("../../")

channels = ["this", "that", "another", "one more"]

from appJar import gui

def deleteTab(tabName):
    print("deleting", tabName)
#    tabs = app.widgetManager.get(app.Widgets.TabbedFrame, "tabs")
#    tabs.deleteTab(tabName)
    app.deleteTabbedFrameTab("tabs", tabName)

def disableTab(tabName):
    print("disabling", tabName)
    tabs = app.widgetManager.get(app.Widgets.TabbedFrame, "tabs")
    tabs.disableTab(app.getTabbedFrameSelectedTab("tabs"))

def press(btn):
    app.openTabbedFrame("tabs")
    for tab in channels:
        app.startTab(tab)
        app.addLabel(tab, tab)
        app.addNamedButton("DELETE", tab, deleteTab)
        app.addNamedButton("DISABLE", tab+"a", disableTab)
        app.stopTab()
    app.stopTabbedFrame()

def pressNew(btn):
    with app.tabbedFrame("tabs"):
        with app.tab("Five"):
            app.label("t5", "Tab Five")

def hide(btn):
    if btn == "HIDE": app.hideTabbedFrameTab("tabs", "Two")
    else: app.showTabbedFrameTab("tabs", "Two")

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
    app.addButtons(["HIDE", "SHOW"], hide)
