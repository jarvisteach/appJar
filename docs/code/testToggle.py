from appJar import gui

def press(btn):
    print(app.getOptionBox("Fred"))

app=gui()
app.setBg("yellow")
app.setFont(40)

#app.addTickOptionBox("Fred", ["Dogs", "Cats", "Elephants Are Super Cool And Funky"])
app.addButton("Check Tick", press)

app.startToggleFrame("Names")
app.addLabelEntry("Person 1")
app.addLabelEntry("Person 2")
app.addLabelEntry("Person 3")
app.addLabelEntry("Person 4")
app.stopToggleFrame()


app.startToggleFrame("Favourites")
app.addRadioButton("fav", "Apples")
app.addRadioButton("fav", "Oranges")
app.addRadioButton("fav", "Pears")
app.addRadioButton("fav", "Grapes")
#app.stopToggleFrame()


app.go()
