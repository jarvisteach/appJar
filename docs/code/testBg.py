from appJar import gui

def getName(btn):
    app.setLabel("FOCUS", app.getFocus())
    print(app.getLabelWidget("f"))

def dialogs(btn):
    if btn == "B2": print(app.colourBox())
    elif btn == "B3": print(app.openBox())
    elif btn == "B4": print(app.directoryBox())

app=gui()
app.addMenuSystem()
app.addMenuCheckBox("SYSTEM", "fred")
app.setFg("green")
app.setFont(15)
app.addToolbar(["But1", "But2", "But3"], getName)

app.setBg("green")

app.addLabel("1", "Label 1")
app.setLabelBg("1", "yellow")

app.startLabelFrame("Big Frame")
#app.setBg("pink")

app.startLabelFrame("LabelFrame")
#app.setLabelFrameBg("LabelFrame", "red")
app.addLabel("2", "Label 2",0)
app.addLabels(["a", "b", "c", "d", "e", "f"],1)

app.addButton("FOCUS NAME", getName, 2, 0)

app.addFlashLabel("FOCUS", "FOCUS NAME HERE",3, 0,3)
app.addButtons(["B2", "B3", "B4"], dialogs,4)
app.setButtonBg("B3", "blue")
app.addEntry("e1", 5, 0)
app.addLabelEntry("e2", 5, 1)
app.startPanedWindow("p1", 6, 1)
app.setBg("yellow")
app.addRadioButton("rb1", "Radios")
app.addRadioButton("rb1", "Tellies")
app.addRadioButton("rb1", "Players")
app.startPanedWindow("p2")
app.setBg("pink")
app.addCheckBox("cb1")
app.addCheckBox("cb2")
app.addCheckBox("cb3")
app.stopPanedWindow()
app.stopPanedWindow()
app.addOptionBox("ob1", [1,2,3,4,5], 7, 0)
app.setOptionBoxBg("ob1", "yellow")
app.addLabelOptionBox("ob2", [1,2,3,4,5], 7, 1)
app.addSpinBox("sb1", [1,2,3,4,5], 8, 0)
app.addLabelSpinBox("sb2", [1,2,3,4,5], 8, 1)
app.addListBox("lb1", [1,2,3,4,5], 9, 0)
app.setListBoxRows("lb1", 5)
app.addTextArea("tx1", 9, 1)
app.setTextAreaHeight("tx1", 5)
app.addScale("sc1", 10, 0)
app.addLabelScale("sc2", 10, 1)
app.addMessage("mg1", "This is a long message")
app.addMeter("m1", 11, 0)
app.addSplitMeter("m2", 12, 1)
app.addDualMeter("m3", 12, 2)

#app.setSticky("EW")
app.addSeparator(13)
#app.setSticky(None)
app.addWebLink("appjar", "http://www.appjar.info", 14)

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
