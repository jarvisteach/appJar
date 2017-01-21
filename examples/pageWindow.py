from appJar import gui

app=gui()

app.setBg("DarkKhaki")
app.setGeometry(280,400)

app.startPagedWindow("Main Title")

app.startPage()
app.addLabel("l13", "Label 1")
app.stopPage()

app.startPage()
app.addLabel("l21", "Label 2")
app.stopPage()

app.startPage()
app.addLabel("l3", "Label 3")
app.stopPage()

app.startPage()
app.addLabel("l4", "Label 4")
app.stopPage()

app.stopPagedWindow()
app.go()
