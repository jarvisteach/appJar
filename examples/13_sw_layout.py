from appJar import gui

def show(btn): app.showSubWindow("sub")
def hide(btn): app.hideSubWindow("sub")

app=gui()
app.addLabel("l1", "Sub Window Demo")
app.addButton("PRESS", show)

app.startSubWindow("sub")
app.addLabel("s1", "sub")
app.addButton("Stop", hide)
app.stopSubWindow()
app.setSubWindowLocation("sub", 400,400)

app.go()
