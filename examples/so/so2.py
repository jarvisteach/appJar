import sys
sys.path.append("../../")
from appJar import gui

hello = True

def press(none):
    global hello
    if hello: print("Hello World!")
    else: print("Goodbye World!")
    hello = not hello

app = gui()
app.setGeometry("300x300")
app.addButton("Button", press)

app.go()
