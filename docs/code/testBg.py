from appJar import gui

app=gui()

app.setBg("green")

app.addLabel("1", "Label 1")
app.setLabelBg("1", "yellow")

app.startLabelFrame("Big Frame")
app.setLabelFrameBg("Big Frame", "blue")

app.startLabelFrame("LabelFrame")
app.setLabelFrameBg("LabelFrame", "red")
app.addLabel("2", "Label 2")
app.addLabels(["a", "b", "c", "d", "e", "f"])

app.addButton("B1", None)
app.addButtons(["B2", "B3", "B4"], None)
row=app.getNextRow()
app.addEntry("e1", row, 0)
app.addLabelEntry("e2", row, 1)
app.addRadioButton("rb1", "Radios")
app.addCheckBox("cb1")
row=app.getNextRow()
app.addOptionBox("ob1", [1,2,3,4,5], row, 0)
app.addLabelOptionBox("ob2", [1,2,3,4,5], row, 1)
row=app.getNextRow()
app.addSpinBox("sb1", [1,2,3,4,5], row, 0)
app.addLabelSpinBox("sb2", [1,2,3,4,5], row, 1)
app.addListBox("lb1", [1,2,3,4,5])
row=app.getNextRow()
app.addScale("sc1", row, 0)
app.addLabelScale("sc2", row, 1)
app.addMessage("mg1", "This is a long message")
app.addTextArea("tx1")
row=app.getNextRow()
app.addMeter("m1", row, 0)
app.addSplitMeter("m2", row, 1)
app.addDualMeter("m3", row, 2)

#app.setSticky("EW")
app.addSeparator()
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

app.go()
