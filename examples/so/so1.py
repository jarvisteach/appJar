import sys
sys.path.append("../../")
from appJar import gui

def press(btn):

    if btn == "1":
        app.setLabel("answer", "1!")
    elif btn == "2":
        app.setLabel("answer", "2!")
    elif btn == "3":
        app.setLabel("answer", "3!")
    elif btn == "4":
        app.setLabel("answer", "4!")
    elif btn == "5":
        app.setLabel("answer", "5!")
    elif btn == "6":
        app.setLabel("answer", "6!")
    elif btn == "7":
        app.setLabel("answer", "7!")
    elif btn == "8":
        app.setLabel("answer", "8!")
    elif btn == "9":
        app.setLabel("answer", "9!")
    elif btn == "10":
        app.setLabel("answer", "10!")
        app.startScrollPane("scroller")
    elif btn == "11":
        app.setLabel("answer", "11!")
    elif btn == "12":
        app.setLabel("answer", "12!")
        app.stopScrollPane("scroller")

def updateButtons(btn=None):
    m = app.getScale("scroller") * 10
    for i in range(1, 13):
        print(i)
        app.setButton (str(i), str(m+i))


app=gui()
app.setFont(20)
app.startScrollPane("p1")
for i in range(1,101):
    app.addButton(str(i), press, 0, i)
app.stopScrollPane()
app.addScale("scroller")
app.setScaleRange("scroller", 0, 9)
app.setScaleChangeFunction("scroller", updateButtons)
app.addLabel ("answer", "Pick a Number!")
updateButtons()
app.go()

