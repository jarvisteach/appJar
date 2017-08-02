import sys
sys.path.append("../")


from appJar import gui
print(gui.SHOW_VERSION())

#from numpy import arange, sin, pi

app=gui()
#app.setFg("blue")
#app.setBg("orange")
app.setLogLevel("INFO")

app.addCheckBox("cb1", column=0)
app.addNamedCheckBox("cb2", "cb2", column=0)
app.addScale("s1", column=0)
app.addLabelScale("ls1", column=0)
app.addOptionBox("o1", ["a", "b"], column=0)
app.addTickOptionBox("to1", ["a", "b"], column=0)
app.addLabelTickOptionBox("lto1", ["a", "b"], column=0)
app.addLabelOptionBox("lo1", ["a", "b"], column=0)
app.addLabels(["a", "b", "c", "d"])
app.addProperties("p1", {"a": True, "b": False}, row=0, column=1)
app.addSpinBox("sb1",["a", "b"], row=1, column=1)
app.addLabelSpinBox("sb2",["a", "b"], row=2, column=1)
app.addSpinBoxRange("sb3", 5, 11, row=3, column=1)
app.addListBox("lb1",["a", "b"], row=4, column=1, rowspan=3)
app.addLabelSpinBoxRange("sb4", 5, 11, row=7, column=1)
#app.addAnimatedImage(
#app.addImageData(name, imageData)
#app.addImage(
app.addRadioButton("rb1", "rb1", row=8, column=1)
app.addRadioButton("rb1", "rb2", row=9, column=1)
app.addNamedButton("b1", "b1", None, row=0, column=2)
app.addButton("b2", None, row=1, column=2)
#app.addImageButton("b2", None, imgFile)
app.addButtons(["b3", "b4", "b5",], None, row=2, column=2)
app.addWebLink("web", "http://www.google.com", row=3, column=2)
app.addDatePicker("dp", row=4, column=2, rowspan=3)
app.addTrashBin("tb", row=6, column=2)
app.addLink("link", None, row=7, column=2)
app.addFlashLabel("fl1", "flash", row=8, column=2)
app.addGrip(row=9, column=2)
app.addSelectableLabel("sl1", "selectable", row=0, column=3)
app.addLabel("l1", "label", row=1, column=3)
app.addEmptyLabel("el1", row=2, column=3)
app.addMessage("mess", "mess", row=3, column=3)
app.addTextArea("ta", row=4, column=3, rowspan=2)
app.addEmptyMessage("mess2", row=6, column=3)
app.addEntry("e1", row=7, column=3)
app.addFileEntry("fe1", row=8, column=3)
app.addDirectoryEntry("de1", row=9, column=3)
app.addValidationEntry("ve1", row=10, column=3)
app.addLabelValidationEntry("lve1", row=11, column=3)
app.setEntryValid("ve1")
app.setEntryInvalid("lve1")

app.addTree("t1",
    """<people>
    <person><name>Fred</name><age>45</age><gender>Male</gender></person>
    <person><name>Tina</name><age>37</age><gender>Female</gender></person>
    <person><name>CLive</name><age>28</age><gender>Male</gender></person>
    <person><name>Betty</name><age>51</age><gender>Female</gender></person>
    </people>""", column=7, row=0, rowspan=5)
app.addScrolledTextArea("ta2", row=5, column=7, rowspan=1)
#app.addGoogleMap("gm1", column=7, row=1)
app.addMicroBit("mb", row=6, column=7, rowspan=7)
#t = arange(0.0, 3.0, 0.01)
#s = sin(2*pi*t)
#app.addPlot("p1", t, s)
#app.addGrid("grid", [["A","B","C"], [3,4,5,6,7,8], [2,4,6,8]], action=None, addRow=True)

app.addAutoEntry("ae", ["a", "b"], row=0, column=5)
app.addLabelAutoEntry("lae1", ["a", "b"], row=1, column=5)
app.addNumericEntry("ne1", row=2, column=5)
app.addLabelNumericEntry("lne1", row=3, column=5)
app.addNumericLabelEntry("lne2", row=4, column=5)
app.addSecretEntry("se", row=5, column=5)
app.addLabelEntry("le", row=6, column=5)
app.addLabelSecretEntry("lse1", row=7, column=5)
app.addSecretLabelEntry("lse2", row=8, column=5)
app.addMeter("m1", row=0, column=4)
app.addSplitMeter("m2", row=1, column=4)
app.addDualMeter("m3", row=2, column=4)
app.addSeparator(row=3, column=4)
app.addHorizontalSeparator(row=4, column=4)
app.addVerticalSeparator(row=5, column=4, rowspan=4)
#app.addPieChart("p1")
app.addProperties("prop", row=6, column=5)
def changeFg(btn):
    app.setFg(app.colourBox(),
        app.getCheckBox("OVER") or app.getMenuCheckBox("Colours", "Override")
    )

def changeBg(btn):
    app.setBg(app.colourBox(),
        app.getCheckBox("OVER") or app.getMenuCheckBox("Colours", "Override"),
        app.getCheckBox("TINT") or app.getMenuCheckBox("Colours", "Tint")
    )

app.addButton("FG COL", changeFg, row=9, column=5)
app.addButton("BG COL", changeBg, row=10, column=5)
app.addCheckBox("OVER", row=11, column=5)
app.addCheckBox("TINT", row=12, column=5)
app.addMenuList("Colours", ["FG Col", "BG Col"], [changeFg, changeBg])
app.addMenuSeparator("Colours")
app.addMenuCheckBox("Colours", "Override")
app.addMenuCheckBox("Colours", "Tint")
app.addMenuSeparator("Colours")
app.addMenuItem("Colours", "Quit", app.stop)

app.addMenuEdit()
app.go()
