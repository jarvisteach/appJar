from appJar import gui

def press(btn): pass

app=gui()
app.setFont(20)

app.addLabel("l1", "Calculator")
app.setLabelBg("l1", "pink")

app.addButtons([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], press)

app.go()
