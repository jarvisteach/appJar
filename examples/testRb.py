import sys
sys.path.append("../")
from appJar import gui
import random

val = 0

def press(btn):
      print(btn)

def updateMeter():
      global val
      val = random.randint(0,100)
      app.setMeter("m1", (val, val))
#      val += 1

app=gui()
app.startTabbedFrame("One")
app.startTab("Two")
app.addDualMeter("m1")
#app.setDualMeterFill("m1", ["yellow","blue"])
#app.setMeterFg("m1", "white")
#app.setMeterBg("m1", "red")
app.registerEvent(updateMeter)
app.addRadioButton("song", "Song 1")
app.addRadioButton("song", "Song 2")
app.addRadioButton("song2", "Song 3")

app.setRadioButtonBg("song", "green")
app.setRadioButtonFg("song", "red")
app.setRadioButtonBg("song2", "green")


app.addListBox("list", [1, 2, 3])
app.setListBoxRows("list", 3)
app.addListBox("list2", [1, 2, 3])

app.setListBoxBg("list", "yellow")
app.setListBoxFg("list", "orange")
app.setListBoxBg("list2", "green")

app.addRadioButton("rb1", "Button1")
app.addRadioButton("rb2", "Button2")
app.addRadioButton("rb3", "Button3")

app.setRadioButtonBg("rb1", "purple")
app.setRadioButtonBg("rb2", "orange")
app.setRadioButtonFg("rb2", "pink")

app.addButton("B1", press)
app.addButton("B2", press)
app.addButton("B3", press)
app.addButton("B4", press)

app.setButtonBg("B1", "green")

app.stopTab()
app.stopTabbedFrame()


app.go()
