from appJar import gui

def changer(btn):
    if btn == "Fruits":
        app.changeOptionBox("Options", ["Apple", "Orange", "Pear", "--", "Grapes", "Kiwi"], "Orange")
    elif btn == "Sports":
        app.changeOptionBox("Options", ["Football", "Cricket", "Golf", "- American -", "Baseball", "American Football"], 3)
    elif btn == "Empty":
        app.changeOptionBox("Options", [])
    elif btn == "Long":
        app.changeOptionBox("Options", ["aaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbb", "cccccccc", "--", "dddddddddddddddddddddddddddd"])

def press(btn):
    print(app.getOptionBox("Options"))

def pos(btn):
    if btn == "Change Entry":
        val = app.getEntry("Item")
    else:
        val = int(app.getOptionBox("Positions"))
    print(val)
    app.setOptionBox("Options", val)

app=gui()
app.setFont(20)
app.addLabelOptionBox("Options", ["", "Apple", "", "- here -", "Orange", "--", "Pear", "kiwi"])
app.addButton("Press", press)
app.addLabelOptionBox("Positions", [0,1,2,3,4,5,6,7,8,9])
app.addButton("Change Position", pos)
app.addLabelEntry("Item")
app.addButton("Change Entry", pos)
app.addButtons(["Fruits", "Sports", "Empty", "Long"], changer)
app.go()
