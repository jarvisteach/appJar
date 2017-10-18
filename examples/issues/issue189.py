import sys
sys.path.append("../../")

from appJar import gui
app = gui("ttk demo")
with app.labelFrame("LabelFrame"):
    with app.notebook("nb"):
        with app.note("note1"):
            app.addLabel("l1", "Simple Label")
            app.addCheckBox("Tick me")
            app.addRadioButton("tb", "Tick me")
            app.addTextArea("t1")
            app.addButton("Press Me", None)
            app.addScale("Scale")
            app.addEntry("Entry")
            app.addButtons(["a", "b", "c"], None)
            app.addLabelEntry("fill me")
            app.addLabels(["a", "b", "c"])
        with app.note("note2"):
            pass
app.go()
