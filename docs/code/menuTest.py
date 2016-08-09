from appJar import gui

def menuPress(men=None):
    print("PRESSED:",men)
    app.setStatus(men)

def enab(option):
    if option == "ENABLE":
        app.enableMenuItem("Test 1", "Option 2")
    else:
        app.disableMenuItem("Test 1", "Option 2")

def showMenus(btn):
    data = "RB 3=" + str(app.getMenuRadioButton("Test 1", "Option 3")) + "\n"
    data += "CB 5=" + str(app.getMenuCheckBox("Test 1", "Option 5")) + "\n"
    data += "CB 6=" + str(app.getMenuCheckBox("Test 1", "Option 6")) + "\n"
    app.clearTextArea("t1")
    app.setTextArea("t1", data)

app=gui("Menu Tester", "400x400")

app.createMenu("Test 1", True)
app.createMenu("Test 2")
app.createMenu("Test 3")
app.addMenu("Funky", menuPress)

app.addMenuItem("Test 1", "Option 1", menuPress, shortcut="f")
app.addMenuItem("Test 1", "Option 2", menuPress, shortcut="g")
app.addMenuItem("Test 1", "-")
app.addMenuItem("Test 1", "Option 3", "dogs", kind="rb", shortcut="3")
app.addMenuItem("Test 1", "Option 3", "cats", kind="rb", shortcut="4")
app.addMenuItem("Test 1", "-")
app.addMenuItem("Test 1", "Option 5", kind="cb", shortcut="5")
app.addMenuItem("Test 1", "Option 6", kind="cb", shortcut="6")
app.addMenuItem("Test 1", "-")
app.addMenuItem("Test 1", "More Menus", kind="sub", shortcut="7")
app.addMenuItem("More Menus", "Option 10", menuPress, shortcut="a")
app.addMenuItem("More Menus", "Option 20", menuPress, shortcut="b")

app.addMenuWindow()
app.addMenuPreferences(menuPress)
app.addMenuHelp(menuPress)
app.addMenuItem("help", "Option Help", menuPress, shortcut="h")
app.addMenuItem("window", "Window", menuPress, shortcut="w")

app.addButton("SHOW", showMenus)
app.addTextArea("t1")
app.addButtons(["ENABLE", "DISABLE"], enab)



app.addStatus()

app.go()
