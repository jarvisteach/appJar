import sys
sys.path.append("../../")
from appJar import gui

def drop(source, target):
    print(source, target)

def wait(btn):
    app.after(2000, drop, "hello")

app = gui("DnD")
app.setLogLevel("DEBUG")

app.addLabel("l1", "Click me")
app.setLabelBg("l1", "green")
app.registerLabelDraggable("l1")

app.addLabel("l2", "Click me 2")
app.setLabelBg("l2", "yellow")
app.registerLabelDraggable("l2")

app.addLabel("l3", "space to drop")
app.setLabelBg("l3", "red")
app.registerLabelDroppable("l3", drop)

toppings={"Cheese":False, "Tomato":False, "Bacon":False, "Corn":False, "Mushroom":False}

app.addProperties("Toppings", toppings)
app.setProperty("Toppings", "Pepper")

app.addTrashBin("tb1")
app.addEntry("e1")
app.setEntryDropTarget("e1")

app.startSubWindow("Subber")
#app.startLabelFrame("lf")
#app.startLabelFrame("lf2")
#app.startLabelFrame("lf3")
#app.startLabelFrame("lf4")

for i in range(5):
    name = "SUB" + str(i)
    app.addLabel(name, name)
    app.setLabelBg(name, "pink")
    app.registerLabelDroppable(name, drop)

app.addButton("PRESS ME", wait)

#app.stopLabelFrame()
#app.stopLabelFrame()
#app.stopLabelFrame()
#app.stopLabelFrame()

app.stopSubWindow()

app.showSubWindow("Subber")

app.go()
