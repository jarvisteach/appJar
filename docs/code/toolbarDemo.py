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
        app.clearStatusbar(4)
    elif tool == "OPEN":
        app.openBox()
    elif tool == "CALENDAR":
        app.numberBox("nb", "nb")

def bar(btn):
    if btn == "HIDE": app.hideToolbar()
    else: app.showToolbar()


tools = ["ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
        "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
        "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
        "WEB", "OFF"]

settings = {"Bold":False, "Italic": False, "Underline": False}

app=gui("Toolbar Demo", "700x700")

app.startPanedWindow("mainPane")

app.setExpand("column")
app.setSticky("new")
app.setBg("lightgrey")
app.addLabel("mainLabel", "Enter your text below")
app.setLabelBg("mainLabel", "grey")

app.setExpand("all")
app.setSticky("nsew")
app.addScrolledTextArea("t1")
#app.setTextAreaBg("t1", "red")

app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 25)
app.startPanedWindow("toolPane")
app.setSticky("new")
app.addProperties("Settings", settings)
app.setSticky("new")
app.setExpand("column")
app.addButtons(["HIDE", "SHOW"], bar)
app.stopAllPanedWindows()

app.addToolbar(tools, tbFunc, True)
app.addStatusbar(fields=3, side="RIGHT")
app.setStatusbarBg("red", 2)
app.setStatusbarFg("white", 2)
app.setStatusbarWidth(50, 2)
app.setStatusbar("Line: 20", 0)
app.setStatusbar("Column: 4", 1)
app.setStatusbar("Mode: Edit", 2)

app.go()
