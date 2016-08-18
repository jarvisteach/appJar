from appJar import gui
def press(btn):
    print(btn)
    if btn=="SHOW'EM":
        print(app.getGridEntries("grid"))
        print(app.getGridSelectedCells("grid"))
    elif btn=="UP": app.increaseFont()
    elif btn=="DOWN": app.decreaseFont()
app=gui()
#app.setFg("orange")
#app.setBg("red")
app.addGrid("grid", [["A","B","C"], [3,4,5,6,7,8], [2,4,6,8]], action=press, addRow=True)
app.addButtons(["SHOW'EM", "UP", "DOWN"], press)

#app.setGridHeight("grid", 300)

app.go()
