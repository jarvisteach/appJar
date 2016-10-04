from appJar import gui

app=gui()

app.setBg("blue")
#app.setExpand("both")
app.setSticky("")

app.addLabel("l1", "One", 0, 0)
app.setLabelBg("l1", "yellow")

app.addLabel("l2", "Two", 0, 1)
app.setLabelBg("l2", "green")

app.addLabel("l3", "Three", 1, 0)
app.setLabelBg("l3", "pink")

app.addLabel("l4", "Four", 1, 1)
app.setLabelBg("l4", "Orange")

app.go()
