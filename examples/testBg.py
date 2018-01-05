import sys
sys.path.append("../")
from appJar import gui

def getName(btn):
    app.setLabel("FOCUS", app.getFocus())
    print(app.getLabelWidget("f"))

def dialogs(btn):
    if btn == "B2": print(app.colourBox())
    elif btn == "B3": print(app.openBox())
    elif btn == "B4": print(app.directoryBox())

app=gui()
app.setFg("green")
app.setFont(15)
app.addToolbar(["But1", "But2", "But3"], getName)

app.setBg("green")

app.addLabel("1", "Label 1")
app.setLabelBg("1", "yellow")

app.startLabelFrame("Big Frame")
app.setBg("pink")

app.startLabelFrame("LabelFrame")
app.setLabelFrameBg("LabelFrame", "red")
app.addLabel("2", "Label 2")
app.addLabels(["a", "b", "c", "d", "e", "f"])

row=app.gr()
app.addButton("FOCUS NAME", getName, row, 0)

app.addFlashLabel("FOCUS", "FOCUS NAME HERE",row, 1)
app.addButtons(["B2", "B3", "B4"], dialogs)
app.setButtonBg("FOCUS NAME", "yellow")
app.setButtonBg("B2", "blue")
app.setButtonBg("B3", "orange")
app.setButtonBg("B4", "pink")
row=app.gr()
app.addEntry("e1", row, 0)
app.addLabelEntry("e2", row, 1)
row=app.gr()
app.startPanedWindow("p1", row, 0, 5)
app.addRadioButton("rb1", "Radios")
app.addRadioButton("rb1", "Tellies")
app.addRadioButton("rb1", "Players")
app.startPanedWindow("p2")
app.addCheckBox("cb1")
app.addCheckBox("cb2")
app.addCheckBox("cb3")
app.stopPanedWindow()
app.stopPanedWindow()
row=app.gr()
app.addOptionBox("ob1", [1,7777777777,"alfs",4,5], row, 0)
app.addLabelOptionBox("ob2", ["bee", "zebra", "elephant", "lots of anacondas"], row, 1)
row=app.gr()
app.addSpinBox("sb1", [1,2,3,4,5], row, 0)
app.addLabelSpinBox("sb2", [1,2,3,4,5], row, 1)
row=app.gr()
app.addListBox("lb1", [1,2,3,4,5], row, 0)
app.setListBoxRows("lb1", 5)
app.addTextArea("tx1", row, 1)
app.setTextAreaHeight("tx1", 5)
row=app.gr()
app.addScale("sc1", row, 0)
app.addLabelScale("sc2", row, 1)
app.addMessage("mg1", "This is a long message")
row=app.gr()
app.addMeter("m1", row, 0)
app.addSplitMeter("m2", row, 1)
app.addDualMeter("m3", row, 2)

#app.setSticky("EW")
app.addHorizontalSeparator()
#app.setSticky(None)
app.addWebLink("appjar", "http://www.appjar.info")

app.stopLabelFrame()

app.addLabel("3", "Label 3")
app.setLabelBg("3", "yellow")

app.startLabelFrame("LabelFrame2")
app.setLabelFrameBg("LabelFrame2", "orange")
app.addLabel("4", "Label 4")
app.stopLabelFrame()

app.addLabel("5", "Label 5")
app.setLabelBg("5", "yellow")

app.stopLabelFrame()
app.addLabel("6", "Label 6")

app.setBg("white")
app.go()
