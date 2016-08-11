from appJar import gui

def get(btn):
    print(app.getOptionBox("Favourite Pets"))
    print(app.getOptionBox("The Action"))

def tickOption(opt):
    app.setOptionBox("Favourite Pets", opt, app.getCheckBox(opt))

def doAction(act):
    app.setOptionBox("The Action", app.getOptionBox(act))

def findIndex(act):
    app.setOptionBox("The Action", app.getScale(act))

app=gui()
app.setFont(20)
app.setBg("PapayaWhip")

app.addLabelTickOptionBox("Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"])
app.addLabelOptionBox("The Action", ["Pet", "Stroke", "Feed", "Bathe", "Walk"])
app.addLabelOptionBox("Set Action", ["Pet", "Stroke", "Feed", "Bathe", "Walk"])
app.setOptionBoxFunction("Set Action", doAction)
app.addScale("index")
app.setScaleRange("index", 0,4)
app.showScaleValue("index")
app.setScaleFunction("index", findIndex)

app.startLabelFrame("Tick Us")
app.addCheckBox("Dogs")
app.addCheckBox("Cats")
app.addCheckBox("Hamsters")
app.addCheckBox("Fish")
app.addCheckBox("People")
app.setCheckBoxFunction("Dogs", tickOption)
app.setCheckBoxFunction("Cats", tickOption)
app.setCheckBoxFunction("Hamsters", tickOption)
app.setCheckBoxFunction("Fish", tickOption)
app.setCheckBoxFunction("People", tickOption)
app.stopLabelFrame()

app.addButton("GET", get)

app.setCheckBox("Dogs", True)
app.setOptionBox("Favourite Pets", "Dogs")

app.go()
