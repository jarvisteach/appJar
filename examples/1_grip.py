from appJar import gui

app=gui()
app.setFont(20)
app.setBg("lightBlue")

app.addLabel("l1", "Move me around...", 0,0)
app.addGrip(0,1)
app.addSeparator(1, 0, 2, colour="red")
app.go()
