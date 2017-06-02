import sys
sys.path.append("../../")

from appJar import gui

def showDate(btn):
    print(app.getDatePicker("dp"))

app=gui()

app.startToggleFrame("Birthday")
app.addDatePicker("dp")
app.addButton("GET", showDate)
app.stopToggleFrame()

app.setDatePickerRange("dp", 1900, 2100)
app.setDatePicker("dp")
app.setDatePickerChangeFunction("dp", showDate)

app.go()
