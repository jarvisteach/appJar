import sys
sys.path.append("../../")
from appJar import gui

count = 0

def press(btn):
    global count
    count += 1
    app.setLabel("title", "Count=" + str(count))

    if btn == "PRESS":
        app.setFg("white")
        app.setBg("green")
    elif btn == "PRESS ME TOO":
        app.setFg("green")
        app.setBg("pink")
    elif btn == "PRESS ME AS WELL":
        app.setFg("orange")
        app.setBg("red")

    if count >= 10:
        app.infoBox("You win", "You got the counter to 10")

app = gui("Demo GUI")

app.setBg("yellow")
app.setFg("red")
app.setFont(15)

app.addLabel("title", "Hello World")
app.addMessage("info", "This is a simple demo of appJar")

app.addButton("PRESS", press)
app.addButton("PRESS ME TOO", press)
app.addButton("PRESS ME AS WELL", press)

app.go()
