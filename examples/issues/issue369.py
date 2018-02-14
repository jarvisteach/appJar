import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:

    name = "p1"
    with app.scrollPane(name):#, disabled="vertical"):
        for i in range(50): app.label(name+str(i), "a"*100)
    name = "p2"
    with app.scrollPane(name, disabled="vertical"):
        for i in range(50): app.label(name+str(i), "a"*100)
    name = "p3"
    with app.scrollPane(name, disabled="horizontal"):
        for i in range(50): app.label(name+str(i), "a"*100)
    name = "p4"
    with app.scrollPane(name, disabled="something"):
        for i in range(50): app.label(name+str(i), "a"*100)
