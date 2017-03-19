import sys
sys.path.append("../")

from appJar import gui
def press(btn):
    print("default:", btn)
    if btn == "writing":
        app.setTextArea("t1", "some writing")
    elif btn == "writing2":
        app.setTextArea("t2", "some writing")
    elif btn == "get":
        print(app.getTextArea("t1"))
    elif btn == "get2":
        print(app.getTextArea("t2"))

    elif btn == "log":
        app.logTextArea("t1")
    elif btn == "log2":
        app.logTextArea("t2")

    elif btn == "check":
        print(app.textAreaChanged("t1"))
    elif btn == "check2":
        print(app.textAreaChanged("t2"))

def sub(btn): print("submit ", btn)
def chng(btn):
    print("change ", btn)
    if btn in ["t1", "t2"]: print(app.getTextArea(btn))

app=gui("Event Tester")


app.addLabel("l1", "click me", 0, 0)
app.setLabelChangeFunction("l1", press)

app.addLabel("l2", "click me", 0, 1)
app.setLabelSubmitFunction("l2", press)

app.addEntry("e1", 1, 0, 2)
app.setEntrySubmitFunction("e1", sub)
app.setEntryChangeFunction("e1", chng)

app.addTextArea("t1", 2, 0)
app.setTextAreaSubmitFunction("t1", sub)
app.setTextAreaChangeFunction("t1", chng)

app.addScrolledTextArea("t2", 2, 1)
app.setTextAreaSubmitFunction("t2", sub)
app.setTextAreaChangeFunction("t2", chng)

app.addButton("writing", press, 3, 0)
app.addButton("writing2", press, 3, 1)

app.addButton("get", press, 4, 0)
app.addButton("get2", press, 4, 1)

app.addButton("log", press, 5, 0)
app.addButton("log2", press, 5, 1)

app.addButton("check", press, 6, 0)
app.addButton("check2", press, 6, 1)

app.go()
