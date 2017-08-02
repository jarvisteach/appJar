import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(app.getGridEntries("g1"))
    print(app.getGridSelectedCells("g1"))
    app.addGridRow("g1", ["a", "b", "c"])

def remove(btn):
    print(btn)
    print(app.getGridEntries("g1"))
    print(app.getGridSelectedCells("g1"))
    app.addGridRow("g1", ["a", "b", "c"])

app=gui()
app.setFont(20)
app.addGrid("g1",
    [["Name", "Age", "Gender"],
    ["Fred", 45, "Male"],
    ["Tina", 37, "Female"],
    ["Clive", 28, "Male"],
    ["Betty", 51, "Female"]],
    action=press,
    addRow=press,
    actionColumnText = "Delete",
    actionButtonLabel = "This One",
    addRowButtonLabel = "Add New One"
    )


app.addButton("PRESS ME", press)
app.go()
