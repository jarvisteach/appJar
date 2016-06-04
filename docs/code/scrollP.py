from rwbatools import gui
cols=["red","blue"]

app=gui()
app.startScrollPane("sp")
for i in range(150):
    idd="L"+str(i)
    app.addLabel(idd, "In the pane")
    app.setLabelBg(idd, cols[i%2])
app.stopScrollPane()
app.addLabel("l2", "Out scroll pane")
app.go()
