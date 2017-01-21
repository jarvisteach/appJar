from appJar import gui

app=gui("Seps", "400x400")
app.setBg("lightblue")

app.addVerticalSeparator(0, 1, 0,3, colour="red")
app.addLabel("l1", "a", 0, 0, 0,3)
app.setLabelBg("l1", "red")
app.addVerticalSeparator(0, 6, 0,3, colour="red")
app.setSticky("nsew")
# should make a  horizontal separator
app.addSeparator(0, 1, 6, colour="red")
app.addVerticalSeparator(1, 2, colour="black")
app.addVerticalSeparator(1, 3, colour="white")
app.addVerticalSeparator(1, 4, colour="orange")
app.addVerticalSeparator(1, 5, colour="green")
app.addHorizontalSeparator(2,1, 6, colour="blue")

app.go()
