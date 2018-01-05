import sys
sys.path.append("../")

from appJar import gui

def login(btn):
    app.hideSubWindow("Login")
    app.show()

def stopSub(btn=None):
    return False

app = gui()
app.addLabel("la", "la")

app.startSubWindow("Login")
app.setStopFunction(stopSub)
app.addLabel("l2", "Login Window")
app.addButton("SUBMIT", login)
app.stopSubWindow()

app.startSubWindow("Other")
app.addLabel("l3", "Other Window")
app.stopSubWindow()

app.addButton("Other", app.showSubWindow)

app.go(startWindow="Login")
