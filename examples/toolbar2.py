import sys
sys.path.append("../")
from appJar import gui

pin = True

def tbFunc(btn):
    print(btn)

def pin(btn): app.setToolbarPinned(True)
def unpin(btn): app.setToolbarPinned(False)

def tbOut(btn): app.hideToolbar()
def tbIn(btn): app.showToolbar()

app = gui()

app.addToolbar(["Save", "Open", "Close"], tbFunc, True)

app.addButtons(["Pin", "Unpin", "Hide", "Show"], [pin, unpin, tbOut, tbIn])
#app.setToolbarPinned(False)

app.go()
