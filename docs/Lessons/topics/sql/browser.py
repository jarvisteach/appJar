from rwbatools import gui
import random

numRows = 20

def getData():
      rows = []
      for loop in range(numRows):
            rows.append(getRanRow(5))
      return rows

def getRanRow(size=10):
      cells = []
      for loop in range(size):
            cells.append(str(random.randint(1,9))*10)
      return cells

# function to handle button press
def press(name):
      win.updateGrid('g1', getData())

# create the window
win = gui("Grid!")
win.addLabel("l1", "hhhhhhhhhaaaaaaaaaaaaaaaaahhhhhhhhhhh" )

win.addGrid('g1', getData())
win.addButton("Rand", press)

win.go()

