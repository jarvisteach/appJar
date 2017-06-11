import sys
sys.path.append("../../")

from appJar import gui

app=gui()
app.startToggleFrame("Birthday")
app.addDatePicker("dp")
app.stopToggleFrame()

app.startToggleFrame("Birthday")
app.startLabelFrame("lf22")
app.addDatePicker("dp2")
app.stopLabelFrame()
app.stopToggleFrame()


app.startToggleFrame("TabsToggle")
app.startLabelFrame("TABS")
app.startTabbedFrame("the tabs")

app.startTab("1")
app.addDatePicker("tdp1")
app.stopTab()
app.startTab("2")
app.addDatePicker("tdp2")
app.stopTab()
app.startTab("3")
app.addDatePicker("tdp3")
app.stopTab()

app.stopTabbedFrame()
app.stopLabelFrame()
app.stopToggleFrame()

app.go()
