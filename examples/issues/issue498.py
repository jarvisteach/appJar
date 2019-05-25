import sys
sys.path.append("../../")

from appJar import gui

def press():
    app.replaceAllTableRows('g1', 
        [["fff", 45, "Male"], ["tttt", 37, "Female"], ["ccc", 28, "Male"], ["bbbb", 51, "Female"]], deleteHeader=True)

with gui() as app:
    app.setFont(20)
    app.addTable("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]])

    app.button('PRESS', press)
