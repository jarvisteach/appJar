import sys
sys.path.append("../")
from appJar import gui
showing = True

def tbFunc(tool):
    print(tool)
    if tool == "SETTINGS":
        global showing
        if showing: app.hideProperties("Settings")
        else: app.showProperties("Settings")
        showing = not showing
    elif tool == "HELP":
        app.infoBox("HELP", "HELPER")
    elif tool == "ABOUT":
        app.infoBox(".HELP", "ABOUTER")
    elif tool == "REFRESH":
        app.clearStatusbar()
    elif tool == "OPEN":
        app.openBox()
    elif tool == "CALENDAR":
        app.numberBox("nb", "nb")
    elif tool == "OFF":
        app.stop()

def bar(btn):
    if btn == "HIDE": app.hideToolbar()
    else: app.showToolbar()


tools = ["aaa", "bbb", "ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
        "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
        "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
        "WEB", "OFF"]

settings = {"Bold":False, "Italic": False, "Underline": False}

app=gui("Toolbar Demo")

app.startPanedFrame("mainPane")

app.setExpand("column")
app.setSticky("new")
app.setBg("lightgrey")
app.addLabel("mainLabel", "Enter your text below")
app.setLabelTooltip("mainLabel", "Mainlabel")
app.setLabelBg("mainLabel", "grey")

app.setExpand("all")
app.setSticky("nsew")
app.addScrolledTextArea("t1")
#app.setTextAreaBg("t1", "red")

app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 25)
app.startPanedFrame("toolPane")
app.setSticky("new")
app.addProperties("Settings", settings)
app.setSticky("new")
app.setExpand("column")
app.addButtons(["HIDE", "SHOW"], bar)
app.stopAllPanedFrames()

app.addToolbar(tools, tbFunc, True)
app.addStatusbar(fields=3, side="RIGHT")
app.setStatusbarBg("red", 2)
app.setStatusbarFg("white", 2)
app.setStatusbarWidth(50, 2)
app.setStatusbar("Line: 20", 0)
app.setStatusbar("Column: 4", 1)
app.setStatusbar("Mode: Edit", 2)
app.addGrip()

app.go()
