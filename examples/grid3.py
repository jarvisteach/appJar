from appJar import gui

cols=["red","blue"]

app=gui()
app.setFont(20)

for loop in range(3):
    app.addLabel(loop, "New Row", colspan=2)
    app.setLabelBg(loop, cols[loop%2])

row = app.getRow() # get current row

app.addLabel("a", "LEFT", row, 0) 
app.addLabel("b", "RIGHT", row, 1) 

app.setLabelBg("a", "green")
app.setLabelBg("b", "orange")

for loop in range(3, 6):
    app.addLabel(loop, "New Row", colspan=2)
    app.setLabelBg(loop, cols[loop%2])

app.go()
