from rwbatools import gui

app=gui()
app.startScrollPane("sp")
for i in range(50):
    app.addLabel("L"+str(i), "In the pane")
app.stopScrollPane()
app.addLabel("l2", "Out scroll pane")
app.go()
