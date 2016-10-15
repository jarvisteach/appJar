from appJar import gui

def showDate(btn):
    print(app.getDatePicker("dp"))

app=gui()
app.addDatePicker("dp")
app.addButton("GET", showDate)
app.go()
