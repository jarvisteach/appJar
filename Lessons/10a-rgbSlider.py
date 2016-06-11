from appJar import gui

def press(btn):
      
      print(btn, "pressed")

      red = win.getEntry("Red")
      green = win.getEntry("Green")
      blue = win.getEntry("Blue")

      if len(red) == 1: red = "0"+red
      if len(green) == 1: green = "0"+green
      if len(blue) == 1: blue = "0"+blue

      rgb = "#"+red+green+blue

      win.setLabel("col",rgb)
      win.setBg(rgb )

# create the GUI and start it
win = gui("Cols")
win.setFont(16)

win.addLabel("title", "Change my Colour")
win.addLabelEntry("Red")
win.addLabelEntry("Green")
win.addLabelEntry("Blue")
win.addLabel("col", "")
win.addButton("Submit", press)

win.go()
