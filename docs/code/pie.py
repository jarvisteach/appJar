from appJar import gui

def press(btn):
    app.setBg("green")

app=gui()
app.setBg("yellow")
app.addPieChart("p1", [50, 200, 75, 300, 150], size=300)
app.addButton("PRESS", press)
app.go()
