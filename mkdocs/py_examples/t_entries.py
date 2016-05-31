from rwbatools import gui

app=gui()
app.setFont(20)

app.addEntry("e1")
app.addEntry("e2")
app.addEntry("e3")
app.addLabelEntry("Name")
app.setEntryDefault("e2", "Age here")
app.go()

