import sys
sys.path.append("../")
from appJar import gui

app=gui()
app.setFont(20)

app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.addRadioButton("song", "Parklife")

app.go()
