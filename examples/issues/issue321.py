import sys
sys.path.append("../../")

from appJar import gui

############
# appJar 0.9
############
#with gui() as app:
#    with app.tabbedFrame("tabs"):
#        with app.tab("Tab 1"):
#            with app.labelFrame("Label Frame 1"):
#                app.label("a", "A label")
#            with app.labelFrame("Label Frame 2"):
#                app.label("b", "Another label")
#        with app.tab("Tab 2"):
#            with app.labelFrame("Label Frame 3"):
#                app.label("2a", "A label")
#            with app.labelFrame("Label Frame 4"):
#                app.label("2b", "Another label")

############
# appJar 0.8
############
app = gui()
app.startTabbedFrame("tabs")
app.startTab("Tab 1")
app.startLabelFrame("Label Frame 1")
app.addLabel("a", "A label")
app.stopContainer()
app.startLabelFrame("Label Frame 2")
app.addLabel("b", "Another label")
app.stopContainer()
app.stopContainer()
app.startTab("Tab 2")
app.startLabelFrame("Label Frame 3")
app.addLabel("2a", "A label")
app.stopContainer()
app.startLabelFrame("Label Frame 4")
app.addLabel("2b", "Another label")
app.stopContainer()
app.stopContainer()
app.stopContainer()
app.go()
