from appJar import gui

app=gui()
app.setFont(20)

app.addFlashLabel("f1", "This is flashing")
app.addLabel("f3", "This is not flashing")
app.addFlashLabel("f2", "This is also flashing")

app.go()
