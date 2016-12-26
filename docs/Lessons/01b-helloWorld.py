# import the library
from appJar import gui

# count how many times button is pressed
count = 0

# function to deal with button press
def press ( btn ) :
      global count
      count += 1
      win.setLabel ( "lb1", "Pressed: " + str(count) + " times" )

# create the GUI
win = gui("Hello")

# configure the GUI
win.setBg("Red")
win.setFont(20)

# add the 3 labels
win.addLabel ( "lb1", "Hello World" )
win.addLabel ( "lb2", "Hello again" )
win.addLabel ( "lb3", "And... goodbye" )

# configure label 1
win.setLabelBg ( "lb1", "yellow" )
win.setLabelFg ( "lb1", "blue" )

# add the button
win.addButton("Press me", press)

# go go go
win.go()
