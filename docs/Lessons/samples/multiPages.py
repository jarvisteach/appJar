# import the library
from rwbatools import gui

# function to handle button presses
def press(btn):
      if btn == "Page A": showPageA()
      elif btn == "Page B": showPageB()
      elif btn == "Page C": showPageC()

# function to make page A
def showPageA():
      win.removeAllWidgets() # this will remove any existing widgets
      win.setBg("Red")
      win.addLabel("l1", "Page A")
      win.addButton("Page B", press)

# function to make page B
def showPageB():
      win.removeAllWidgets()
      win.setBg("Green")
      win.addLabel("l2", "Page B")
      win.addButton("Page C", press)

# function to make page C
def showPageC():
      win.removeAllWidgets()
      win.setBg("Blue")
      win.addLabel("l3", "Page C")
      win.addButton("Page A", press)

# create the GUI, show page A, and GO!
win = gui ( "Hello" )
showPageA()
win.go ( )
