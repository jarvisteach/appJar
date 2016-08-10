from appJar import gui

def get(btn):
    print(app.getOptionBox("Favourite Pets"))

app=gui()
app.setFont(20)

app.addTickOptionBox("Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"])
app.addLabelTickOptionBox("More Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"])
app.setOptionBox("Favourite Pets", 3)
app.addButton("GET", get)

app.go()
