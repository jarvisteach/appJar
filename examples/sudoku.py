import sys
sys.path.append("../")
import random
from appJar import gui

def clicked(lbl):
    app.setLabel(lbl, app.numBox("Number", "Enter a number"))
    app.setLabelBg(lbl, "green")

def press(btn):
    if btn == "NEW": print("Create new grid")
    elif btn == "RESET": print("Reset grid")
    elif btn == "CHECK": print("Validate grid")
    elif btn == "EXIT": app.stop()

def menu(btn):
    print(btn)

with gui("Sudoku") as app:

    app.addMenuList("File", ["Load", "Save"], menu)
    app.addMenuList("Game", ["New", "Reset", "Check"], menu)

    app.setFont(20)
    app.setBg("PapayaWhip")
    app.addLabel("title", "Welcome to Sudoku")

    with app.frame("grid"):
        for row in range(9):
            for col in range(9):
                name = str(row)+"-"+str(col)
                val = random.choice([1,2,3,4,5,6,7,8,9,"", "", "", ""])
                app.addLabel(name, val, row, col)
                app.setLabelRelief(name, "sunken")
                app.setLabelBg(name, "DarkKhaki")
                app.setLabelSubmitFunction(name, clicked)

    app.addButtons(["NEW", "RESET", "CHECK", "EXIT"], press)
