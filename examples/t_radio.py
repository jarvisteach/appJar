import sys
sys.path.append("../")
from appJar import gui

def press(rb):
    if rb == "PLAY":
        rb = "song"
    print(app.getRadioButton(rb))

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.setRadioButtonBg("song", "red")
app.setRadioButtonFunction("song", press)   # call this funciton, whenever the RadioButton changes
app.addButton("PLAY", press)
app.go()
