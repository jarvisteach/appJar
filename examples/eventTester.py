import sys
sys.path.append("../")

from appJar import gui
def press(btn):
    print("default:", btn)

def sub(btn): print("submit ", btn)
def chng(btn): print("change ", btn)

app=gui("Event Tester")


app.addLabel("l1", "click me")
app.setLabelChangeFunction("l1", press)

app.addLabel("l2", "click me")
app.setLabelSubmitFunction("l2", press)

app.addEntry("e1")
app.setEntrySubmitFunction("e1", sub)
app.setEntryChangeFunction("e1", chng)

app.addTextArea("t1")
app.setTextAreaSubmitFunction("t1", sub)
app.setTextAreaChangeFunction("t1", chng)

app.addScrolledTextArea("t2")
app.setTextAreaSubmitFunction("t2", sub)
app.setTextAreaChangeFunction("t2", chng)

app.go()
