# import the library
from appJar import gui

app = gui()                 # top slice - CREATE the GUI

app.addLabel("title", "Welcome to appJar")   # add a label
app.setLabelBg("title", "red")                  # set the label's background to be red

app.go()                    # bottom slice - START the GUI
