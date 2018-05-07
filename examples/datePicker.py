import sys
sys.path.append("../")

from appJar import gui

def press(btn):
    if btn == "CLEAR": app.clearDatePicker("dp1")
    elif btn == "CLEAR ALL": app.clearAllDatePickers()
    elif btn == "GET": print(app.getDatePicker("dp1"))
    elif btn == "SET": app.setDatePicker("dp1")

app=gui()
app.addDatePicker("dp1")
app.addButtons(["CLEAR", "CLEAR ALL", "GET", "SET"], press)
app.setBg("red")
app.go()
