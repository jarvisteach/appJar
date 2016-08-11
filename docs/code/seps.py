from appJar import gui

app=gui()
app.setBg("lightblue")

app.addSeparator(0, 0, 4, colour="red")
app.addVerticalSeparator(1, 0, colour="black")
app.addVerticalSeparator(1, 1, colour="white")
app.addVerticalSeparator(1, 2, colour="orange")
app.addVerticalSeparator(1, 3, colour="green")
app.addHorizontalSeparator(2, 0, 4, colour="blue")

app.go()
