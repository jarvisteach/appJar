import sys
sys.path.append("../../")


def press(btn):
    print(btn)

from appJar import gui

app=gui()

app.addGrid("g1",
    [["Name", "Age", "Gender"],
    ["Fred", 45, "Male"],
    ["Tina", 37, "Female"],
    ["Clive", 28, "Male"],
    ["Betty", 51, "Female"]],
    action=press, addRow=True)

app.addGridRow("g1", ["a", "b", "c"])

app.go()
