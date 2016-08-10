from appJar import gui

app=gui()
app.setFont(20)
app.addLabelOptionBox("Options", ["- Fruits -", "Apple", "Orange", "Pear", "kiwi",
                                "- Pets -", "Dogs", "Cats", "Fish", "Hamsters"])
app.go()
