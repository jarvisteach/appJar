from rwbatools import gui
options=["Blur", "Queen", "Oasis", "One Direction"]
app=gui("OptionBox Demo", "200x200")

app.addOptionBox("options", options)

app.go()
