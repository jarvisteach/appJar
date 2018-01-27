import sys
sys.path.append("../../")

colour = "red"
col = "blue"

all_vars = ["a", "b"]
from appJar import gui

app=gui()

app.addLabel("l1", "help")
app.addListBox("avar_options",all_vars)

app.startSubWindow("Adding Variables", modal=True)
app.setSticky("nesw")
#app.setBg(colour)
#app.setFont(title_size,font)
app.addLabel("addVarTitle", "Adding Variables")
app.setStretch("both")
#app.setLabelBg("addVarTitle",col)
#app.setLabelFg("addVarTitle", col)

app.addListBox("var_options",all_vars)
#app.setStretch("both")
#app.setSticky("nesw")
#app.setListBoxMulti("var_options")
#app.setListBoxGroup("var_options")
app.stopSubWindow()

app.showSubWindow("Adding Variables")

app.go()
