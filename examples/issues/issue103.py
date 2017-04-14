import sys
sys.path.append("../../")

def changed(btn):
    print(btn)

def setter(btn):
    prop = False
    if app.getRadioButton("prop") == "True": prop = True

    if btn == "SetEntry": app.setEntry("Try me...", "new text", callFunction=prop)
    elif btn == "ClearEntry": app.clearEntry("Try me...", callFunction=prop)
    elif btn == "ClearAllEntries": app.clearAllEntries(callFunction=prop)
    elif btn == "SetText": app.setTextArea("the text", "new text", callFunction=prop)
    elif btn == "ClearText": app.clearTextArea("the text", callFunction=prop)
    elif btn == "SetRadio": app.setRadioButton("song", "Bo Rap", callFunction=prop)
    elif btn == "SetCheck": app.setCheckBox("Apples", True, callFunction=prop)
    elif btn == "SetOption": app.setOptionBox("Options", "Dogs", callFunction=prop)
    elif btn == "SetTicks": app.setOptionBox("Favourite Pets", "Dogs", True, callFunction=prop)
    elif btn == "SetSpin": app.setSpinBox("options", "Pear", callFunction=prop)
    elif btn == "SetList": app.selectListItem("list", "pear", callFunction=prop)
    elif btn == "SetScale": app.setScale("scale", 50, callFunction=prop)
    elif btn == "Toppings": app.setProperties("Toppings", toppings, callFunction=prop)

from appJar import gui
app=gui()
app.setBg("DarkKhaki")
app.setSticky("news")

app.addLabel("l1", "Change Events")

app.startFrame("f1")
app.addLabel("print", "")
app.addRadioButton("prop", "True", 0, 1)
app.addRadioButton("prop", "False", 0, 2)
app.setLabelSubmitFunction("l1", changed)
app.stopFrame()

# writing
app.startLabelFrame("Writing")
app.setSticky("new")
app.addLabelEntry("Try me...")
app.setEntryChangeFunction("Try me...", changed)

# text area
app.startLabelFrame("Type something...", 0, 1)
app.setSticky("news")
app.addTextArea("the text")
app.setTextAreaHeight("the text", 5)
app.setTextAreaChangeFunction("the text", changed)
app.stopLabelFrame()

app.addButtons(["SetEntry", "ClearEntry", "ClearAllEntries"], setter, 1, 0)
app.addButtons(["SetText", "ClearText"], setter, 1, 1)
app.stopLabelFrame()

# buttons
app.startLabelFrame("Buttons")
app.setSticky("news")
app.addRadioButton("song", "Killer Queen", column=0)
app.addRadioButton("song", "Bo Rap", column=0)
app.setRadioButtonChangeFunction("song", changed)

app.addCheckBox("Apples", 0, 1)
app.setCheckBoxChangeFunction("Apples", changed)

app.addButton("SetRadio", setter, 2, 0)
app.addButton("SetCheck", setter, 2, 1)
app.stopLabelFrame()

# boxes
app.startLabelFrame("Boxes")
app.setSticky("new")
app.addLabelOptionBox("Options", ["- Fruits -", "Apple", "Orange",
                        "Pear", "kiwi", "- Pets -", "Dogs", "Cats",
                        "Fish", "Hamsters"], 0)
app.setOptionBoxChangeFunction("Options", changed)

app.addTickOptionBox("Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"], 0, 1)
app.setOptionBoxChangeFunction("Favourite Pets", changed)

app.addLabelSpinBox("options", ["Apple", "Orange", "Pear", "kiwi"], 0,2)
app.setSpinBoxChangeFunction("options", changed)

app.addListBox("list", ["apple", "orange", "pear", "kiwi"], 0,3)
app.setListBoxChangeFunction("list", changed)

app.addButton("SetOption", setter, 1, 0)
app.addButton("SetTicks", setter, 1, 1)
app.addButton("SetSpin", setter, 1, 2)
app.addButton("SetList", setter, 1, 3)
app.stopLabelFrame()

# scale
app.startLabelFrame("Scale")
app.setSticky("news")
app.addLabelScale("scale")
app.setScaleChangeFunction("scale", changed)

app.addButton("SetScale", setter, 0, 1)
app.stopLabelFrame()

toppings={"Cheese":False, "Tomato":False, "Bacon":False,
            "Corn":False, "Mushroom":False}
app.addProperties("Toppings", toppings)
app.setPropertiesChangeFunction("Toppings", changed)
app.addButton("Toppings", setter)


app.addButton("b1", None)
app.setButtonChangeFunction("b1", changed)
app.setButtonSubmitFunction("b1", changed)

app.go()
