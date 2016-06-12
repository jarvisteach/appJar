from appJar import gui

def press(btn):
    if btn=="Save":
        n=app.getEntry("name")
        a=app.getEntry("age")
        r=app.getOptionBox("role")
        app.infoBox("Details", "You entered: {}, {}, {}".format(n, str(a), r))
    elif btn=="Quit":
        app.stop()

app=gui()

app.addLabel("l1", "Name", 0, 0)
app.addLabel("l2", "Age", 1, 0)
app.addLabel("l3", "Role", 2, 0)

app.addEntry("name", 0, 1)
app.addNumericEntry("age", 1, 1)
app.addOptionBox("role", ["Teacher", "Student", "Developer", "Volunteer"], 2, 1)

app.addButtons(["Save", "Quit"], press, 3, 0, 2)

app.go()
