import sys
sys.path.append("../../")

def press(btn):
    if btn == "add":
        app.setBgImage("map.gif")
    elif btn == "remove":
        app.removeBgImage()
    elif btn == "bgA":
        app.setFg("yellow")
        app.setBg("pink")
    elif btn == "bgB":
        app.setFg("white")
        app.setBg("blue")

from appJar import gui

app=gui("Test BG", "400x400")
app.setBg("green")
app.setFg("orange")
app.addLabel("l1", "Some Label Text")
app.addButtons(["add", "remove", "bgA", "bgB"], press)
app.go()
