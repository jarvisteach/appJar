from appJar import gui

def press(btn):
    app.setBg("green")

app=gui()
app.setBg("yellow")
#app.addPieChart("p1", [50, 200, 75, 300, 150], size=300)
app.addPieChart("p1", {"apples":50, "oanges":200, "grapes":75, "beef":300, "turkey":150}, size=300)
app.addButton("PRESS", press)
app.setButtonTooltip("PRESS", "help me")
app.go()
