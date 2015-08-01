# import the library
from rwbatools import gui

# create the GUI
win = gui("Hello")

# add a label
win.addLabel ( "lb1", "Hello World" )

# go go go
win.go()
