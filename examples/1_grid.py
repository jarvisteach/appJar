import sys
sys.path.append("../")
from appJar import gui
def press(btn):
    print(btn)
    if btn=="SHOW'EM":
        print(app.getGridEntries("grid"))
        print(app.getGridSelectedCells("grid"))
    elif btn=="UP": app.increaseFont()
    elif btn=="DOWN": app.decreaseFont()
    elif btn=="FRENCH": app.setLanguage("FRENCH")
    elif btn=="newRow": app.addGridRow("grid", app.getGridEntries("grid"))
    elif btn == "HIDE": app.hideGrid("grid")
    elif btn == "SHOW": app.showGrid("grid")
    elif btn == "HEADER": app.setGridHeaders("grid", app.getGridEntries("grid"))
    elif btn == "ALL": app.deleteAllGridRows("grid")
    elif btn == "COL": app.addGridColumn("grid", int(app.getSpinBox("spin")), ["yyy", "zzz"])
    elif btn == "D_COL": app.deleteGridColumn("grid", int(app.getSpinBox("spin")))
    elif btn == "COUNT": print(app.getGridRowCount("grid"))
    elif btn == "SORT": app.sortGrid("grid", 0)
    elif btn == "FONTS":
#        app.setGridBg("grid", "yellow")
        app.setGridActiveBg("grid", "pink")
        app.setGridInactiveBg("grid", "green")
    else:
        if app.getCheckBox("Delete?"):
            app.deleteGridRow("grid", int(btn))
        else:
            print(app.getGridRow("grid", int(btn)))

app=gui()
app.addLabel("title", "Grid Widget Test")
app.setLabelFg("title", "blue")
app.setLabelBg("title", "yellow")
app.setLabelFont(20)
app.addGrid("grid", [["A","B","C"], [3,4,5,6,7], [2,4,6,8]], action=press, addRow=press, showMenu=True)
app.setGridHeight("grid", 400)
with app.labelFrame("LabelFrame Text", hideTitle=True):
    app.addCheckBox("Delete?")
    app.addButtons(["FRENCH", "SHOW'EM", "UP", "DOWN", "FONTS", "SORT"], press)
#app.addButtons(["D_COL", "HIDE", "SHOW", "DELETE", "ALL", "COUNT", "HEADER", "COL"], press)
#app.addSpinBoxRange("spin", 0, 10)
app.go()
