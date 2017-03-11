import sys
sys.path.append("../../")
from appJar import gui

app=gui("Languages")

app.addLabel("l1", "default text")
app.addLabel("l2", "default text")
app.addLabel("l3", "default text")
app.addButtons(["ENGLISH", "FRENCH", "KOREAN"], app.changeLanguage)

app.go("ENGLISH")
