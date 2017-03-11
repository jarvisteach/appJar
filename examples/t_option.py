from appJar import gui
songs=["Killer Queen", "Paradise City", "Parklife"]

def press(btn):
    print(app.getOptionBox("song"))

app=gui()
app.addOptionBox("song", songs)
app.addButton("PLAY", press)
app.go()
