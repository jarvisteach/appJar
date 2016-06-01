# import the library
from rwbatools import gui

app = gui()                 # top slice - CREATE the GUI

app.addLabel("title", "Welcome to RWBAtools")   # add a label
app.setLabelBg("title", "red")                  # set the label's background to be red

app.go()                    # bottom slice - START the GUI
