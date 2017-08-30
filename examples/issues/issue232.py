import sys
sys.path.append("../../")
from appJar import gui

data1 = [["Name", "Age", "Gender"], ["Fred", 45, "Male"], ["Tina", 37, "Female"], ["Clive", 28, "Male"], ["Betty", 51, "Female"]]
data2 = [["NewName", "NewAge", "NewGender", "A.N.Other"], ["Fred", 45, "Male"], ["Tina", 37, "Female"], ["Clive", 28, "Male"], ["Betty", 51, "Female"]]

def swapGrid(btn):
    app.removeGrid("g1")
    app.openTab("Tabs", "one")
    app.addGrid("g1", data2)
    app.stopTab()

app = gui()
app.startTabbedFrame("Tabs")
app.startTab("one")
app.addGrid("g1", data1)
app.stopTab()
app.startTab("two")
app.addLabel("l2", "Tab Two")
app.stopTab()
app.startTab("three")
app.addLabel("l3", "Tab Three")
app.stopTab()
app.stopTabbedFrame()
app.addButton("SWAP", swapGrid)
app.go()
