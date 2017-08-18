import sys
sys.path.append("../../")

from appJar import gui
app = gui("ttk demo")
#app.useTtk()
app.startLabelFrame("LabelFrame")
app.addLabel("l1", "Simple Label")
app.addCheckBox("Tick me")
app.addRadioButton("tb", "Tick me")
app.addButton("Press Me", None)
app.addScale("Scale")
app.addEntry("Entry")
app.stopLabelFrame()
app.go()

