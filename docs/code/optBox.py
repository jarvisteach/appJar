from appJar import gui

def press(btn):
    print(app.getOptionBox("Options"))

app=gui()
app.setFont(20)
app.addLabelOptionBox("Options", ["Apple", "Orange", "Pear", "kiwi"])
app.addButton("Press", press)
app.go()
