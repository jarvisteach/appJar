import sys
sys.path.append("../")

from appJar import gui
def press(btn):
    print(btn)

app=gui("Event Tester")


app.addLabel("l1", "click me")
app.setLabelChangeFunction("l1", press)

app.addLabel("l2", "click me")
app.setLabelSubmitFunction("l2", press)

app.go()
