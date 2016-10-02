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

def bar(btn):
    if btn == "HIDE": app.hideToolbar()
    else: app.showToolbar()


tools = ["ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
        "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
        "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
        "WEB", "OFF"]

settings = {"Bold":False, "Italic": False, "Underline": False}

app=gui()

app.startPanedWindow("mainPane")
app.setBg("grey")
app.addLabel("mainLabel", "Enter your text below")
app.addTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 25)
app.startPanedWindow("toolPane")
app.setSticky("new")
app.addProperties("Settings", settings)
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
