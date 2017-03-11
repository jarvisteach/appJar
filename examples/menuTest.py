import sys
sys.path.append("../")
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

def printVals(item):
    print(item)
    print(app.getMenuRadioButton("Test 2", item))

app=gui("Menu Tester", "400x400")

app.createMenu("Test 1", True)
app.createMenu("Test 2")
app.createMenu("Test 3")
app.addMenu("Funky", menuPress)

app.addMenuItem("Test 1", "Option 1", menuPress, shortcut="f", underline=1)
app.addMenuItem("Test 1", "Option 2", menuPress, shortcut="g", underline=1)
app.addMenuItem("Test 2", "-")
app.addMenuRadioButton("Test 3", "RBBB", "RB1")
app.addMenuRadioButton("Test 3", "RBBB", "RB2")
app.addMenuItem("Test 3", "-")
app.addMenuCheckBox("Test 3", "CB1")
app.addMenuCheckBox("Test 3", "CB2")
app.addMenuCheckBox("Test 3", "CB3")
app.addMenuRadioButton("Test 3", "RBBB", "RB3", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB1", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB2", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB3", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB4", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB5", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB6", printVals)
app.addMenuRadioButton("Test 2", "RBBB", "RB7", printVals)
app.addMenuItem("Test 2", "-")
app.addMenuCheckBox("Test 2", "CB1")
app.addMenuCheckBox("Test 2", "CB2")
app.addMenuCheckBox("Test 2", "CB3")
app.addMenuItem("Test 1", "-")
app.addMenuItem("Test 1", "Option 3", kind="rb", shortcut="3", rb_id="dogs")
app.addMenuItem("Test 1", "Option 3", kind="rb", shortcut="4", rb_id="cats")
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
#app.addMenuItem("help", "Option Help", menuPress, shortcut="h")
#app.addMenuItem("window", "Window", menuPress, shortcut="w")

app.addButton("SHOW", showMenus)
app.addTextArea("t1")
app.addButtons(["ENABLE", "DISABLE"], enab)



app.addStatus()

app.go()
