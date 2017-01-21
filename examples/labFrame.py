from appJar import gui

app = gui()
app.startLabelFrame("Songs")
app.addRadioButton("song", "Song 1")
app.addRadioButton("song", "Song 2")
app.addRadioButton("song", "Song 3")
app.addRadioButton("song", "Song 4")

app.go()
