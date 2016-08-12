from appJar import gui

def press(btn=None):
    print("CHANGIN")
    lab = app.getLabelWidget("l1")
    lab.config(bg="red")
    lab.config(width=200)

app=gui()

app.addLabel("l1", "No text")
app.addButton("CHANGE", press)

app.go()
