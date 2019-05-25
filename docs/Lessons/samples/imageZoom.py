# import the library
import sys
sys.path.append("../../../")
from appJar import gui

def press(btn):
      red = win.getEntry("Red")
      green = win.getEntry("Green")
      blue = win.getEntry("Blue")
      rgb = "#"+red+green+blue
      print ( rgb )
      win.setBg(rgb )

def zoom(btn):
      print ( win.getScale("scl") )
      win.zoomImage("img", win.getScale("scl"))

# create the GUI and start it
win = gui("Hexadecimal Colours")

#win.setFont(16)
win.addLabelEntry("Red")
win.addLabelEntry("Green")
win.addLabelEntry("Blue")
win.addButton("Submit", press)
win.addScale("scl")
win.setScaleRange("scl", -5, 5)
win.setScaleChangeFunction("scl", zoom)
win.addImage("img", "../resources/8ball.gif")

win.go()
