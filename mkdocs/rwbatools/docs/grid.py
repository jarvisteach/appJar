from rwbatools import gui

app=gui()
app.setFont(20)
app.addGrid("g1",
            [["Name", "Age", "Gender"],
            ["Fred", 45, "Male"],
            ["Tina", 37, "Female"],
            ["Clive", 28, "Male"],
            ["Betty", 51, "Female"]])
app.setGridGeom("g1", 400,400)
app.go()
