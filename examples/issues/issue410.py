import sys
sys.path.append("../../")
from appJar import gui

def press(): pass

app = gui()
app.setFont(20)
app.addTable("g1",
    [["Name", "Age", "Gender"],
    ["Fred", 45, "Male"],
    ["Tina", 37, "Female"],
    ["Clive", 28, "Male"],
    ["Betty", 51, "Female"]],
    action=press
    )
app.go()
