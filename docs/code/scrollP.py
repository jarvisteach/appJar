from rwbatools import gui
cols=["red","blue"]

app=gui("Scroll Pane", "300x200")
app.startScrollPane("sp")
for i in range(150):
    idd="L"+str(i)
    app.addLabel(idd, "In the paneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    app.setLabelBg(idd, cols[i%2])
app.stopScrollPane()
app.startScrollPane("sp2")
for i in range(150):
    idd="LL"+str(i)
    app.addLabel(idd, "In the paneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    app.setLabelBg(idd, cols[i%2])
app.stopScrollPane()
app.addLabel("l2", "Out scroll pane")
app.go()
