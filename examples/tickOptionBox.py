import sys
sys.path.append("../")

new_ticks = ["Dogs2", "Cats2", "-", " ", "Hamsters2", "Fish2", "Spiders2", "", " "]
orig_ticks = ["Dogs", "Cats", "Hamsters", "Fish", "Spiders"]

from appJar import gui

def get(btn):
    print(app.getOptionBox("Favourite Pets"))
    print(app.getOptionBox("The Action"))

def tickOption(opt):
    print("tick box", opt)
    app.setOptionBox("Favourite Pets", opt, app.getCheckBox(opt))

def tickOptionBox(opt):
    print("menu tick box", opt)
    optValue = app.getOptionBox("Favourite Pets")[opt]
    app.setCheckBox(opt, optValue, callFunction=False)

def doAction(act):
    app.setOptionBox("The Action", app.getOptionBox(act))

def findIndex(act):
    app.setOptionBox("The Action", app.getScale(act))

def changeOptions(btn=None):
    app.changeOptionBox("Favourite Pets", new_ticks)
    app.setOptionBoxChangeFunction("Favourite Pets", tickOptionBox)

def changeOptionsBack(btn=None):
    app.changeOptionBox("Favourite Pets", orig_ticks)
    app.setOptionBoxChangeFunction("Favourite Pets", tickOptionBox)

app=gui()
app.setFont(20)
app.setBg("PapayaWhip")

app.addLabelTickOptionBox("Favourite Pets", [])
changeOptionsBack()
app.addLabelOptionBox("The Action", ["Pet", "Stroke", "Feed", "Bathe", "Walk"])
app.addLabelOptionBox("Set Action", ["Pet", "Stroke", "Feed", "Bathe", "Walk"])
app.setOptionBoxChangeFunction("Set Action", doAction)
app.addScale("index")
app.setScaleRange("index", 0,4)
app.showScaleValue("index")
app.setScaleChangeFunction("index", findIndex)

app.startLabelFrame("Tick Us")
app.addCheckBox("Dogs")
app.addCheckBox("Cats")
app.addCheckBox("Hamsters")
app.addCheckBox("Fish")
app.addCheckBox("People")
app.setCheckBoxChangeFunction("Dogs", tickOption)
app.setCheckBoxChangeFunction("Cats", tickOption)
app.setCheckBoxChangeFunction("Hamsters", tickOption)
app.setCheckBoxChangeFunction("Fish", tickOption)
app.setCheckBoxChangeFunction("People", tickOption)
app.stopLabelFrame()

app.addButtons(["GET", "CHANGE", "BACK"], [get,changeOptions, changeOptionsBack])

#app.setCheckBox("Dogs", True)
#app.setOptionBox("Favourite Pets", "Dogs")


app.go()
