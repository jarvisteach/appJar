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
    elif btn=="newRow": app.replaceGridRow("grid", 1, app.getGridEntries("grid"))
    elif btn == "HIDE": app.hideGrid("grid")
    elif btn == "SHOW": app.showGrid("grid")
    elif btn == "HEADER": app.setGridHeaders("grid", app.getGridEntries("grid"))
    elif btn == "ALL": app.deleteAllGridRows("grid")
    elif btn == "COUNT": print(app.getGridRowCount("grid"))
    else: app.deleteGridRow("grid", int(btn))
app=gui("600x600", "600x600")
#app.setFg("orange")
#app.setBg("red")
app.addGrid("grid", [["A","B","C"], [3,4,5,6,7,8], [2,4,6,8]], action=press, addRow=press)
app.addButtons(["FRENCH", "SHOW'EM", "UP", "DOWN"], press)
app.addButtons(["HIDE", "SHOW", "DELETE", "ALL", "COUNT", "HEADER"], press)

#app.setGridHeight("grid", 300)

app.go()
